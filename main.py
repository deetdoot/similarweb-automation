from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()

site = input()

baseurl = "https://www.similarweb.com/website/"+ site +"/"

try:
    browser.get(baseurl)
    browser.maximize_window()


    xpaths = dict(globalrank="/html/body/div[1]/main/div/div/section[2]/div/ul/li[1]/div[2]",
                  homecountry="/html/body/div[1]/main/div/div/section[2]/div/ul/li[2]/div[1]/div[2]",
                  countryrank="/html/body/div[1]/main/div/div/section[2]/div/ul/li[2]/div[2]",
                  category="/html/body/div[1]/main/div/div/section[2]/div/ul/li[3]/div[1]/div[2]/a",
                  categoryrank="/html/body/div[1]/main/div/div/section[2]/div/ul/li[3]/div[2]",
                  total_monthly_visit="/html/body/div[1]/main/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/span[2]/span[1]",
                  avg_duration="/html/body/div[1]/main/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div/span[2]/span",
                  pages_per_visit = "/html/body/div[1]/main/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[4]/div/span[2]/span",
                  bounce_rate="/html/body/div[1]/main/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[5]/div/span[2]/span",

    )


    global_rank_number = browser.find_element_by_xpath(xpaths['globalrank']).text
    home_country = browser.find_element_by_xpath(xpaths['homecountry']).text
    country_rank = browser.find_element_by_xpath(xpaths['countryrank']).text
    category_name = browser.find_element_by_xpath(xpaths['category']).text
    category_rank = browser.find_element_by_xpath(xpaths['categoryrank']).text
    total_monthly_visit_data = browser.find_element_by_xpath(xpaths['total_monthly_visit']).text
    avg_duration = browser.find_element_by_xpath(xpaths['avg_duration']).text
    pages_per_visit = browser.find_element_by_xpath(xpaths['pages_per_visit']).text
    bounce_rate = browser.find_element_by_xpath(xpaths['bounce_rate']).text


    country_data_dict = {}
    i = 1
    while i < 6:
        key = 'country' + str(i)
        try:
            value1 = browser.find_element_by_xpath("//*[@id='geo-countries-accordion']/div[" + str(i) + "]/div/span/span[2]/span").text
        except:
            if NoSuchElementException:
                value1 = browser.find_element_by_xpath("//*[@id='geo-countries-accordion']/div[" + str(i) + "]/div/span/span[2]/a").text
        value2 = browser.find_element_by_xpath( "//*[@id='geo-countries-accordion']/div[" + str(i) + "]/div/span/span[1]/span[1]").text
        country_data_dict[key] = [value1,value2]
        i += 1



    print(' {} \t {} \t  {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t  {} \t {} \t {} \t {} \t {} \t {} \t {} \t'. format(global_rank_number, home_country, country_rank, category_name , category_rank , total_monthly_visit_data, avg_duration, pages_per_visit, bounce_rate, country_data_dict.get('country1')[0], country_data_dict.get('country1')[1], country_data_dict.get('country2')[0], country_data_dict.get('country2')[1], country_data_dict.get('country3')[0], country_data_dict.get('country3')[1],country_data_dict.get('country4')[0], country_data_dict.get('country4')[1], country_data_dict.get('country5')[0], country_data_dict.get('country5')[1] ))

except:
    print ('no data found')