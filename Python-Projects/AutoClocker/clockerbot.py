# import tkinter as tk
# from tkinter import ttk
# import threading
# import time
# import schedule
# import pyautogui
# from datetime import datetime
# import psutil
# import subprocess
# import os
# import random

# class TeamsAutoTyper:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Teams Auto Typer")
#         self.root.geometry("300x200")

#         self.running = False
#         self.days_disabled = {
#             "Mon": False,
#             "Tue": False,
#             "Wed": False,
#             "Thu": False,
#             "Fri": False
#         }

#         self.toggle_button = ttk.Button(root, text="Start", command=self.toggle)
#         self.toggle_button.pack(pady=20)

#         self.day_vars = {}
#         for day in self.days_disabled.keys():
#             var = tk.BooleanVar()
#             chk = ttk.Checkbutton(root, text=day, variable=var, onvalue=True, offvalue=False)
#             chk.pack()
#             self.day_vars[day] = var

#         self.schedule_jobs()

#     def toggle(self):
#         self.running = not self.running
#         self.toggle_button.config(text="Stop" if self.running else "Start")
#         if self.running:
#             self.run_scheduler()

#     def add_randomness(self, base_time, threshold_minutes=15):
#         """
#         Add randomness to a base time within a specified threshold.
#         :param base_time: The base time in "HH:MM" format.
#         :param threshold_minutes: The maximum number of minutes to add or subtract.
#         :return: A new time string with randomness applied.
#         """
#         hours, minutes = map(int, base_time.split(':'))
#         total_minutes = hours * 60 + minutes
#         offset = random.randint(-threshold_minutes, threshold_minutes)
#         total_minutes += offset
#         total_minutes %= 1440  # Handle wrapping around midnight
#         new_hours = total_minutes // 60
#         new_minutes = total_minutes % 60
#         return f"{new_hours:02d}:{new_minutes:02d}"

#     def schedule_with_randomness(self, day, base_time, task, threshold_minutes=15):
#             """
#             Schedule a task with randomness applied to the base time.
#             :param day: The day of the week (e.g., schedule.every().monday).
#             :param base_time: The base time in "HH:MM" format.
#             :param task: The function to execute.
#             :param threshold_minutes: The maximum number of minutes to add or subtract.
#             """
#             random_time = self.add_randomness(base_time, threshold_minutes)
#             day.at(random_time).do(task)

#     def schedule_jobs(self):
#         self.schedule_with_randomness(schedule.every().monday, "09:30", self.type_in)
#         self.schedule_with_randomness(schedule.every().monday, "18:30", self.type_out)
#         self.schedule_with_randomness(schedule.every().tuesday, "09:30", self.type_in)
#         self.schedule_with_randomness(schedule.every().tuesday, "18:30", self.type_out)
#         self.schedule_with_randomness(schedule.every().wednesday, "08:30", self.type_in)
#         self.schedule_with_randomness(schedule.every().wednesday, "17:30", self.type_out)
#         self.schedule_with_randomness(schedule.every().thursday, "08:30", self.type_in)
#         self.schedule_with_randomness(schedule.every().thursday, "17:30", self.type_out)
#         self.schedule_with_randomness(schedule.every().friday, "08:30", self.type_in)
#         self.schedule_with_randomness(schedule.every().friday, "17:30", self.type_out)

#     def is_teams_running(self):
#         """Check if Microsoft Teams is running."""
#         for proc in psutil.process_iter(['name']):
#             if proc.info['name'] == 'Teams.exe':
#                 return True
#         return False

#     def open_teams(self):
#         """Open Microsoft Teams if it's not running."""
#         if not self.is_teams_running():
#             teams_path = r"C:\Program Files\WindowsApps\MSTeams_25060.205.3499.6849_x64__8wekyb3d8bbwe\ms-teams.exe"
#             if os.path.exists(teams_path):
#                 subprocess.Popen([teams_path, '--processStart', 'Teams.exe'])
#                 time.sleep(10)  # Wait for Teams to open
#             else:
#                 print("Microsoft Teams not found. Please ensure it is installed.")
#                 return False
#         return True

