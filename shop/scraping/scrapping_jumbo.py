from shop.scraping.scrape_product_info import scrape_product_info_selenium
from shop.scraping.scrape_product_info import scrape_product_price

brandClass= 'product-brand'
nameClass = 'product-name'
priceClass = 'prices-main-price'
imageClass ='zoomed-image'

def scrappingJumbo(url):
    brand, name, price, image = scrape_product_info_selenium(url,brandClass,nameClass,priceClass,imageClass,imageClass)
    return brand,name,price,image,"Jumbo",url


def scrappingJumboPrice(url):
    price = scrape_product_price(url,priceClass)
    print("Precio del producto:", price)
    return price
