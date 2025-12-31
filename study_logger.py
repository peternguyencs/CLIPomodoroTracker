import time
from datetime import datetime
import csv
import os

# 1 SETUP: Define the log file name
LOG_FILE = "study_sessions.csv"

def initialize_log():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Start Time", "Topic", "Duration (Mins)"])


def start_pomodoro(minutes, topic):
    """Handles the countdown logic."""
    seconds = minutes * 60
    start_time = datetime.now().strftime("%H:%M") # Military Time

    print(f"\n[STAY FOCUSED] Session started at {start_time}")
    print(f"Topic: {topic}")

    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            # This '\r' overwrites the same line in the terminal
            print(f"Time Remaining: {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            seconds -= 1

        print("\n\n[COMPLETE] Great Job, Peter. Session logged.")
        save_to_log(start_time, topic, minutes)

    except KeyboardInterrupt:
        print("\n\n[STOPPED] Session cancelled. No data saved.")

def save_to_log(start_t, topic, duration):
    """Appends the completed session to our CSV file."""
    date_today = datetime.now().strftime("%Y-%m-%d")
    with open(LOG_FILE, mode='a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_today, start_t, topic, duration])

# 3. MAIN EXECUTION
if __name__ == "__main__":
    initialize_log()
    print("=== BSCS STUDY LOGGER ===")

    current_topic = input("What are you studing right now? ")
    # Using 25 minutes for a standard Pomodoro
    start_pomodoro(25, current_topic)

