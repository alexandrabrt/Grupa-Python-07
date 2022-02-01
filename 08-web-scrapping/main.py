from selenium import webdriver
from bs4 import BeautifulSoup
from handlers.data import parse_data, write_output
from handlers.driver import accept_cookies


source = 'https://htmlcolorcodes.com/'


if __name__ == '__main__':
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()

    driver.get(source)

    accept_cookies(driver)

    soup = BeautifulSoup(driver.page_source, features='html.parser')
    colors = parse_data(soup)

    write_output(colors)

    driver.close()