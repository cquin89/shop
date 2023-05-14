from scrape_product_info import scrape_product_info_selenium
from scrape_product_info import scrape_product_price

url = 'https://www.jumbo.cl/arroz-integral-c-and-co-1-kg-1893883/p'
brandClass= 'product-brand'
nameClass = 'product-name'
priceClass = 'product-sigle-price-wrapper'
imageClass ='zoomed-image'

brand, name, price, image = scrape_product_info_selenium(url,brandClass,nameClass,priceClass,imageClass,imageClass)
print("Marca del producto:", brand)
print("Nombre del producto:", name)
print("Precio del producto:", price)
print("URL de la imagen:", image)


price = scrape_product_price(url,priceClass)
print("Precio del producto:", price)