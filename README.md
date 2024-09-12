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

1. Clone the repository:
```
git clone https://github.com/yourusername/donor-registration-bot.git
cd donor-registration-bot
```

2. Create an environment file with your token:
```
chmod +x create_env_file.sh
./create_env_file.sh
```
This script will ask you to paste your telegram bot token. Just paste it and press enter.


You can also create this file manually. File must contain following:
```
TELEGRAM_BOT_TOKEN=<token>
```
For example:
```
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
```

3. Configure Google Sheets.

4. Run docker containers:
```bash
docker compose build
docker compose up -d
```

### Usage

Once the bot is up and running, it will:

- Interact with users to collect essential information.
- Automatically save all the collected data into a pre-configured Google Sheet.
