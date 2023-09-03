# import logging

from notion_client import Client

from notion_automator.consts import NOTION_TOKEN


# notion_client = Client(auth=NOTION_TOKEN, log_level=logging.DEBUG)
notion_client = Client(auth=NOTION_TOKEN)
