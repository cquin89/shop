from shop.scraping.scrape_product_info import scrape_product_info_selenium
from shop.scraping.scrape_product_info import scrape_product_price

brandClass= 'Text_text__cB7NM ProductDetail_textBrand__IRQMn Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--bold__8_Ayh Text_text--lg__GZWsa Text_text--black__zYYxI Text_text__cursor--pointer__WZsQE Text_text--none__zez2n'
nameClass = 'Text_text__cB7NM Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--regular__KSs6J Text_text--xl__l05SR Text_text--black__zYYxI Text_text__cursor--auto__cMaN1 Text_text--none__zez2n'
priceClass = 'Text_text__cB7NM Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--medium__rIScp Text_text--2xl__Kf5kN Text_text--guardsman-red__wr1D8 Text_text__cursor--auto__cMaN1 Text_text--none__zez2n'
imageClass = 'baseContainer_container__TSgMX baseContainer_justify-center__hKrln baseContainer_align-start__6PKCY baseContainer_flex-direction--row__4HZkU baseContainer_absolute-default--topLeft__lN1In'

def scrappingUnimarc(url):
    brand, name, price, image = scrape_product_info_selenium(url,brandClass,nameClass,priceClass,imageClass,None)
    return brand,name,price,image,"Unimarc",url


def scrappingUnimarcPrice(url):
    price = scrape_product_price(url,priceClass)
    print("Precio del producto:", price)
    return price
