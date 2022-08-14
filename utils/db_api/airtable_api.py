import os

from airtable.airtable import Airtable
from dotenv import load_dotenv

load_dotenv()

BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = os.getenv("TABLE_NAME")
API_KEY_AIRTABLE = os.getenv("API_KEY_AIRTABLE")

airtable_conn = Airtable(BASE_ID, TABLE_NAME, API_KEY_AIRTABLE)
