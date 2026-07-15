import time
import os
import sys
from app import get_uploads_playlist


def my_task():
    print("Doing the actual work...")
    get_uploads_playlist()


def main():
    my_task()
    print("Sleeping for 15 minutes before restarting...")
    time.sleep(900)

    # Restart the script as a fresh process
    os.execv(sys.executable, [sys.executable] + sys.argv)


if __name__ == "__main__":
    main()
