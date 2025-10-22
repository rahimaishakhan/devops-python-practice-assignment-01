import psutil # External library required for accessing system metrics (CPU usage). Must be installed with 'pip install psutil'.
import time   # Default Python library used to pause the loop execution.
import sys    # Default Python library for system-level operations (used for clean exit).

# Best Practice: Use CAPITALIZED variables for configuration values that won't change (constants).
CPU_THRESHOLD_PERCENT = 80 # If CPU usage goes above this percentage, an alert is triggered.
MONITOR_INTERVAL_SECONDS = 3 # How often the script will check the CPU (every 3 seconds).

# ------------------------- FUNCTION DEFINITION ----------------------------------
def monitor_cpu_health():
    """Continuously monitors CPU usage and alerts if a threshold is breached."""
    print(f"Monitoring CPU usage... (Alert threshold: {CPU_THRESHOLD_PERCENT}%)")
    
    # We use a 'try...except' block to handle user interruption (like pressing Ctrl+C) gracefully.
    try:
        # 'while True:' creates an INFINITE LOOP, which runs forever until something stops it (like Ctrl+C).
        while True:
            # psutil.cpu_percent() is a method from the external library that gets the current CPU usage.
            cpu_usage = psutil.cpu_percent(interval=None) 
            
            # This is our monitoring check:
            if cpu_usage > CPU_THRESHOLD_PERCENT:
                # Log a critical alert message using an F-string for easy variable insertion.
                print(f"🚨 ALERT! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                # Log a normal status message.
                print(f"Current CPU usage: {cpu_usage}% (OK)")
            
            # 'time.sleep()' is the DEFAULT PYTHON FUNCTION that pauses the program for the specified number of seconds.
            time.sleep(MONITOR_INTERVAL_SECONDS)
            
    except KeyboardInterrupt:
        # This 'except' block specifically catches the interrupt signal (Ctrl+C).
        print("\nMonitoring interrupted by user. Exiting gracefully.")
        sys.exit(0) # Exits the script with a success code (0).
    except Exception as e:
        # This catches any other unexpected system errors.
        print(f"\n❌ An unexpected error occurred during monitoring: {e}")
        sys.exit(1) # Exits the script with an error code (1).

# ------------------------- SCRIPT EXECUTION ----------------------------------
if __name__ == "__main__":
    monitor_cpu_health()

