from shop.scraping.scrape_product_info import scrape_product_info_selenium
from shop.scraping.scrape_product_info import scrape_product_price

brandClass= 'jsx-1874573512 product-brand fa--brand false'
nameClass = 'jsx-1442607798 product-name fa--product-name false'
priceClass = 'jsx-749763969 prices-0'
imageClass = 'jsx-4112511439 image-wrapper'

def scrappingTottus(url):
    brand, name, price, image = scrape_product_info_selenium(url,brandClass,nameClass,priceClass,imageClass,imageClass)
    return brand,name,price,image,"Tottus",url


def scrappingTottusPrice(url):
    price = scrape_product_price(url,priceClass)
    print("Precio del producto:", price)
    return price
