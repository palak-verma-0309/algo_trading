import schedule
import time
import subprocess
from datetime import datetime

def job():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running main.py...")
    subprocess.run(["python", "main.py"])
schedule.every().day.at("09:15").do(job)

print("Scheduler started. Waiting for job...")
while True:
    schedule.run_pending()
    time.sleep(30)
