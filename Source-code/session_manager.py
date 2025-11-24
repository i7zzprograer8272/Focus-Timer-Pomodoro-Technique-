### 3. session_manager.py
"""
Session management for tracking Pomodoro sessions
"""
import datetime
import json
import os

class SessionManager:
    """Manages Pomodoro session tracking and history"""
    
    def __init__(self):
        self.session_count = 0
        self.session_history = []
        self.history_file = "pomodoro_history.json"
        self.load_history()
        
    def complete_session(self):
        """Record a completed work session"""
        self.session_count += 1
        session_data = {
            "session_number": self.session_count,
            "timestamp": datetime.datetime.now().isoformat(),
            "type": "work",
            "duration": 25  # Default work duration
        }
        self.session_history.append(session_data)
        self.save_history()
        
        print(f" Work Session #{self.session_count} completed!")
        
    def reset_sessions(self):
        """Reset session counter"""
        self.session_count = 0
        print(" Session counter reset!")
        
    def save_history(self):
        """Save session history to file"""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.session_history, f, indent=2)
        except Exception as e:
            print(f" Could not save history: {e}")
            
    def load_history(self):
        """Load session history from file"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    self.session_history = json.load(f)
                # Set session count from history
                if self.session_history:
                    self.session_count = self.session_history[-1]["session_number"]
        except Exception as e:
            print(f" Could not load history: {e}")
            self.session_history = []
            
    def display_history(self):
        """Display session history"""
        print("\n Session History:")
        print("-" * 40)
        
        if not self.session_history:
            print("No sessions recorded yet.")
            return
            
        for session in self.session_history[-10:]:  # Show last 10 sessions
            timestamp = datetime.datetime.fromisoformat(session["timestamp"])
            formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Session #{session['session_number']} - {formatted_time}")
            
        print(f"\nTotal sessions completed: {len(self.session_history)}")
        
    def get_total_sessions(self):
        """Get total number of sessions completed"""
        return len(self.session_history)
