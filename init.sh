#!/bin/bash

generate_password() {
    local length=32
    local password=""

    local ALLOWED_CHARS="a-zA-Z0-9=_+\-#%"

    while [ ${#password} -lt $length ]; do
        password=$(tr -dc "$ALLOWED_CHARS" < /dev/urandom | head -c $length)
    done

    echo "$password"

}


# Function to prompt the user
confirm() {
    read -r -p "${1:-Are you sure? [y/N]} " response
    case "$response" in
        [yY][eE][sS]|[yY])
            true
            ;;
        *)
            false
            ;;
    esac
}

RED='\033[0;31m'
NC='\033[0m' # No Color
# Function to check if a file exists and print a warning
check_file_exists() {
    if [ -f "$1" ]; then
        printf "${RED}: $1 already exists.${NC}\n"
        return 0
    else
        return 1
    fi
}


message=""

# DB ENV VARIABLES
generate_db_env_variables() {
  filename="database/.db.env"
  echo "Generating $filename"
  check_file_exists $filename
  if confirm "Do you want to proceed? [y/N]"; then
      echo "POSTGRES_USER=dd_user" > $filename
      echo POSTGRES_PASSWORD=\"$(generate_password)\" >> $filename
      echo POSTGRES_DB=dd_database >> $filename

      message="$filename generated successfully\n\n"
  else
      message="$filename generation canceled.\n\n"
  fi
}


# TELEGRAM BOT TOKEN ENV
generate_bot_token_env() {
  filename="token.env"
  echo "Generating $filename"
  check_file_exists $filename

  if confirm "Do you want to proceed? [y/N]"; then
      read -p "Please enter the Telegram Bot Token: " token
      echo TELEGRAM_BOT_TOKEN="$token" > $filename
      message="$filename generated successfully.\n\n"
  else
      message="$filename generation canceled.\n\n"
  fi
}









# Функция для отображения меню
function show_menu() {
    local message=$1
    shift

    local choices=("$@")
    local num_choices=${#choices[@]}
    local selected=0
    local key

    
    while true; do
        clear
        printf "$message"
        printf "Choose file you want to generate:\n"
        for ((i = 0; i < num_choices; i++)); do
            if [ "$i" -eq "$selected" ]; then
                echo "> ${choices[$i]}"
            else
                echo "  ${choices[$i]}"
            fi
        done

        # Чтение нажатой клавиши
        read -rsn1 key

        case "$key" in
            # Стрелочка вниз
            $'\x1b' )
                read -rsn1 key
                if [ "$key" == "[" ]; then
                    read -rsn1 key
                    if [ "$key" == "B" ]; then
                        selected=$(( (selected + 1) % num_choices ))
                    fi
                    if [ "$key" == "A" ]; then
                        selected=$(( (selected - 1 + num_choices) % num_choices ))
                    fi
                fi
                ;;
            "" )
                return $selected
                ;;
            # Выход по 'q'
            q )
                echo "Выход"
                exit 0
                ;;
        esac
    done
}


while true; do
    options=('Database .env file' 'Bot token .env file' 'Exit')
    show_menu "$message" "${options[@]}"

    choice=$?

    case $choice in
        0)
            clear
            generate_db_env_variables
            ;;
        1)
            clear
            generate_bot_token_env
            ;;
        2)
            echo "Exiting..."
            exit 0
            ;;
        *)
            message="Invalid option"
            ;;
    esac
done
