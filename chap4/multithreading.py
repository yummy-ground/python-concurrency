import os
import time
import threading
from threading import Thread


def display_threads():
    print("=" * 10)

    print(f"- Current Process PID : {os.getpid()}")
    print(f"- Thread Count : {threading.active_count()}")
    print("[Active Threads]")
    for thread in threading.enumerate():
        print(thread)

    print("=" * 10)


def cpu_waster(i: int) -> None:
    thread = threading.current_thread()
    print(f"{thread} doing {i} work")
    time.sleep(3)


def main(thread_num: int) -> None:
    display_threads()

    print(f"> Starting {thread_num} CPU wasters")
    for i in range(thread_num):
        thread = Thread(target=cpu_waster(i))
        thread.start()

    display_threads()


if __name__ == '__main__':
    thread_num = 5
    main(thread_num)