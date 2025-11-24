# main entry point for the pomodoro focus app

from timer import PomodoroTimer
from session_manager import SessionManager
from ui import UserInterface
from config import Config

def main():
    # main application function
    print("Focus Timer, Pomodoro Technique application")
    print()
    
    # initialization of components
    config = Config()
    session_manager = SessionManager()
    ui = UserInterface()
    timer = PomodoroTimer()
    
    while True:
        # displaying main menu items
        choice = ui.display_main_menu()
        
        if choice == "1":
            # starting pomodoro session
            work_duration = config.get_work_duration()
            short_break = config.get_short_break()
            long_break = config.get_long_break()
            
            ui.show_session_start(work_duration)
            timer.start_pomodoro_session(
                work_duration, 
                short_break, 
                long_break,
                session_manager
            )
            
        elif choice == "2":
            # setting configuration
            config.configure_settings()
            
        elif choice == "3":
            # for viewing session history
            session_manager.display_history()
            
        elif choice == "4":
            # for exiting application
            print("\nYour session has ended, see you later.")
            break
            
        else:
            print("Wrong choice, Please enter your choice again")

if __name__ == "__main__":
    main()

