def checkDependencies(): 
    import time
    
    print('Checking Dependency Packages......')

    time.sleep(0.5)

    print()
    print("checking for selenium...")
    try:
        import selenium
    except ImportError:
        print("you should install \'selenium\' before continuing.")
        wait = input("PRESS ENTER TO EXIT.")
        return -1
    
    time.sleep(0.5)

    print()
    print("checking for Beautifulsoup4...")
    try:
        import bs4
    except ImportError:
        print("you should install \'bs4\' before continuing.")
        wait = input("PRESS ENTER TO EXIT.")
        return -1
   
    time.sleep(0.5)

 
    print()
    print("checking for re...")
    try:
        import re
    except:
        print("you should install \'re\' before continuing.")
        wait = input("PRESS ENTER TO EXIT.")
        return -1
   
    time.sleep(0.5)

 
    print()
    print("checking for lxml...")
    try:
        import lxml
    except:
        print("you should install lxml parser before continuing.")
        wait = input("PRESS ENTER TO EXIT.")
        return -1
   
    time.sleep(0.5)

 
    print()
    print("checking for smtplib...")
    try:
        import smtplib
    except:
        print("you should install smtplib before continuing.")
        wait = input("PRESS ENTER TO EXIT.")
        return -1
   
    time.sleep(0.5)

 
    print()
    print("checking for dnspython...")
    try:
        import dns
    except:
        print("you should install dnspython before continuing.")
        wait = input("PRESS ENTER TO EXIT.")
        return -1
   
    time.sleep(0.5)

 
    print() 
    print("You are ready to go!!")
    return 1
