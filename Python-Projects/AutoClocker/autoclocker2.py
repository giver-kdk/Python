import tkinter as tk
from tkinter import ttk
import threading
import time
import schedule
import pyautogui
from datetime import datetime
import psutil
import subprocess
import os
import random

class TeamsAutoTyper:
    def __init__(self, root):
        self.root = root
        self.root.title("Teams Auto Typer")
        self.root.geometry("500x400")

        self.running = False
        self.days_disabled = {
            "Mon": False,
            "Tue": False,
            "Wed": False,
            "Thu": False,
            "Fri": False
        }

        # Threshold control
        self.threshold_label = ttk.Label(root, text="Randomness Threshold (minutes):")
        self.threshold_label.pack(pady=5)

        self.threshold_var = tk.IntVar(value=15)  # Default threshold is 15 minutes
        self.threshold_spinbox = ttk.Spinbox(root, from_=0, to=60, textvariable=self.threshold_var, width=5)
        self.threshold_spinbox.pack(pady=5)

        # Toggle button
        self.toggle_button = ttk.Button(root, text="Start", command=self.toggle)
        self.toggle_button.pack(pady=10)

        # Days checkboxes and time entries
        self.day_vars = {}
        self.time_entries = {}  # To store time entry widgets

        for day in self.days_disabled.keys():
            frame = ttk.Frame(root)
            frame.pack(pady=5)

            # Checkbox for enabling/disabling the day
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(frame, text=day, variable=var, onvalue=True, offvalue=False)
            chk.pack(side=tk.LEFT, padx=5)
            self.day_vars[day] = var

            # Time entry for type-in
            type_in_label = ttk.Label(frame, text="Type-In:")
            type_in_label.pack(side=tk.LEFT, padx=5)
            type_in_entry = ttk.Entry(frame, width=8)
            type_in_entry.insert(0, "09:30")  # Default type-in time
            type_in_entry.pack(side=tk.LEFT, padx=5)
            self.time_entries[f"{day}_in"] = type_in_entry

            # Time entry for type-out
            type_out_label = ttk.Label(frame, text="Type-Out:")
            type_out_label.pack(side=tk.LEFT, padx=5)
            type_out_entry = ttk.Entry(frame, width=8)
            type_out_entry.insert(0, "18:30")  # Default type-out time
            type_out_entry.pack(side=tk.LEFT, padx=5)
            self.time_entries[f"{day}_out"] = type_out_entry

        # Teams path input (unchanged)
        self.teams_path = r"C:\Program Files\WindowsApps\MSTeams_25060.205.3499.6849_x64__8wekyb3d8bbwe\ms-teams.exe"
        self.image_path = r'D:\CODES\Python\Python-Projects\AutoClocker\chat-image.png'

        # Schedule jobs
        self.schedule_jobs()

        # Ensure the app runs in the background
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def toggle(self):
        self.running = not self.running
        self.toggle_button.config(text="Stop" if self.running else "Start")
        if self.running:
            self.run_scheduler()

    def add_randomness(self, base_time):
        """
        Add randomness to a base time within the specified threshold.
        :param base_time: The base time in "HH:MM" format.
        :return: A new time string with randomness applied.
        """
        threshold_minutes = self.threshold_var.get()
        hours, minutes = map(int, base_time.split(':'))
        total_minutes = hours * 60 + minutes
        offset = random.randint(-threshold_minutes, threshold_minutes)
        total_minutes += offset
        total_minutes %= 1440  # Handle wrapping around midnight
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        return f"{new_hours:02d}:{new_minutes:02d}"

    def schedule_with_randomness(self, day, base_time, task):
        """
        Schedule a task with randomness applied to the base time.
        :param day: The day of the week (e.g., schedule.every().monday).
        :param base_time: The base time in "HH:MM" format.
        :param task: The function to execute.
        """
        random_time = self.add_randomness(base_time)
        day.at(random_time).do(task)

    def schedule_jobs(self):
        # Clear existing jobs
        schedule.clear()

        # Schedule tasks with randomness for each day
        for day in self.days_disabled.keys():
            if not self.day_vars[day].get():  # Skip if the day is disabled
                continue

            # Get type-in and type-out times from the GUI
            type_in_time = self.time_entries[f"{day}_in"].get()
            type_out_time = self.time_entries[f"{day}_out"].get()

            # Schedule type-in and type-out tasks
            self.schedule_with_randomness(schedule.every().__getattribute__(day.lower()), type_in_time, self.type_in)
            self.schedule_with_randomness(schedule.every().__getattribute__(day.lower()), type_out_time, self.type_out)

    def is_teams_running(self):
        """Check if Microsoft Teams is running."""
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'Teams.exe':
                return True
        return False

    def open_teams(self):
        """Open Microsoft Teams if it's not running."""
        if not self.is_teams_running():
            if os.path.exists(self.teams_path):
                subprocess.Popen([self.teams_path, '--processStart', 'Teams.exe'])
                time.sleep(10)  # Wait for Teams to open
            else:
                print("Microsoft Teams not found. Please ensure it is installed.")
                return False
        return True

    def navigate_to_chat(self, chat_name):
        """Navigate to the chat window named 'SpiralBot'."""
        # Simulate pressing Ctrl+E to focus on the search bar
        pyautogui.hotkey('ctrl', 'e')
        time.sleep(1)

        # Clear text field
        pyautogui.hotkey("ctrl", "a")  # Select all text
        pyautogui.press("backspace")   # Clear the field

        # Type the chat name
        pyautogui.write(chat_name)
        time.sleep(1)  # Wait for search results to load

        # Locate the chat in the search results and click on it
        try:
            # Use pyautogui to locate the chat name on the screen
            chat_position = pyautogui.locateOnScreen(self.image_path, confidence=0.8)
            if chat_position:
                # Calculate the center of the located image
                chat_center = pyautogui.center(chat_position)
                # Move the mouse to the center and click
                pyautogui.moveTo(chat_center)
                pyautogui.click()
                time.sleep(1)  # Wait for the chat to open
                pyautogui.hotkey("ctrl", "r")  # Focus on chat box
            else:
                print(f"Chat '{chat_name}' not found in search results.")
        except Exception as e:
            print(f"Error locating chat: {e}")

    def type_in(self):
        if not self.running or self.days_disabled[datetime.now().strftime("%a")]:
            return
        if self.open_teams():
            self.navigate_to_chat("SpiralBot")
            pyautogui.write("Hi")
            pyautogui.press("enter")

    def type_out(self):
        if not self.running or self.days_disabled[datetime.now().strftime("%a")]:
            return
        if self.open_teams():
            self.navigate_to_chat("SpiralBot")
            pyautogui.write("Out")
            pyautogui.press("enter")

    def run_scheduler(self):
        def scheduler_loop():
            while self.running:
                schedule.run_pending()
                time.sleep(1)

        threading.Thread(target=scheduler_loop, daemon=True).start()

    def update_days_disabled(self):
        for day, var in self.day_vars.items():
            self.days_disabled[day] = var.get()

    def on_close(self):
        """Handle the window close event."""
        if self.running:
            self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TeamsAutoTyper(root)
    root.mainloop()