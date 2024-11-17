import datetime
import time

def print_elapsed_time():
    start_time = datetime.datetime.now()

    while True:
        current_time = datetime.datetime.now()
        elapsed_time = current_time - start_time
        seconds_elapsed = elapsed_time.total_seconds()

        print(f"{int(seconds_elapsed)}s", end="\r", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    print_elapsed_time()
