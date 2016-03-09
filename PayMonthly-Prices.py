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
    
    # After performing the search, click the button to get the rates for pay monthly.
    payMonthlyButton = browser.find_element_by_id('paymonthly')
    payMonthlyButton.click()
    
    # Now we get the price table and print it out
    standardRates = browser.find_element_by_id('standardRatesTable')
    for row in standardRates.find_elements(By.TAG_NAME, 'tr'):
        print row.text
    
# define the URL and countries here as they have been supplied and do not change in this task
url = "http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk"
countries = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']

# Starts up Firefox and navigates to the URL
browser = webdriver.Firefox()
browser.get(url)

# Get country rates for the countries specified
for country in countries:
    getCountryRates(country)