def main():  
    import sys
    import os
    sys.path.append("./Functions/")

    from dependencyChecker import checkDependencies
    from netSurfer import search 
    from linkCollector import getLinks
    from emailActivityChecker import checkActivity
    from emailCollector import getEmails

    print("""
            Welcome To The Mailer
    ------------------------------------ 

    """)

    #Check for dependencies. Abort if any package is missing 
    dependencies_check_result = checkDependencies()
    if dependencies_check_result == -1:
        return
    
    wait = input("PRESS ENTER TO CONTINUE.")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #Search Internet for keyword(s) and Get links
    keywords = input("Enter Query String: ")
    res = search(keywords)
    links = getLinks(res)
    if len(links) <= 0:
        print("Oops!! Noting Found!")
        wait = input("PRESS ENTER TO EXIT.")
        return
    email_list=[]
    link_counter=1
    print(str(len(links))+" Links Found")
    print("Searching Each Link ...")
    
    for link in links:
        print("Link No. "+ str(link_counter))
        link_counter = link_counter + 1
        email_list = email_list + getEmails(link)
    
    
    email_list= list(set(email_list))
    print(email_list)

main()
