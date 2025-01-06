#!/bin/bash

# Function to check if FIO is installed
check_fio_installed() {
    if ! command -v fio &> /dev/null; then
        echo "FIO is not installed. Installing..."
        sudo apt update
        sudo apt install fio -y
    else
        echo "FIO is already installed."
    fi
}

# Function to list SATA drives with Model and capacity
list_sata_drives() {
    echo " ----------SATA----------"
    lsblk -d -o NAME,MODEL,SIZE | awk '/sd[a-z]/&&!/Virtual/ {print ++count":", "/dev/"$1":", $2, $3, "| Size:", $4}' count=0
}

# Function to list NVME drives with Model and capacity
list_nvme_drives() {
    echo " ----------NVME----------"
    lsblk -d -o NAME,MODEL,SIZE | awk '/nvme/&&!/Virtual/ {print ++count":", "/dev/"$1":", $2, $3, "| Size:", $4}' count=0
}

# Function to display available drives
display_available_drives() {
    list_sata_drives
    list_nvme_drives
}

# Function to select drive type (SATA or NVME)
select_drive_type() {
    echo "Select drive type:"
    echo "1. SATA"
    echo "2. NVME"
    read -p "Enter the number of the drive type you want to select: " drive_type
}

# Function to select OS drive
select_os_drive() {
    read -p "Enter the number of the drive you want to select: " selected_drive_number
    selected_drive=""
    if [[ "$selected_drive_number" =~ ^[0-9]+$ ]]; then
        if [ "$drive_type" -eq 1 ]; then
            selected_drive=$(lsblk -d -o NAME | awk '/sd[a-z]/&&!/Virtual/ {++count; if (count=='$selected_drive_number') print "/dev/"$1}')
        elif [ "$drive_type" -eq 2 ]; then
            selected_drive=$(lsblk -d -o NAME | awk '/nvme/&&!/Virtual/ {++count; if (count=='$selected_drive_number') print "/dev/"$1}')
        else
            echo "Invalid drive type."
        fi
    else
        echo "Invalid input. Please enter a number."
    fi
    
    if [ -n "$selected_drive" ]; then
        echo "You selected: $selected_drive"
    fi
}

# Main function
main() {
    check_fio_installed
    display_available_drives
    select_drive_type
    if [ "$drive_type" -eq 1 ]; then
        list_sata_drives
    elif [ "$drive_type" -eq 2 ]; then
        list_nvme_drives
    else
        echo "Invalid drive type."
        exit 1
    fi
    select_os_drive
}

# Execute main function
main
