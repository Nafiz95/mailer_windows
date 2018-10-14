def getEmails(link = "https://www.randomlists.com/email-addresses"): 
    from selenium import webdriver
    
    #Go to the link
    chrome_path= r"E:\mailer_windows/chromedriver"
    driver=webdriver.Chrome(chrome_path)
    driver.set_window_size(0,0)
    driver.set_window_position(15000,15000)
    driver.get(link) 
    respond = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    
    
    #Search for Mail
    mail_list=[]
    print(respond)
    #If eamil
    #push to mail_list
    #return mail_list 
getEmails()