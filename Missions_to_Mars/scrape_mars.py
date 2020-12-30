#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup as bs
import requests
import splinter
import json
import pandas as pd
import time

def scrape_all():
    executable_path = {'executable_path' : 'c:/Users/eluba/Documents/GitHub/web-scraping-challenge/Missions_to_Mars/chromedriver.exe'}
    browser = splinter.Browser('chrome', **executable_path)

### NASA Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = bs(html, 'html.parser')

    content = soup.find("div", class_='list_text')
    title = content.find("div", class_='content_title')
    #title.text

    article = content.find("div", class_='article_teaser_body')
    #article.text

### JPL Mars Space Images
    url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_2)
    html = browser.html

    #soup = bs(html, 'html.parser')
    #featured_image = soup.find("article", class_='carousel_item')['style']
    #latter = featured_image.split('/spaceimages/')[1].split("'")[0]
    #former = url.split('?')[0]
    #final_url = former + latter
    #final_url

    browser.find_by_id("full_image").click()
    browser.find_by_text("more info     ").click()

    html = browser.html
    soup = bs(html, 'html.parser')
    featured_img = soup.find("img", class_='main_image')['src']
    featured_img
    pic_url = f"https://www.jpl.nasa.gov{featured_img}"
    #pic_url

### Mars Facts
    url_3 = 'https://space-facts.com/mars/'
    response = requests.get(url_3)
    soup = bs(response.text, 'html.parser')
    table = soup.find_all('table')[0]
#print(table)

    mars_facts = pd.read_html(str(table))
    #print(mars_facts)

    mars_table = mars_facts[0].to_json(orient='records')
    #print(mars_table)

    mars_df = pd.read_json(mars_table)
    #mars_df
### Mars Hemispheres
### Webpage does not respond
#url_4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
#browser.visit(url_4)
#print(url_4)
    browser.quit()

    mars_data = {
        "Mars_News_title": title.text,
        "Mars_News_Article": article.text,
        "Mars_Featured_Image": pic_url,
        "Mars_Facts": mars_df,
        #"Mars_Hemisphere": hemisphere_image_urls

        }
    return mars_data

data_test = scrape_all()
print(data_test)
