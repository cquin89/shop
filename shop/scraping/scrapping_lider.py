from shop.scraping.scrape_product_info import scrape_product_info_selenium
from shop.scraping.scrape_product_info import scrape_product_price

brandClass= 'prduct-detail-cart__brand-link'
nameClass = 'product-detail-display-name'
priceClass = 'pdp-mobile-sales-price'
imageClass = 'desktop__primary-image-container'

def scrappingLider(url):
    brand, name, price, image = scrape_product_info_selenium(url,brandClass,nameClass,priceClass,imageClass,imageClass)
    return brand,name,price,image,"Lider",url


def scrappingLiderPrice(url):
    price = scrape_product_price(url,priceClass)
    print("Precio del producto:", price)
    return price
