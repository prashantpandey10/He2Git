from selenium import webdriver

browser=webdriver.Firefox()
url="https://www.hackerearth.com/submissions/prashantpandeyfun10/"
browser.get(url)
browser.implicitly_wait(20)

alllinks=[]

end=browser.find_element_by_xpath("/html/body/div[6]/div[4]/p")
viewbut=browser.find_element_by_xpath("//a[contains(@class,'load-scroll-content button btn-blue hidden') and .//text()='View More']")


while not end.is_displayed():
    webdriver.ActionChains(browser).move_to_element(viewbut).click(viewbut).perform()


alllinks=browser.find_elements_by_xpath("//a[contains(@class,'link-13') and  .//text()='View']")
allproblems=browser.find_elements_by_xpath("//a[contains(@class,'no-color hover-link')]")
allmarks=browser.find_elements_by_xpath("//div[contains(@class,'tool-tip')]")


it=1
f=open("hetogit.txt",'wb')
for i,j,k in zip(allproblems,allmarks,alllinks):
    if "correct-submission tool-tip" in j.get_attribute("outerHTML"):
        f.write(str(it)+"  ")
        f.write(i.text+"    ")
        f.write(k.get_attribute("href")+"  ")
        f.write("\n\n")
    it+=1