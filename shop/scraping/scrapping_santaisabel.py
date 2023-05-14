from scrape_product_info import scrape_product_info_selenium

url = 'https://www.santaisabel.cl/arroz-grado-1-banquete-1-kg-premium-grano-largo-y-ancho/p'
brandClass= 'product-brand'
nameClass = 'product-name'
priceClass = 'product-sigle-price-wrapper'
imageClass = 'zoomed-image'

brand, name, price, image = scrape_product_info_selenium(url,brandClass,nameClass,priceClass,imageClass,imageClass)
print("Marca del producto:", brand)
print("Nombre del producto:", name)
print("Precio del producto:", price)
print("URL de la imagen:", image)