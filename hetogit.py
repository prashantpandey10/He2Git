from sys import argv

selenium_present = True

try:
    from selenium import webdriver
  
except ImportError:
    selenium_present = False
if not selenium_present:
    print '''Please install python package "selenium" to use HEtoGit'''
    exit(0)

if len(argv) < 2:
    print 'Usage: hetogit.py <username>'
    exit(0)
else:
    username = argv[1]

browser=webdriver.Firefox()
url="https://www.hackerearth.com/submissions/{0}/".format(username)
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
    try:
        webdriver.ActionChains(browser).move_to_element(viewbut).click(viewbut).perform()
    except Exception:
        pass

""" 
alllinks store all links to my solution
allproblems contain all problem name
allmarks contain respective score
"""
alllinks=browser.find_elements_by_xpath("//a[contains(@class,'link-13') and  .//text()='View']")
allproblems=browser.find_elements_by_xpath("//a[contains(@class,'no-color hover-link')]")
allmarks=browser.find_elements_by_xpath("//div[contains(@class,'tool-tip')]")

# Written all scraped data to file.
solution_cnt=1
with open("hetogit.txt",'wb') as f:
    for problem, marks, link in zip(allproblems,allmarks,alllinks):
        if "correct-submission tool-tip" in marks.get_attribute("outerHTML"):
            problem_link = link.get_attribute("href")
            data = "{0} {1}    {2}\n\n".format(solution_cnt, problem.text, problem_link)
            f.write(data)
        solution_cnt+=1
