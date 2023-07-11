import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def scrape_product_info_selenium(url,brandTag,nameTag,priceTag,imageTag,waitUntilTag):
    # Asegúrate de cambiar la ruta a la ubicación de tu ChromeDriver
    chrome_driver_path = '/path/to/chromedriver'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-javascript")
    
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    driver.get(url)

    if(waitUntilTag is None):
        print('no wait')
    else:
        # Aumentar el tiempo de espera a 5 segundos
        wait = WebDriverWait(driver, 15)

        # Esperar a que un elemento con class 'zoomed-image' esté presente en la página
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, waitUntilTag)))

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    product_brand = soup.find(class_=brandTag)
    product_brand_text = product_brand.text.strip() if product_brand else "No se pudo encontrar la marca del producto en la página."

    product_name = soup.find(class_=nameTag)
    product_name_text = product_name.text.strip() if product_name else "No se pudo encontrar el nombre del producto en la página."

    product_price =  soup.find(class_=priceTag)
    product_price_text = product_price.text.strip() if product_price else "No se pudo encontrar el precio del producto en la página."

    product_image =  soup.find(class_=imageTag)
    image_url = getImage(product_image)
    if image_url is None:
         image_url = getImage2(product_image)
    else:
        print("Se obtuvo la imagen")
    
   
    driver.quit()

    return product_brand_text, product_name_text, product_price_text, image_url

def getImage(product_image):
    img_element = product_image.find('img')

    if img_element:
        img_src = img_element['src']
        return img_src
    else:
        return None

def getImage2(product_image):
    if product_image:
        style = product_image['style']
        url_pattern = r"url\(['\"](.*?)['\"]\)"
        match = re.search(url_pattern, style)

        if match:
            image_url = match.group(1)
            return image_url
        else:
            return None
    else:
        return None


def scrape_product_info_requests(url,brandTag,nameTag,priceTag,imageTag):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            product_brand = soup.find(class_=brandTag)
            product_brand_text = product_brand.text.strip() if product_brand else "No se pudo encontrar la marca del producto en la página."

            product_name = soup.find(class_=nameTag)
            product_name_text = product_name.text.strip() if product_name else "No se pudo encontrar el nombre del producto en la página."

            product_price =  soup.find(class_=priceTag)
            product_price_text = product_price.text.strip() if product_price else "No se pudo encontrar el precio del producto en la página."

            
            product_image =  soup.find(class_=imageTag)
            img_element = product_image.find('img')

            if img_element:
                img_src = img_element['src']
            return product_brand_text, product_name_text, product_price_text, img_src
        else:
            print("Error al realizar la solicitud:", response.status_code)
        return None,None,None,None

def scrape_product_price(url,priceTag):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')


            product_price =  soup.find(class_=priceTag)
            product_price_text = product_price.text.strip() if product_price else "No se pudo encontrar el precio del producto en la página."

            return product_price_text
        else:
            print("Error al realizar la solicitud:", response.status_code)
        return None
