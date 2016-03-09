from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# This will get the country rates, done here so as not to repeat code for each country
def getCountryRates(country):
    print '----------' + country + '----------'
    # This finds the search box for the country, clicks on it to clear any text that might
    # already be there and searches for the country we are looking for
    countrySearch = browser.find_element_by_id('countryName')
    countrySearch.click()
    countrySearch.send_keys(country + Keys.RETURN)
    

# define the URL and countries here as they have been supplied and do not change in this task
url = "http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk"
countries = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']

# Starts up Firefox and navigates to the URL
browser = webdriver.Firefox()
browser.get(url)

# Test case
getCountryRates(countries[0])