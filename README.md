# Focus-Timer-Pomodoro-Technique-

## Project Title

Focus Timer - Pomodoro Technique

## Overview of the project

A Python-based implementation of the Pomodoro Technique, a time management method that uses a timer to break work into focused intervals (typically 25 minutes) separated by short breaks. This application helps students and professionals maintain concentration and prevent burnout through structured work-rest cycles.

## Features

### **Timer Functionality**
- **Customizable Durations**: Adjustable work and break periods
- **Automatic Session Cycling**: Seamless transitions between work and break sessions
- **Progress Visualization**: Real-time progress bar and countdown display
- **Session Tracking**: Automatic recording of completed Pomodoro sessions

### **Customization Options**
- Set preferred work duration (1-60 minutes)
- Configure short break length (1-60 minutes)
- Adjust long break duration (1-60 minutes)
- Persistent settings across sessions

### **Progress Monitoring**
- Real-time progress bar during sessions
- Session history tracking
- Visual indicators for session types
- Overall productivity statistics

### **User Experience**
- Audio notifications for session transitions
- Clean command-line interface
- Intuitive menu navigation
- Cross-platform compatibility

## Technologies & Tools Used

### Programming Language
- **Python 3.6+** - Core programming language

### Standard Library Modules
- `time` - Timer and countdown functionality
- `threading` - Concurrent execution (if needed for future enhancements)
- `json` - Configuration and data storage
- `os` - File system operations
- `sys` - System-specific parameters and functions
- `datetime` - Timestamp handling and session tracking

### Platform-Specific Features
- `winsound` (Windows) - Audio notifications
- ASCII bell character (Unix/macOS) - Fallback audio alerts

### Development Tools
- **Git** - Version control
- **VS Code/PyCharm** - Code editor
- **Command Line/Terminal** - Application execution

## Steps to install and run the project

### Prerequisites
- Python 3.6 or higher installed on your system
- Basic command-line knowledge

### Step-by-Step Installation

1. **Download the Project**
   ```bash
   # Clone or download all project files to a directory
   # Ensure these files are in the same folder:
   # - main.py
   # - timer.py
   # - session_manager.py
   # - ui.py
   # - config.py
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # Should show Python 3.6 or higher
   ```

3. **Run the Application**
   ```bash
   python main.py
   ```

### File Structure
```
pomodoro_timer/
├── main.py /             # Main application entry point
├── timer.py            # Timer control and countdown logic
├── session_manager.py  # Session tracking and history management
├── ui.py              # User interface and menu handling
├── config.py          # Configuration settings management
├── pomodoro_config.json    # Auto-generated settings file
├── pomodoro_history.json   # Auto-generated session history
├── README.md          # Project documentation
└── statement.md       # Problem statement and scope
```

## Running the Application

### Starting the Timer
1. Open terminal/command prompt in the project directory
2. Run: `python main.py`
3. Use the main menu to navigate features

### Main Menu Options
```
MAIN MENU
==============================
1. Start Pomodoro Session
2. Configure Settings
3. View Session History
4. Exit
```

### Default Session Cycle
- **Work Session**: 25 minutes
- **Short Break**: 5 minutes
- **Long Break**: 15 minutes (after 4 work sessions)
- **Cycle**: Work → Short Break → Work → Short Break → Work → Short Break → Work → Long Break

## Instructions for Testing

### Functional Testing

1. **Timer Accuracy Test**
   ```bash
   # Set work duration to 1 minute for quick testing
   # Start session and verify countdown accuracy
   # Check session transition timing
   ```

2. **Session Cycle Test**
   - Start Pomodoro session
   - Verify automatic work-to-break transitions
   - Confirm long break after 4 sessions
   - Check session counter increments correctly

3. **Configuration Test**
   - Change work duration to 30 minutes
   - Modify break durations
   - Restart application to verify persistence

4. **History Tracking Test**
   - Complete multiple sessions
   - View session history
   - Verify timestamps and session counts

5. **Error Handling Test**
   - Enter invalid menu choices
   - Test boundary values in configuration
   - Interrupt sessions with Ctrl+C

### Test Commands
```bash
# Quick test with shorter durations
# Modify config to:
# Work: 1 minute, Short Break: 1 minute, Long Break: 2 minutes
# Then run multiple cycles to test functionality
```
