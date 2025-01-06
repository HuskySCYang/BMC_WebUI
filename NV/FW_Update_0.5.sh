#!/bin/bash

# Read parameters from Config.txt file
while IFS=':' read -r key value; do
    # Remove leading and trailing spaces from the value
    value=$(echo "$value" | tr -d '[:space:]')
    # Set corresponding variables based on key-value pairs
    case "$key" in
        BMC_IP) BMC_IP="$value" ;;
        UserName) BMC_USER="$value" ;;
        PassWord) BMC_PASS="$value" ;;
        Default) DEFAULT_USER="$value" ;;
        Img_New) IMG_NEW="$value" ;;
        Img_Old) IMG_OLD="$value" ;;
        *) ;;
    esac
done < config.txt

# Output the values of read variables for confirmation
echo "BMC_IP: $BMC_IP"
echo "BMC_USER: $BMC_USER"
echo "BMC_PASS: $BMC_PASS"
echo "DEFAULT_USER: $DEFAULT_USER"
echo "IMG_NEW: $IMG_NEW"
echo "IMG_OLD: $IMG_OLD"

# Prompt user to confirm Config information
read -p "Are the Config.txt settings correct? (Y/N): " choice

# Convert choice to uppercase
choice=$(echo "$choice" | tr '[:lower:]' '[:upper:]')

# Check user input
case "$choice" in
  Y)
    echo "Proceeding with the provided Config settings..."
    ;;
  *)
    echo "Exiting the script. Please check Config.txt and run the script again."
    exit 1
    ;;
esac

# Prompt user to choose test time or test cycles
echo "1) 12 hours    3) 48 hours    5) 1000 cycles"
echo "2) 24 hours    4) 60 hours    6) Custom cycles"
read -p "Choose the test time or test cycles: " option

# Based on the user's choice, perform the corresponding action
case "$option" in
  1) 
    duration=12
    unit="hours"
    ;;
  2)
    duration=24
    unit="hours"
    ;;
  3)
    duration=48
    unit="hours"
    ;;
  4)
    duration=60
    unit="hours"
    ;;
  5)
    duration=1000
    unit="cycles"
    ;;
  6)
    read -p "Please input the test cycles: " duration
    unit="cycles"
    ;;
  *)
    echo "Invalid choice. Exiting the script."
    exit 1
    ;;
esac

# Output the chosen test duration
echo "Test duration: $duration $unit"

# Prompt user to save WEBGUI settings
read -p "Do you want to save the WEBGUI settings? (Y/N): " save_choice

# Convert save choice to uppercase
save_choice=$(echo "$save_choice" | tr '[:lower:]' '[:upper:]')

# Check user input1
case "$save_choice" in
  Y)
    echo "Saving WEBGUI settings..."
    ./YafuflashAop.a04 -nw -ip $BMC_IP -u $BMC_USER -p $BMC_PASS -img-select 1 $IMG_NEW -fb -pc
    ;;
  *)
    echo "Not saving WEBGUI settings. Exiting the script."
    ./YafuflashAop.a04 -ip $BMC_IP -u $BMC_USER -p $BMC_PASS -img-select 1 $IMG_NEW -fb
    ;;
esac

# Wait for 3 minutes
sleep 180

# Check user input2
case "$save_choice" in
  Y)
    echo "Saving WEBGUI settings..."
    echo "Executing the save loop..."
    # Start loop based on test duration
    echo "Starting save loop with $duration $unit..."
    for ((i=1; i<=$duration; i++)); do
        # Perform save loop actions here
        echo "Save loop cycle $i"
        # Perform action to save here
        ./YafuflashAop.a04 -nw -ip $BMC_IP -u $BMC_USER -p $BMC_PASS -img-select 1 $IMG_OLD -fb -pc
Sleep 180
        # Check if it's the last cycle, if so, switch to new image
        if [ $i -eq $duration ]; then
            echo "Switching to new image..."
        ./YafuflashAop.a04 -nw -ip $BMC_IP -u $BMC_USER -p $BMC_PASS -img-select 1 $IMG_NEW -fb -pc
        fi
    done
Sleep 180    
    ;;
  *)
    echo "Not saving WEBGUI settings. Exiting the script."
    echo "Executing the no-save loop..."
    # Start loop based on test duration
    echo "Starting no-save loop with $duration $unit..."
    for ((i=1; i<=$duration; i++)); do
        # Perform no-save loop actions here
        echo "No-save loop cycle $i"
        # Perform action not to save here
        ./YafuflashAop.a04 -nw -ip $BMC_IP -u $BMC_USER -p $DEFAULT_USER -img-select 1 $IMG_OLD -fb
Sleep 180        
        # Check if it's the last cycle, if so, switch to new image
        if [ $i -eq $duration ]; then
            echo "Switching to new image..."
        ./YafuflashAop.a04 -nw -ip $BMC_IP -u $BMC_USER -p $DEFAULT_USER -img-select 1 $IMG_NEW -fb
        fi
    done
Sleep 180    
    ;;
esac

echo "Execution completed."
