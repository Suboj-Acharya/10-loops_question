# Exponential backoff that doubles the wait time between retries but stop after 5 retries
import time
wait_time = 1
retries=5
attempts=1
while (attempts <= retries):
    print(f"Attempt {attempts} Wait_Time {wait_time}")
    time.sleep(wait_time)
    attempts=attempts+1
    wait_time *=2
    
                
        