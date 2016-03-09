from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This will get the country rates, done here so as not to repeat code for each country
def getCountryRates(country):
    print '----------' + country + '----------'
    # This finds the search box for the country, clears any text that may
    # already be there and searches for the country we are looking for
    countrySearch = browser.find_element_by_id('countryName')
    countrySearch.clear()
    countrySearch.send_keys(country + Keys.ENTER)
    
    # After performing the search, click the button to get the rates for pay monthly.
    try:
        # I encountered an issue where the button would be looked for before it was active
        # This will try for a few seconds to find it before continuing on
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'paymonthly'))
        )
    except:
        # If the pay monthly button is never found let the user know the reason for the error
        print "Couldn't find the Pay Monthly Button"
    else:
        payMonthlyButton = browser.find_element_by_id('paymonthly')
        payMonthlyButton.click()
        # Now we get the price table and print it out
        standardRates = browser.find_element_by_id('standardRatesTable')
        for row in standardRates.find_elements(By.TAG_NAME, 'tr'):
            print row.text            
    
# define the URL and countries here as they have been supplied and do not change in this task
url = "http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk"
pageTitle = "O2 | International | International Caller Bolt On"
countries = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']

# Starts up Firefox and navigates to the URL
browser = webdriver.Firefox()
browser.get(url)

# Check we are on the right page
try:
    element = WebDriverWait(browser, 10).until(
        EC.title_contains("O2 | International")
    )
except:
    print "On the wrong page exiting browser"
    browser.quit()
else:
    # Get country rates for the countries specified
    for country in countries:
        getCountryRates(country)

    browser.quit()