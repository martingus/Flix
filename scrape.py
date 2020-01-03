from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def netflix_login(form):
    global browser, logged_in
    try:   
        chrome_options = Options() #to allow headless browser mode
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--window-size=1920x1080")
        browser=webdriver.Chrome(chrome_options=chrome_options)
        browser.implicitly_wait(3)
        browser.get('http://www.netflix.com/pt-en/login')
        browser.find_element_by_class_name('input_id').send_keys(form.username.data) 
        browser.find_elements_by_class_name('input_id')[1].send_keys(form.password.data)
        browser.find_elements_by_css_selector('button')[1].click()
        browser.find_element_by_link_text(form.name.data).click()
        logged_in=1
        return logged_in
    except:
        browser.close()
        logged_in=0
        return logged_in

def film_search(filmname):  
    browser.find_element_by_class_name('icon-search').click()
    browser.find_element_by_tag_name('input').clear()
    browser.find_element_by_tag_name('input').send_keys(filmname)
    time.sleep(2)
    try:
        links=[]
        imgs=[]
        for i in range (0,3):
            links.append(browser.find_elements_by_class_name('title-card-container')[i].text)
            imgs.append(browser.find_elements_by_class_name('boxart-image')[i].get_attribute('src'))
    except Exception as e:
        #print(e)
        links=[]
        imgs=[]
    browser.find_element_by_tag_name('input').clear()
    return links, imgs

#netflix_login()

