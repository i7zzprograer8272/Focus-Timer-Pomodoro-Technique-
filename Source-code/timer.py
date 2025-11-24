### 2. timer.py
"""
Timer module for Pomodoro session management
"""
import time
import os
import sys

class PomodoroTimer:
    """Handles timer functionality for Pomodoro sessions"""
    
    def __init__(self):
        self.is_running = False
        
    def start_pomodoro_session(self, work_duration, short_break, long_break, session_manager):
        """Start a complete Pomodoro session cycle"""
        self.is_running = True
        
        try:
            while self.is_running and session_manager.session_count < 4:
                # Work session
                print(f"\n Starting Work Session #{session_manager.session_count + 1}")
                self.countdown(work_duration, "WORK")
                
                if not self.is_running:
                    break
                    
                session_manager.complete_session()
                self.play_notification_sound()
                
                # Break session
                if session_manager.session_count % 4 == 0:
                    print(f"\n Time for Long Break!")
                    self.countdown(long_break, "LONG BREAK")
                else:
                    print(f"\n Time for Short Break!")
                    self.countdown(short_break, "SHORT BREAK")
                    
                if self.is_running:
                    self.play_notification_sound()
                    
        except KeyboardInterrupt:
            print("\n\n Session interrupted by user")
            self.is_running = False
            
    def countdown(self, minutes, session_type):
        """Countdown timer for a session"""
        total_seconds = minutes * 60
        
        while total_seconds > 0 and self.is_running:
            # Calculate minutes and seconds
            mins, secs = divmod(total_seconds, 60)
            
            # Format time display
            time_format = f"{session_type}: {mins:02d}:{secs:02d}"
            
            # Clear line and display time
            sys.stdout.write('\r' + time_format + ' ' * 10)
            sys.stdout.flush()
            
            # Wait for 1 second
            time.sleep(1)
            total_seconds -= 1
            
        if self.is_running:
            sys.stdout.write('\r' + ' ' * 50 + '\r')
            sys.stdout.flush()
            
    def play_notification_sound(self):
        """Play notification sound (beep)"""
        try:
            # Windows beep
            import winsound
            winsound.Beep(1000, 800)  # Frequency 1000Hz, duration 800ms
        except:
            # Unix beep alternative
            print("\a")  # ASCII bell character
            
    def stop_timer(self):
        """Stop the timer"""
        self.is_running = False
