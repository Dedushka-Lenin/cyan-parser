def cleaning(text):
    removal_list = [
        ' ',
        '\xa0',
        '₽',
        '/м²'
    ]

    for elm in removal_list:

        text = text.replace(elm, "")

    return text


def get_text(text):

    if text == []:
        return ''

    return text[0].get_text(strip=True)


def get_info(offer):

    title = offer.find_all(attrs={"data-mark": "OfferTitle"})
    price = offer.find_all(attrs={"data-mark": "MainPrice"})
    price_per_meter = offer.find_all(attrs={"data-mark": "PriceInfo"})
    description = offer.find_all(attrs={"data-name": "Description"})
    url = offer.find('a')

    if price == []:
        price = offer.find_all(attrs={"data-testid": "offer-discount-new-price"})


    title =  get_text(title)
    price =  int(cleaning(get_text(price)))
    price_per_meter =  int(cleaning(get_text(price_per_meter)))
    square = round(price/price_per_meter, 1)
    description =  get_text(description)
    url = url['href']

    
    offer_info = {
        'title':  title,   
        'price':  price,
        'price_per_meter': price_per_meter,
        'square': square,
        'description': description,
        'url':url
    }

    return offer_info