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
use admin

# Проверка существования пользователя перед его созданием
if (db.getUser('$FSM_USER') === null) {
  db.createUser({
    user: '$FSM_USER',
    pwd:  '$FSM_PASSWORD',
    roles: [{
      role: 'readWrite',
      db: '$FSM_DB'
    }]
  });
  print("User '$FSM_USER' created successfully.");
} else {
  print("User '$FSM_USER' already exists.");
}
EOF
