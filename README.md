# 📚 Study Countdown Timer

A **minimalistic study countdown timer** designed to boost productivity while allowing you to take quick notes. This tool ensures you stay focused without distractions, automatically resuming your session after system restarts.

---

## ✨ Features
- **Simple and Minimalistic**: A transparent, always-on-top timer.
- **Task Notes**: Jot down tasks directly within the app and have them saved automatically.
- **Resume Where You Left Off**: The timer pauses on shutdown and resumes from the same point when the system restarts.
- **Always Accessible**: The window cannot be closed and can be dragged anywhere on the screen.

---

## 🛠️ How to Set It Up

# Countdown Timer Setup

This guide walks you through the steps to create and run a transparent countdown timer with a notes feature using Python. The timer will run without showing a command prompt window and without requiring administrator privileges.

## Requirements

- Python 3.11 installed on your system
- `tkinter` for GUI (usually included by default with Python installations)
- Your Python script file: `countdown_timer.py`

## File Locations

- **Python Executable**: `C:\Program Files\Python311\pythonw.exe`
- **Python Script**: `C:\Users\sanchit\Desktop\countdown_timer.py`
- **Save/Notes Files**: `timer_state.json` and `notes.json` should be created automatically by the script in the same directory as `countdown_timer.py`.

## Steps to Set Up the Countdown Timer

### 1. Create the Python Script Shortcut

1. **Create a Shortcut** on your desktop:
   - Right-click on your desktop and select **New > Shortcut**.
   - In the **location** field, enter the following command:

     ```
     "C:\Program Files\Python311\pythonw.exe" "C:\Users\sanchit\Desktop\countdown_timer.py"
     ```

   - Click **Next**.
   - Name the shortcut (e.g., "Countdown Timer").
   - Click **Finish**.

2. **Shortcut Properties**:
   - Right-click the shortcut and select **Properties**.
   - In the **Target** field, ensure the command is exactly:

     ```
     "C:\Program Files\Python311\pythonw.exe" "C:\Users\sanchit\Desktop\countdown_timer.py"
     ```

   - In the **Start in** field, enter:

     ```
     C:\Users\sanchit\Desktop
     ```

   - Click **Apply** and then **OK**.

### 2. Adjust Permissions for the Script

1. **Right-click** on `countdown_timer.py` (located on your desktop) and select **Properties**.
2. Go to the **Security** tab.
   - Make sure your user account has **full control** permissions.
   - If not, click **Edit** and grant the required permissions.
3. Click **Apply** and **OK**.

### 3. Avoid Requiring Administrator Rights

1. **Right-click** on the newly created shortcut.
2. Select **Properties**.
3. Click the **Advanced** button.
   - Make sure **"Run as administrator"** is **unchecked**.
   - Click **OK**, then **Apply**, and **OK**.

4. **Compatibility** (if needed):
   - Go to the **Compatibility** tab.
   - Ensure **"Run this program as an administrator"** is **unchecked**.
   - Click **Apply** and **OK**.

### 4. Create a Task Scheduler Task (Alternative Method)

If you still face issues running the shortcut without admin rights, use Task Scheduler to automate the script launch:

1. **Open Task Scheduler**:
   - Press `Win + R`, type `taskschd.msc`, and press Enter.
   
2. **Create a New Task**:
   - Click **Action > Create Basic Task**.
   - Name the task (e.g., "Countdown Timer").
   - Click **Next**.

3. **Set the Trigger**:
   - Choose **"At log on"** or any trigger you prefer.
   - Click **Next**.

4. **Set the Action**:
   - Choose **Start a program**.
   - In the **Program/script** field, enter the path to `pythonw.exe`:

     ```
     C:\Program Files\Python311\pythonw.exe
     ```

   - In the **Add arguments** field, enter the path to your Python script:

     ```
     "C:\Users\sanchit\Desktop\countdown_timer.py"
     ```

   - Click **Next** and **Finish**.

5. **General Tab Settings**:
   - In the task you just created, go to the **General** tab.
   - Ensure **"Run only when user is logged on"** is selected.
   - Uncheck **"Run with highest privileges"**.
   - Save the task.

6. **Test the Task**:
   - Right-click the task and select **Run**. Check if the timer runs without requiring admin rights.

### 5. Run the Timer

1. **Double-click** the shortcut on your desktop to run the countdown timer.
2. If you set up Task Scheduler, the timer should also start automatically based on the trigger you defined (e.g., at user logon).

## Additional Information

- **Notes and Timer Save Files**: The script will create `timer_state.json` and `notes.json` in the same directory as `countdown_timer.py` to manage the timer state and store your notes.
- **Transparency and Positioning**: The timer window is designed to be transparent and draggable on your desktop.
- **Resetting Permissions**: If you move the script to another directory, you might need to update permissions or recreate the shortcut with the new path.

## Troubleshooting

- If the shortcut does not run without administrator privileges, double-check the **Security** and **Compatibility** settings.
- Use Task Scheduler if a shortcut alone does not suffice for your setup.
- Ensure Python and the script paths are correctly specified in the shortcut or Task Scheduler.



