from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def netflix_login():
    global browser
    try:
        browser
        return browser
    except NameError:    
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--wondow-size=1920x1080")
        browser=webdriver.Chrome(chrome_options=chrome_options)
        browser.implicitly_wait(3)
        browser.get('http://www.netflix.com/pt-en/login')
        browser.find_element_by_class_name('input_id').send_keys(os.environ.get('FLIX_USER')) 
        browser.find_elements_by_class_name('input_id')[1].send_keys(os.environ.get('FLIX_PWD'))
        browser.find_elements_by_css_selector('button')[1].click()
        browser.find_element_by_link_text('Martin').click()
        return browser

def film_search(browser, filmname):  
    browser.find_element_by_class_name('icon-search').click()
    browser.find_element_by_tag_name('input').clear()
    browser.find_element_by_tag_name('input').send_keys(filmname)
    time.sleep(2)
    try:
        links=[]
        imgs=[]
        for i in range (0,3):
            print(i)
            links.append(browser.find_elements_by_class_name('title-card-container')[i].text)
            imgs.append(browser.find_elements_by_class_name('boxart-image')[i].get_attribute('src'))
    except Exception as e:
        #print(e)
        links=[]
        imgs=[]
    browser.find_element_by_tag_name('input').clear()
    return browser, links, imgs

#netflix_login()

