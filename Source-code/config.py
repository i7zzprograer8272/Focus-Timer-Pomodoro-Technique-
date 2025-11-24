### 5. config.py

"""
Configuration management for Pomodoro timer settings
"""
import json
import os

class Config:
    """Manages application configuration settings"""
    
    def __init__(self):
        self.config_file = "pomodoro_config.json"
        self.default_config = {
            "work_duration": 25,
            "short_break": 5,
            "long_break": 15
        }
        self.current_config = self.load_config()
        
    def load_config(self):
        """Load configuration from file or create default"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            else:
                self.save_config(self.default_config)
                return self.default_config.copy()
        except Exception as e:
            print(f"Could not load config: {e}")
            return self.default_config.copy()
            
    def save_config(self, config=None):
        """Save configuration to file"""
        if config is None:
            config = self.current_config
            
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print(f"Could not save config: {e}")
            
    def get_work_duration(self):
        """Get work duration setting"""
        return self.current_config["work_duration"]
        
    def get_short_break(self):
        """Get short break duration"""
        return self.current_config["short_break"]
        
    def get_long_break(self):
        """Get long break duration"""
        return self.current_config["long_break"]
        
    def set_work_duration(self, duration):
        """Set work duration"""
        self.current_config["work_duration"] = duration
        self.save_config()
        print(f"Work duration set to {duration} minutes")
        
    def set_short_break(self, duration):
        """Set short break duration"""
        self.current_config["short_break"] = duration
        self.save_config()
        print(f"Short break set to {duration} minutes")
        
    def set_long_break(self, duration):
        """Set long break duration"""
        self.current_config["long_break"] = duration
        self.save_config()
        print(f"Long break set to {duration} minutes")
        
    def configure_settings(self):
        """Interactive configuration menu"""
        from ui import UserInterface
        ui = UserInterface()
        
        while True:
            choice = ui.display_config_menu()
            
            if choice == "1":
                current = self.get_work_duration()
                new_duration = ui.get_duration_input("work", current)
                self.set_work_duration(new_duration)
                
            elif choice == "2":
                current = self.get_short_break()
                new_duration = ui.get_duration_input("short break", current)
                self.set_short_break(new_duration)
                
            elif choice == "3":
                current = self.get_long_break()
                new_duration = ui.get_duration_input("long break", current)
                self.set_long_break(new_duration)
                
            elif choice == "4":
                break
                
            else:
                print("Invalid choice. Please try again.")
                
    def display_current_settings(self):
        """Display current configuration"""
        print("\n Current Settings:")
        print(f"  Work Duration: {self.get_work_duration()} minutes")
        print(f"  Short Break: {self.get_short_break()} minutes")
        print(f"  Long Break: {self.get_long_break()} minutes")
