import tkinter as tk
from datetime import datetime, timedelta
import json
import os

# Settings
TIMER_HOURS = 14  # 14-hour countdown
SAVE_FILE = "timer_state.json"  # File to store timer state
NOTES_DIR = r"C:\Users\sanchit\Desktop\daily does"  # Directory to store daily notes
TRANSPARENCY = 0.6  # 0 (fully transparent) to 1 (fully opaque)

# Ensure notes directory exists
os.makedirs(NOTES_DIR, exist_ok=True)

# Load or initialize the countdown timer
def load_timer():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as file:
                data = json.load(file)
                remaining_seconds = data["remaining_seconds"]
                last_save_time = datetime.fromisoformat(data["last_save_time"])
                return remaining_seconds, last_save_time
        except (json.JSONDecodeError, KeyError, ValueError):
            # If the file is corrupted or data is invalid, reset the timer
            reset_timer()
            return load_timer()
    else:
        reset_timer()
        return load_timer()

def save_timer(remaining_seconds):
    with open(SAVE_FILE, "w") as file:
        json.dump({
            "remaining_seconds": remaining_seconds,
            "last_save_time": datetime.now().isoformat()
        }, file)

def reset_timer():
    remaining_seconds = TIMER_HOURS * 3600  # Convert hours to seconds
    save_timer(remaining_seconds)

# Get today's note file based on the current date
def get_today_note_file():
    today_date = datetime.now().date().isoformat()  # Use date as 'YYYY-MM-DD'
    file_name = os.path.join(NOTES_DIR, f"notes_{today_date}.txt")
    return file_name

# Load notes from today's file
def load_notes():
    note_file = get_today_note_file()
    if os.path.exists(note_file):
        with open(note_file, "r") as file:
            return file.read()
    return ""

# Save notes to today's file (overwrite with current content)
def save_notes(content):
    note_file = get_today_note_file()
    with open(note_file, "w") as file:
        file.write(content)

# Create the Notes window
class NotesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Notes")
        self.geometry("200x200+220+10")  # Adjust size and position
        self.configure(bg="white")
        self.overrideredirect(True)  # Remove title bar
        self.attributes("-topmost", True)  # Always on top

        # Load notes
        self.notes = load_notes()

        # Notes display
        self.text_area = tk.Text(self, font=("Arial", 12), wrap="word", bg="white", fg="black")
        self.text_area.pack(expand=True, fill="both")
        self.text_area.insert(tk.END, self.notes)  # Load existing notes

        # Save button
        save_button = tk.Button(self, text="Save", command=self.save_notes, font=("Arial", 10))
        save_button.pack(pady=5)

    def save_notes(self):
        # Save notes from the text area to the file
        content = self.text_area.get("1.0", tk.END).strip()
        save_notes(content)  # Save the entire content

# Create the GUI for Countdown
class CountdownApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Countdown Timer")
        self.geometry("200x150+10+10")  # Adjust size and position
        self.overrideredirect(True)  # Remove title bar
        self.attributes("-topmost", True)  # Always on top
        self.attributes("-alpha", TRANSPARENCY)  # Set transparency
        self.configure(bg="white")
        
        self.label = tk.Label(self, font=("Arial", 20), bg="white", fg="black")
        self.label.pack(expand=True)

        # Notes button
        notes_button = tk.Button(self, text="Notes", command=self.open_notes, font=("Arial", 10))
        notes_button.pack(pady=5)
        
        # Close Notes button
        close_button = tk.Button(self, text="Close Notes", command=self.close_notes, font=("Arial", 10))
        close_button.pack(pady=5)

        # Load or reset timer
        self.remaining_seconds, self.last_save_time = load_timer()
        self.calculate_adjustment()  # Adjust based on any time that has passed

        # Initialize Notes Window
        self.notes_window = None

        # Make the window draggable
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.do_move)

        self.update_timer()

    def calculate_adjustment(self):
        now = datetime.now()
        time_passed = (now - self.last_save_time).total_seconds()
        self.remaining_seconds = max(self.remaining_seconds - time_passed, 0)
        save_timer(self.remaining_seconds)

    def update_timer(self):
        # Update the countdown
        if self.remaining_seconds > 0:
            self.label.config(text=str(timedelta(seconds=int(self.remaining_seconds))))
            self.remaining_seconds -= 1
            save_timer(self.remaining_seconds)
            # Update every second
            self.after(1000, self.update_timer)
        else:
            self.label.config(text="Time's Up!")

    def open_notes(self):
        # Open the Notes window if it's not already open
        if self.notes_window is None or not self.notes_window.winfo_exists():
            self.notes_window = NotesWindow(self)
    
    def close_notes(self):
        # Close the Notes window and save notes
        if self.notes_window is not None and self.notes_window.winfo_exists():
            self.notes_window.save_notes()
            self.notes_window.destroy()
            self.notes_window = None

    # Functions to make the window draggable
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

# Save the current state when closing
def on_close():
    save_timer(app.remaining_seconds)
    app.destroy()

# Run the application
if __name__ == "__main__":
    app = CountdownApp()
    app.protocol("WM_DELETE_WINDOW", on_close)  # Handle the window close event
    app.mainloop()
