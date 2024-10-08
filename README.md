# Donor Registration Bot

A simple chatbot designed to collect essential donor information and streamline the registration process for blood donation events. The bot records data such as full name, date of birth, passport number, appointment details, and more. The collected information is stored in a Google Sheet for easy access by the event organizers.

## Features

- **Donor Registration**: Collects the donor's name, date of birth, passport number, and preferred donation time and place.
- **Data Export**: Automatically exports the collected data to Google Sheets for easy access and management.
- **Reminders**: Sends reminders to registered donors about their appointments and other event information.
- **Customizable Messaging**: Different messages for volunteers and staff, as well as personalized notifications for donors depending on location.

## Getting Started

### Prerequisites

To run this bot locally, you will need:

- telegram bot token
- docker and docker compose installed on your machine

### Installation

#### 1. Clone the repository:
```
git clone https://github.com/catfield123/donor-day-bot
cd donor-day-bot
```

#### 2. Create environment files:

##### Using init scripts
```
chmod +x init.sh
./init.sh
```
This script can generate .env file with password for database and  ask you to paste your telegram bot token. Just paste it and press enter. Note, that token is hidden while you are entering it in terminal. 


##### Manually

File `user_token.env` must contain following:
```
USER_BOT_TOKEN=<token>
```
For example:
```
USER_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
```

File `staff_token.env` must contain following:
```
STAFF_BOT_TOKEN=<token>
```

File `database/.db.env` must contain following:
```
POSTGRES_USER=dd_user
POSTGRES_PASSWORD="YOUR_SECRET_PASSWORD_HERE"
POSTGRES_DB=dd_database
```

File `mongo/.root.env` must contain following:
```
MONGO_INITDB_DATABASE=dd_mongo
MONGO_INITDB_ROOT_USERNAME=dd_root_user
MONGO_INITDB_ROOT_PASSWORD="YOUR_SECRET_PASSWORD_HERE"
```

File `mongo/.fsm.env` must contain following:
```
FSM_DB=fsm_db
FSM_USER=fsm_user
FSM_PASSWORD="YOUR_SECRET_PASSWORD_HERE"
```

#### 3. Configure Google Sheets.

#### 4. Pre-build docker container with uv installed. Copy and run following command in terminal:
```
echo 'FROM python:3.11-slim-buster
RUN pip install uv' | docker build -t python:3.11-slim-buster-uv -
```

#### 5. Run docker containers:
```bash
docker compose build
docker compose up -d
```

### Usage

Once the bot is up and running, it will:

- Interact with users to collect essential information.
- Automatically save all the collected data into a pre-configured Google Sheet.
