from shop.scraping.scrape_product_info import scrape_product_info_requests
from shop.scraping.scrape_product_info import scrape_product_price

brandClass= 'Text_text__cB7NM ProductDetail_textBrand__IRQMn Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--semibold__MukSj Text_text--lg__GZWsa Text_text--black__zYYxI Text_text__cursor--pointer__WZsQE Text_text--none__zez2n'
nameClass = 'Text_text__cB7NM Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--regular__KSs6J Text_text--2xl__Kf5kN Text_text--black__zYYxI Text_text__cursor--auto__cMaN1 Text_text--none__zez2n'
priceClass = 'Text_text__cB7NM Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--semibold__MukSj Text_text--3xl__tLA7o Text_text--guardsman-red__wr1D8 Text_text__cursor--auto__cMaN1 Text_text--none__zez2n'
imageClass = 'baseContainer_container__TSgMX baseContainer_justify-start___sjrG baseContainer_align-start__6PKCY baseContainer_flex-direction--column__iiccg baseContainer_absolute-default--topLeft__lN1In'

def scrappingUnimarc(url):
    brand, name, price, image = scrape_product_info_requests(url,brandClass,nameClass,priceClass,imageClass)
    return brand,name,price,image,"Unimarc",url


def scrappingUnimarcPrice(url):
    price = scrape_product_price(url,priceClass)
    print("Precio del producto:", price)
    return price
