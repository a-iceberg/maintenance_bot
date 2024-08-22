#!/bin/bash

BOT_PID=$(pgrep -f "python3 reserve_bot.py")

if [ -z "$BOT_PID" ]; then
    echo "Bot is not running"
    exit 0
fi

echo "Stopping bot (PID: $BOT_PID)..."

kill -15 $BOT_PID

for i in {1..10}; do
    if ! ps -p $BOT_PID > /dev/null; then
        echo "Bot stopped successfully"
        exit 0
    fi
    sleep 1
done

echo "Bot did not stop gracefully. Forcing termination..."
kill -9 $BOT_PID

if ! ps -p $BOT_PID > /dev/null; then
    echo "Bot terminated."
else
    echo "Failed to terminate bot. Please check manually"
fi