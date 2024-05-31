from urllib.request import urlopen
from bs4 import BeautifulSoup

inner_html_code = str(urlopen('https://citaty.info/random').read(),'utf-8')

inner_soup = BeautifulSoup(inner_html_code, "html.parser")

def delete_div(code,tag,arg):
     for div in code.find_all(tag, arg):
        div.decompose()


def get_quote():
    for i in range(99):
        delete_div(inner_soup, "div", {'class':'page__body'+str(i)})
        delete_div(inner_soup, "nav", {'class':'header-nav__menu'+str(i)})
        delete_div(inner_soup, "div", {'class':'field-item even last'+str(i)})
        delete_div(inner_soup, "div", {'class':'nav__dropdown'+str(i)})
        delete_div(inner_soup, "ul", {'class':'nav'+str(i)})
        delete_div(inner_soup, "div", {'class':'html not-front not-logged-in one-sidebar sidebar-first page-random i18n-ru form-single-submit-processed popup-behavior-processed'+str(i)})

    delete_div(inner_soup, "li", {'class':'nav__item'})


    delete_div(inner_soup, 'pre','')

    delete_div(inner_soup,'code','')

    data = [i for i in inner_soup.get_text().split('\n') if i]
    text = data[6]
    return text
