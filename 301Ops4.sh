#!/bin/bash

while true; do
    clear
    echo "Menu:"
    echo "1. Hellow World Semper Fi"
    echo "2. Ping Self"
    echo "3. IP Info"
    echo "4. Exit"
    
    read -p "Enter your choice (1-4): " choice

    case $choice in
        1)
            echo "Hellow World Semper Fi!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    read -p "Press Enter to continue..."
done
