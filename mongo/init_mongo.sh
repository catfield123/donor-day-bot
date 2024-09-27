#!/bin/sh

export TERM=xterm

set -e

if [ -z "$FSM_USER" ]; then
  echo "Error: Missing environment variable FSM_USER"
  exit 1
fi

if [ -z "$FSM_PASSWORD" ]; then
  echo "Error: Missing environment variable FSM_PASSWORD"
  exit 1
fi

if [ -z "$FSM_DB" ]; then
  echo "Error: Missing environment variable FSM_DB"
  exit 1
fi


mongosh <<EOF

// Check for the existence of the database FSM_DB
let dbExists = db.getSiblingDB('$FSM_DB').runCommand({ isMaster: 1 }).ok === 1;

if (!dbExists) {
  print("Database '$FSM_DB' does not exist. Creating it now.");
  db.getSiblingDB('$FSM_DB').runCommand({ create: '$FSM_DB' });
  print("Database '$FSM_DB' created successfully.");
} else {
  print("Database '$FSM_DB' already exists.");
}

use $FSM_DB

// Check for the existence of the user FSM_USER in the database FSM_DB. 
let userExists = db.getUser('$FSM_USER') !== null;

if (!userExists) {
  // If user doesn't exist, create it.
  db.createUser({
    user: '$FSM_USER',
    pwd:  '$FSM_PASSWORD',
    roles: [{
      role: 'readWrite',
      db: '$FSM_DB'
    }]
  });
  print("User '$FSM_USER' created successfully in database '$FSM_DB'.");
} else {
  print("User '$FSM_USER' already exists in the database.");
}
EOF
