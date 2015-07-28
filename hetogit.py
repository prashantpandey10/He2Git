from selenium import webdriver

browser=webdriver.Firefox()
url="https://www.hackerearth.com/submissions/prashantpandeyfun10/"  # append your username instead of mine!
browser.get(url)                                                    # This opens a firefox console  
browser.implicitly_wait(20)

# this is the xpath of "No more submission" element.
end=browser.find_element_by_xpath("/html/body/div[6]/div[4]/p")     

# this is the xpath of "View More" button which needs to be clicked to load more submission
viewbut=browser.find_element_by_xpath("//a[contains(@class,'load-scroll-content button btn-blue hidden') and .//text()='View More']")

""" 
Traverse till "No more submission" element is not visible and when
you scroll for 5 times you will see "View More" button so you need
to click it to load more data
"""
while not end.is_displayed():
    webdriver.ActionChains(browser).move_to_element(viewbut).click(viewbut).perform()

""" 
alllinks store all links to my solution
allproblems contain all problem name
allmarks contain respective score
"""
alllinks=browser.find_elements_by_xpath("//a[contains(@class,'link-13') and  .//text()='View']")
allproblems=browser.find_elements_by_xpath("//a[contains(@class,'no-color hover-link')]")
allmarks=browser.find_elements_by_xpath("//div[contains(@class,'tool-tip')]")

# Written all scraped data to file.
it=1
f=open("hetogit.txt",'wb')
for i,j,k in zip(allproblems,allmarks,alllinks):
    if "correct-submission tool-tip" in j.get_attribute("outerHTML"):
        f.write(str(it)+"  ")
        f.write(i.text+"    ")
        f.write(k.get_attribute("href")+"  ")
        f.write("\n\n")
    it+=1
