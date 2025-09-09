import itertools
import time
import sys
import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.repo.offerRepo import OfferRepo
from app.core.config import URL

from utils import get_info



offerRepo = OfferRepo()

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)


for num in itertools.count(1): 

    print(num)

    url = URL+f"&p={num}"

    try:
        driver.get(url)

        current_url = driver.current_url
        if current_url != url:
            break

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        if "404" in driver.title or "Not Found" in driver.page_source:
            break

    except WebDriverException:
        break

    offerList = soup.find_all(attrs={"data-testid": "offer-card"})

    for offer in offerList:
        offer_info = get_info(offer)
        print(offer_info)
        offerRepo.create(offer_info)

    time.sleep(1)

driver.quit()