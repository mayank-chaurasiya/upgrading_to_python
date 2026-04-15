"""Exponential Backoff
Problem: Implement an exponential backoff strategy that doubles the wait time
between retries, starting from 1 second, but stops after 5 retries.
"""

import time

wait_time = 1
MAX_RETRIES = 5
attempts = 0

while attempts < MAX_RETRIES:
    print(f"Attempts : {attempts + 1}, Wait time {wait_time} seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
