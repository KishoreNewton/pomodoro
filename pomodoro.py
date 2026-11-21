import sys
import time

minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 25
print(f"Focus for {minutes} minutes.")
time.sleep(minutes * 60)
print("Time for a break.")
