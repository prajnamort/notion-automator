#!/usr/bin/env python3
import time

from notion_automator.tasks import update_tasks


def main():
    while True:
        update_tasks()
        time.sleep(60 * 5)


if __name__ == '__main__':
    main()
