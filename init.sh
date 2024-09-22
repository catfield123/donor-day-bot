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


# MONGO ENV VARIABLES
generate_mongo_env_variables() {
  filename_root="mongo/.root.env"
  filename_fsm="mongo/.fsm.env"
  echo "Generating $filename_root and $filename_fsm"
  check_file_exists $filename_root
  check_file_exists $filename_fsm
  if confirm "Do you want to proceed? [y/N]"; then
      echo MONGO_INITDB_DATABASE=dd_mongo > $filename_root
      echo MONGO_INITDB_ROOT_USERNAME=dd_root_user >> $filename_root
      echo MONGO_INITDB_ROOT_PASSWORD=\"$(generate_password)\" >> $filename_root
      
      echo FSM_DB=fsm_db > $filename_fsm
      echo FSM_USER=fsm_user >> $filename_fsm
      echo FSM_PASSWORD=\"$(generate_password)\" >> $filename_fsm

      message="$filename_root generated successfully \n$filename_fsm generated successfully\n\n"
  else
      message="$filename_root generation canceled. \n$filename_fsm generation canceled.\n\n"
  fi
}


# TELEGRAM BOT TOKEN ENV
generate_user_bot_token_env() {
  filename="user_token.env"
  echo "Generating $filename"
  check_file_exists $filename

  if confirm "Do you want to proceed? [y/N]"; then
      read -s -p "Please enter the Telegram Bot Token for users: " token
      echo USER_BOT_TOKEN="$token" > $filename
      message="$filename generated successfully.\n\n"
  else
      message="$filename generation canceled.\n\n"
  fi
}


# TELEGRAM USER BOT TOKEN ENV
generate_staff_bot_token_env() {
  filename="staff_token.env"
  echo "Generating $filename"
  check_file_exists $filename

  if confirm "Do you want to proceed? [y/N]"; then
      read -s -p "Please enter the Telegram Bot Token for staff: " token
      echo STAFF_BOT_TOKEN="$token" > $filename
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
    options=('database/.db.env file' 'mongo/.root.env & mongo/.fsm.env files' 'user_token.env - user bot token' 'staff_token.env - staff bot token' 'Exit')
    show_menu "$message" "${options[@]}"

    choice=$?

    case $choice in
        0)
            clear
            generate_db_env_variables
            ;;
        1)
            clear
            generate_mongo_env_variables
            ;;
        2)
            clear
            generate_user_bot_token_env
            ;;
        3)
            clear
            generate_staff_bot_token_env
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            message="Invalid option"
            ;;
    esac
done
