try:
    ## Importing pre-requisites
    from selenium import webdriver
    ## Importing dependencies
    from core.chat_bot import activate_bot
    from core.recursive import text_recursively
except Exception as e:
    package = str(e).split()[-1]
    print("ERROR")
    print("{} package not found" .format(package))
    print("Please install the module", package)


# Driver to open a browser
try:
    driver = webdriver.Chrome('/media/subhasish/Professional/git_repos/chat_bot/chromedriver_linux64/chromedriver')
    print("Using Chrome as default browser")
except:
    driver = webdriver.Firefox(executable_path = r"D:/Academics/GIT-repository/Colaboration/Chat_bot/Firefox/geckodriver/geckodriver.exe")
    print("Using Firefox as default browser")
#link to open a site
driver.get("https://web.whatsapp.com/")
input("Scan the QR code and then press Enter")

user_input = 'temp'
while user_input != 'q':
    print("\nEnter 'r' for recursive message")
    print("\nEnter 'a' for activaing BOT")
    print("\nEnter 'q' to EXIT")
    user_input = input()
    if user_input == 'r':
        text_recursively(driver)
    elif user_input == 'a':
        activate_bot(driver)
    elif user_input == 'q':
        driver.quit()
