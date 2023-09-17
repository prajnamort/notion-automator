#!/usr/bin/env python3
import time

from notion_automator.tasks import update_tasks


def main():
    while True:
        try:
            update_tasks()
        except Exception as e:
            print(e)
            time.sleep(60 * 60)
            continue

        time.sleep(60 * 5)


if __name__ == '__main__':
    main()
