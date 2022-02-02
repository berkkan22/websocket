from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def open():
    global driver
    driver = webdriver.Chrome(
        executable_path=r'D:\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.canlitv.mobi")


def switchSelenium(channal):
    driver.get("https://www.canlitv.mobi/kanal-7-hd-izle")

    # play

    # wait bis lade kreis weg ist

    # voll bild
