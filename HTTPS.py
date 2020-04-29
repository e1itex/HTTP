from selenium import webdriver
 
options = webdriver.chromeoptions()
options.add_argument('headless')
driver = webdriver.chrome(chrome_options=options)
 
drive.get("https://www.us-proxy.org/")
 
tbody = driver.find_element_by_tag_name
 
cell = tbody.find_elements_by_tag_name("tr")
 
for column in cell:
	column = column.text.split("")
	print (column[0]+":"+column[1])

driver.quit()