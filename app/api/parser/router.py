from fastapi import APIRouter, HTTPException

from app.api.parser.pageRepo import PageRepo
from app.api.parser.parserRepo import ParserRepo


class ParserRouter():
   def __init__(self):

      self.pageRepo = PageRepo()
      self.parserRepo = ParserRepo()

      self.router = APIRouter()

      self.router.post("/parse", status_code=200)(self.parse)

   async def parse(self):
      pass