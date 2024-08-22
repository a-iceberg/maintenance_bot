#!/bin/bash

pip3 install --upgrade pip
pip3 install -r requirements.txt

#python3 reserve_bot.py

read -p "Please enter your Telegram bot token: " BOT_TOKEN

if [ -z "$BOT_TOKEN" ]; then
    echo "Error: Bot token cannot be empty"
    exit 1
fi

nohup python3 reserve_bot.py "$BOT_TOKEN" > /dev/null 2>&1 &

echo "Bot started. Check reserve_bot.log for output"