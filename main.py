#!/usr/bin/env python3

from notion_automator.consts import (
    TASKS_DATABASE_ID, TasksProp
)
from notion_automator.client import notion_client


def update_tasks():
    resp = notion_client.databases.retrieve(database_id=TASKS_DATABASE_ID)
    property_ids = {}
    for prop in TasksProp.ALL:
        prop_id = resp['properties'][prop]['id']
        property_ids[prop] = prop_id

    resp = notion_client.databases.query(
        database_id=TASKS_DATABASE_ID,
        filter={
            "property": "State",
            "rich_text": {
                "starts_with": "🔄",
            },
        },
        filter_properties=[
            property_ids[TasksProp.TASK],
            property_ids[TasksProp.DUE],
            property_ids[TasksProp.NEXT_DUE],
            property_ids[TasksProp.DONE],
        ],
    )
    if not resp['results']:
        return

    for task in resp['results']:
        print('-------------------------------------------------------------')
        print('Task:', task['properties'][TasksProp.TASK]['title'][0]['text']['content'])
        print('Due:', task['properties'][TasksProp.DUE]['date'])
        print('Next Due:', task['properties'][TasksProp.NEXT_DUE]['formula']['date'])

        assert task['properties'][TasksProp.DONE]['checkbox'] is True

        task = notion_client.pages.update(
            page_id=task['id'],
            properties={
                TasksProp.DUE: {
                    'date': task['properties'][TasksProp.NEXT_DUE]['formula']['date'],
                },
                TasksProp.DONE: {
                    'checkbox': False,
                }
            }
        )

        print('-->')
        print('Due:', task['properties'][TasksProp.DUE]['date'])
        print('Next Due:', task['properties'][TasksProp.NEXT_DUE]['formula']['date'])


def main():
    update_tasks()


if __name__ == '__main__':
    main()
