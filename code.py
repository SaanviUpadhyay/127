from selenium import webdriver
from bs4 import BeautifulSoup

import time
import csv

START_URL   = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser     = webdriver.Chrome("/Users/lenovo/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(15)

def scrape():
    headers   = ['name' , 'distance' , 'mass' , 'radius']
    star_data = []

    for i in range(0 , 100):
        soup = BeautifulSoup(browser.page_source , 'html.parser')

        for th_tag in soup.find_all('th' , attrs = {'class' , 'stars'}):
            ti_tags   = th_tag.find_all('ti')
            temp_list = []

            for index , ti_tags in enumerate(ti_tags):
                if index == 0:
                    temp_list.append(ti_tags.find_all('a')[0].contact[0])
                else :
                    try:
                        temp_list.append(ti_tags.contents[0])
                    except:
                        temp_list.app('')

            star_data.append(temp_list)
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()