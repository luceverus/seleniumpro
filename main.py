from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

search_bar.send_keys("hello!")
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements_by_class_name("g")

print(search_results)

browser.quit()
