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

    final_mars_df = pd.DataFrame({'':mars_df[0],'Mars':mars_df[1]})
    #final_mars_df

    ### Mars Hemispheres
    ### Webpage does not respond
    ###url_4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    ### Used https://www.planetary.org/ page instead


    #Schiaparelli Hemisphere
    url_4 = 'https://www.planetary.org/space-images/mars-schiaparelli-hemisphere'
    browser.visit(url_4)
    html = browser.html

    temp_title = browser.find_by_tag('h1')
    schiaparelli_title = temp_title[0].text
    browser.find_by_tag('figure').click()

    soup = bs(browser.html, 'html.parser')
    schiaparelli_img = soup.find("img")['src']
    schiaparelli_img


    #Valles Marineris Hemisphere
    url_5 = 'https://www.planetary.org/space-images/20140202_valles_marineris_enhanced'
    browser.visit(url_5)
    html = browser.html

    temp_title = browser.find_by_tag('h1')
    valles_marineris_title = temp_title[0].text
    browser.find_by_tag('figure').click()

    soup = bs(browser.html, 'html.parser')
    valles_marineris_img = soup.find("img")['src']
    valles_marineris_img

    #Cerberurs Hemisphere
    url_6 = 'https://www.planetary.org/space-images/20140202_cerberus_enhanced'
    browser.visit(url_6)
    html = browser.html

    temp_title = browser.find_by_tag('h1')
    cerberus_title = temp_title[0].text
    browser.find_by_tag('figure').click()

    soup = bs(browser.html, 'html.parser')
    cerberus_img = soup.find("img")['src']
    cerberus_img

    #Syrtis Major Hemisphere
    url_7 = 'https://www.planetary.org/space-images/20140202_syrtis_major_enhanced'
    browser.visit(url_7)
    html = browser.html

    temp_title = browser.find_by_tag('h1')
    syrtis_major_title = temp_title[0].text
    browser.find_by_tag('figure').click()

    soup = bs(browser.html, 'html.parser')
    syrtis_major_img = soup.find("img")['src']
    syrtis_major_img

    hemisphere_image_urls = [
        {"title": valles_marineris_title, "img_url": valles_marineris_img},
        {"title": cerberus_title, "img_url": cerberus_img},
        {"title": schiaparelli_title, "img_url": schiaparelli_img},
        {"title": syrtis_major_title, "img_url": syrtis_major_img},
    ]

    hemisphere_image_urls
    time.sleep(5)
    browser.quit()

    mars_data = {
        "Mars_News_title": title.text,
        "Mars_News_Article": article.text,
        "Mars_Featured_Image": pic_url,
        "Mars_Facts": final_mars_df.to_html(),
        "Mars_Hemisphere": hemisphere_image_urls
        }
    return mars_data

#data_test = scrape_all()
#print(data_test)
