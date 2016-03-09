from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# define the URL and countries here as they have been supplied and do not change in this task
url = "http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk"
countries = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']

# Starts up Firefox and navigates to the URL
browser = webdriver.Firefox()
browser.get(url)