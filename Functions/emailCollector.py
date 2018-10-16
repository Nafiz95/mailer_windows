def getEmails(link): 
    from selenium import webdriver
    import re

    
    #Go to the link
    chrome_path= r"./chromedriver_linux64/chromedriver"
    driver=webdriver.Chrome(chrome_path)
    driver.set_window_size(0,0)
    driver.set_window_position(15000,15000)
    try:
        driver.get(link) 
        respond = driver.execute_script("return document.documentElement.outerHTML")
    except:
        respond = ""
    driver.quit()
    
    email_list=re.findall(r'[\w\.-]+@[\w\.-]+', respond)
    
    return email_list
