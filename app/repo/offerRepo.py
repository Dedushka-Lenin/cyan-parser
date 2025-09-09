from app.db.recordManager import RecordManager

class OfferRepo(RecordManager):
    def __init__(self):
        super().__init__('offers')