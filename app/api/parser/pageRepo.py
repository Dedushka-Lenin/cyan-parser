import requests
from bs4 import BeautifulSoup

from fastapi import HTTPException

from app.db.recordManager import RecordManager

class PageRepo(RecordManager):
    def __init__(self):
        super().__init__('page')