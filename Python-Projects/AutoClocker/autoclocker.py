import tkinter as tk
import ctypes
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import threading
import time
import schedule
import pyautogui
from datetime import datetime
import psutil
import subprocess
import os
import random
import json

class TeamsAutoTyper:
    def __init__(self, root):
        self.root = root
        self.root.title("Teams Auto Typer")
        self.root.geometry("500x400")
        self.running = False

        # Load configuration
        self.config_file = r"D:\CODES\Python\Python-Projects\AutoClocker\config\config.json"
        self.load_config()

        # Days enabled (default: all days are enabled)
        self.days_enabled = {
            "Mon": True,
            "Tue": True,
            "Wed": True,
            "Thu": True,
            "Fri": True
        }

        # Threshold control
        self.threshold_label = ttk.Label(root, text="Randomness Threshold (minutes):")
        self.threshold_label.pack(pady=5)

        self.threshold_var = tk.IntVar(value=self.config.get("threshold", 15))  # Default threshold is 15 minutes
        self.threshold_spinbox = ttk.Spinbox(root, from_=0, to=60, textvariable=self.threshold_var, width=5)
        self.threshold_spinbox.pack(pady=5)

        # Toggle button
        self.toggle_button = ttk.Button(root, text="Start" if not self.config.get("running", False) else "Stop", command=self.toggle)
        self.toggle_button.pack(pady=10)

        # Edit button
        self.edit_button = ttk.Button(root, text="Edit Times", command=self.toggle_edit_mode)
        self.edit_button.pack(pady=5)

        # Days checkboxes and time entries
        self.day_vars = {}
        self.time_entries = {}  # To store time entry widgets
        self.edit_mode = False  # Whether time entries are editable

        for day in self.days_enabled.keys():
            frame = ttk.Frame(root)
            frame.pack(pady=5)

            # Checkbox for enabling/disabling the day
            var = tk.BooleanVar(value=self.days_enabled[day])
            chk = ttk.Checkbutton(frame, text=day, variable=var, onvalue=True, offvalue=False)
            chk.pack(side=tk.LEFT, padx=5)
            self.day_vars[day] = var

            # Time entry for type-in
            type_in_label = ttk.Label(frame, text="Type-In:")
            type_in_label.pack(side=tk.LEFT, padx=5)
            type_in_entry = ttk.Entry(frame, width=8, state="readonly")
            type_in_entry.pack(side=tk.LEFT, padx=5)
            self.time_entries[f"{day}_in"] = type_in_entry

            # Time entry for type-out
            type_out_label = ttk.Label(frame, text="Type-Out:")
            type_out_label.pack(side=tk.LEFT, padx=5)
            type_out_entry = ttk.Entry(frame, width=8, state="readonly")
            type_out_entry.pack(side=tk.LEFT, padx=5)
            self.time_entries[f"{day}_out"] = type_out_entry

        # Teams path input (unchanged)
        self.teams_path = r"C:\Program Files\WindowsApps\MSTeams_25060.205.3499.6849_x64__8wekyb3d8bbwe\ms-teams.exe"
        self.image_path = r'D:\CODES\Python\Python-Projects\AutoClocker\assets\chatimage.png'

        # Load saved times
        self.load_times()

        # Schedule jobs
        self.schedule_jobs()

        # Ensure the app runs in the background
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_config(self):
        """Load configuration from the JSON file."""
        try:
            with open(self.config_file, "r") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            # Default configuration
            self.config = {
                "threshold": 15,
                "running": False,
                "days_enabled": {
                    "Mon": True,
                    "Tue": True,
                    "Wed": True,
                    "Thu": True,
                    "Fri": True
                }
            }

    def save_config(self):
        """Save configuration to the JSON file."""
        self.config["threshold"] = self.threshold_var.get()
        self.config["running"] = self.running
        self.config["days_enabled"] = {day: var.get() for day, var in self.day_vars.items()}

        with open(self.config_file, "w") as f:
            json.dump(self.config, f)

    def toggle(self):
        self.running = not self.running
        self.toggle_button.config(text="Stop" if self.running else "Start")
        self.save_config()  # Save the running state
        if self.running:
            self.run_scheduler()

    def toggle_edit_mode(self):
        """Toggle the edit mode for time entries."""
        self.edit_mode = not self.edit_mode
        self.edit_button.config(text="Save Times" if self.edit_mode else "Edit Times")

        for day in self.days_enabled.keys():
            self.time_entries[f"{day}_in"].config(state="normal" if self.edit_mode else "readonly")
            self.time_entries[f"{day}_out"].config(state="normal" if self.edit_mode else "readonly")

        if not self.edit_mode:
            # Save times when exiting edit mode
            self.save_times()
            self.schedule_jobs()  # Reschedule jobs with updated times

    def save_times(self):
        """Save the type-in and type-out times to a file."""
        times = {}
        for day in self.days_enabled.keys():
            times[f"{day}_in"] = self.time_entries[f"{day}_in"].get()
            times[f"{day}_out"] = self.time_entries[f"{day}_out"].get()

        with open(r"D:\CODES\Python\Python-Projects\AutoClocker\config\times.json", "w") as f:
            json.dump(times, f)

    def load_times(self):
        """Load the type-in and type-out times from a file."""
        try:
            # Load times from the JSON file
            with open(r"D:\CODES\Python\Python-Projects\AutoClocker\config\times.json", "r") as f:
                times = json.load(f)
            
            # Fetch times for each day and insert into the entry widgets
            for day in self.days_enabled.keys():
                # Type-In time
                type_in_time = times.get(f"{day}_in", "09:30")  # Default to "09:30" if key not found
                self.time_entries[f"{day}_in"].config(state="normal")  # Temporarily enable editing
                self.time_entries[f"{day}_in"].delete(0, tk.END)  # Clear the entry
                self.time_entries[f"{day}_in"].insert(0, type_in_time)  # Insert the time
                self.time_entries[f"{day}_in"].config(state="readonly")  # Revert to readonly

                # Type-Out time
                type_out_time = times.get(f"{day}_out", "18:30")  # Default to "18:30" if key not found
                self.time_entries[f"{day}_out"].config(state="normal")  # Temporarily enable editing
                self.time_entries[f"{day}_out"].delete(0, tk.END)  # Clear the entry
                self.time_entries[f"{day}_out"].insert(0, type_out_time)  # Insert the time
                self.time_entries[f"{day}_out"].config(state="readonly")  # Revert to readonly

        except FileNotFoundError:
            # If the file doesn't exist, use default times
            for day in self.days_enabled.keys():
                # Type-In time (default)
                self.time_entries[f"{day}_in"].config(state="normal")  # Temporarily enable editing
                self.time_entries[f"{day}_in"].delete(0, tk.END)  # Clear the entry
                self.time_entries[f"{day}_in"].insert(0, "09:30")  # Insert default time
                self.time_entries[f"{day}_in"].config(state="readonly")  # Revert to readonly

                # Type-Out time (default)
                self.time_entries[f"{day}_out"].config(state="normal")  # Temporarily enable editing
                self.time_entries[f"{day}_out"].delete(0, tk.END)  # Clear the entry
                self.time_entries[f"{day}_out"].insert(0, "18:30")  # Insert default time
                self.time_entries[f"{day}_out"].config(state="readonly")  # Revert to readonly

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

        # Map day abbreviations to full names
        day_map = {
            "Mon": "monday",
            "Tue": "tuesday",
            "Wed": "wednesday",
            "Thu": "thursday",
            "Fri": "friday"
        }

        # Schedule tasks with randomness for each day
        for day in self.days_enabled.keys():
            if not self.day_vars[day].get():  # Skip if the day is disabled
                continue

            # Get type-in and type-out times from the GUI
            type_in_time = self.time_entries[f"{day}_in"].get()
            type_out_time = self.time_entries[f"{day}_out"].get()

            # Get the full day name
            full_day = day_map[day]

            # Schedule type-in and type-out tasks
            self.schedule_with_randomness(getattr(schedule.every(), full_day), type_in_time, self.type_in)
            self.schedule_with_randomness(getattr(schedule.every(), full_day), type_out_time, self.type_out)

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
                time.sleep(3)  # Wait for Teams to open
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
        if not self.running or not self.day_vars[datetime.now().strftime("%a")].get():
            return
        if self.open_teams():
            self.navigate_to_chat("SpiralBot")
            pyautogui.write("In")
            pyautogui.press("enter")

    def type_out(self):
        if not self.running or not self.day_vars[datetime.now().strftime("%a")].get():
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

    def on_close(self):
        """Handle the window close event."""
        self.save_config()  # Save configuration before closing
        if self.running:
            self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Auto Clocker")
    app = TeamsAutoTyper(root)
    # App Icon
    img = Image.open(r"D:\CODES\Python\Python-Projects\AutoClocker\assets\type-icon.png")
    photo = ImageTk.PhotoImage(img)
    root.iconphoto(True, photo)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("AutoClockerID")
    # Run App
    root.mainloop()