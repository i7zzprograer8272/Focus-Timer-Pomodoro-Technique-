"""
User interface handling for the Pomodoro timer
"""

class UserInterface:
    """Handles all user interface interactions"""
    
    def display_main_menu(self):
        """Display the main menu and get user choice"""
        print("\n" + "=" * 30)
        print(" MAIN MENU")
        print("=" * 30)
        print("1.  Start Pomodoro Session")
        print("2.  Configure Settings")
        print("3.  View Session History")
        print("4.  Exit")
        print("-" * 30)
        
        return input("Enter your choice (1-4): ").strip()
    
    def show_session_start(self, work_duration):
        """Display session start information"""
        print("STARTING POMODORO SESSION!")
        print(f"Work duration: {work_duration} minutes")
        print("Short break: 5 minutes")
        print("Long break: 15 minutes")
        print("\nPress Ctrl+C to stop the session")
        print("-" * 40)
        
    def show_progress_bar(self, current, total, length=30):
        """Display a progress bar"""
        progress = current / total
        bars = int(progress * length)
        spaces = length - bars
        
        bar = "_" * bars + "_" * spaces
        percentage = progress * 100
        
        print(f"\rProgress: [{bar}] {percentage:.1f}%", end="", flush=True)
        
    def display_config_menu(self):
        """Display configuration menu"""
        print("\n  CONFIGURATION MENU")
        print("1. Set Work Duration")
        print("2. Set Short Break Duration")
        print("3. Set Long Break Duration")
        print("4. Back to Main Menu")
        
        return input("Enter your choice (1-4): ").strip()
    
    def get_duration_input(self, session_type, current_value):
        """Get duration input from user"""
        while True:
            try:
                value = int(input(f"Enter {session_type} duration in minutes (current: {current_value}): "))
                if 1 <= value <= 60:
                    return value
                else:
                    print(" Please enter a value between 1 and 60 minutes.")
            except ValueError:
                print(" Please enter a valid number")

