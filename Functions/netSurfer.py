def search(query_string_input): 
    from selenium import webdriver
     
    query_string = query_string_input.replace(' ','+')
    query_string = "https://www.google.com/search?q="+query_string

    chrome_path= r"E:\mailer_windows/chromedriver"
    driver=webdriver.Chrome(chrome_path)
    
    driver.set_window_size(0,0)
    driver.set_window_position(15000,15000)
    
    driver.get(query_string)
    
    respond = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    return respond