#     # def navigate_to_chat(self, chat_name):
#     #     """Navigate to the chat window named 'SpiralBot'."""
#     #     # Simulate pressing Ctrl+E to focus on the search bar
#     #     pyautogui.hotkey('ctrl', 'e')
#     #     time.sleep(1)
#     #     # Type the chat name
#     #     pyautogui.write(chat_name)
#     #     time.sleep(1)
#     #     # Press Enter to open the chat
#     #     pyautogui.press('enter')
#     #     time.sleep(2)  # Wait for the chat to open

#     def navigate_to_chat(self, chat_name):
#         """Navigate to the chat window named 'SpiralBot'."""
#         # Simulate pressing Ctrl+E to focus on the search bar
#         pyautogui.hotkey('ctrl', 'e')
#         time.sleep(1)
        

#         # Clear text field
#         pyautogui.hotkey("ctrl", "a")  # Select all text
#         pyautogui.press("backspace")   # Clear the field

#         # Type the chat name
#         pyautogui.write(chat_name)
#         time.sleep(1)  # Wait for search results to load

#         # Locate the chat in the search results and click on it
#         try:
#             # Use pyautogui to locate the chat name on the screen
#             chat_position = pyautogui.locateOnScreen(r'D:\CODES\Python\Python-Projects\AutoClocker\chat-image.png', confidence=0.8)
#             if chat_position:
#                 # Calculate the center of the located image
#                 chat_center = pyautogui.center(chat_position)
#                 # Move the mouse to the center and click
#                 pyautogui.moveTo(chat_center)
#                 pyautogui.click()
#                 time.sleep(1)  # Wait for the chat to open
#                 pyautogui.hotkey("ctrl", "r")  # Focus on chat box

#             else:
#                 print(f"Chat '{chat_name}' not found in search results.")
#         except Exception as e:
#             print(f"Error locating chat: {e}")

#     def type_in(self):
#         if not self.running or self.days_disabled[datetime.now().strftime("%a")]:
#             return
#         if self.open_teams():
#             self.navigate_to_chat("SpiralBot")
#             pyautogui.write("Hi")
#             pyautogui.press("enter")

#     def type_out(self):
#         if not self.running or self.days_disabled[datetime.now().strftime("%a")]:
#             return
#         if self.open_teams():
#             self.navigate_to_chat("SpiralBot")
#             pyautogui.write("Out")
#             pyautogui.press("enter")

#     def run_scheduler(self):
#         def scheduler_loop():
#             while self.running:
#                 schedule.run_pending()
#                 time.sleep(1)

#         threading.Thread(target=scheduler_loop, daemon=True).start()

#     def update_days_disabled(self):
#         for day, var in self.day_vars.items():
#             self.days_disabled[day] = var.get()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TeamsAutoTyper(root)
#     root.mainloop()

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
        self.root.geometry("400x300")

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

        # Days checkboxes
        self.day_vars = {}

        for day in self.days_disabled.keys():
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(root, text=day, variable=var, onvalue=True, offvalue=False)
            chk.pack()
            self.day_vars[day] = var

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
        # Schedule tasks with randomness
        self.schedule_with_randomness(schedule.every().monday, "09:30", self.type_in)
        self.schedule_with_randomness(schedule.every().monday, "18:30", self.type_out)
        self.schedule_with_randomness(schedule.every().tuesday, "09:30", self.type_in)
        self.schedule_with_randomness(schedule.every().tuesday, "18:30", self.type_out)
        self.schedule_with_randomness(schedule.every().wednesday, "08:30", self.type_in)
        self.schedule_with_randomness(schedule.every().wednesday, "17:30", self.type_out)
        self.schedule_with_randomness(schedule.every().thursday, "08:30", self.type_in)
        self.schedule_with_randomness(schedule.every().thursday, "17:30", self.type_out)
        self.schedule_with_randomness(schedule.every().friday, "08:30", self.type_in)
        self.schedule_with_randomness(schedule.every().friday, "17:30", self.type_out)

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