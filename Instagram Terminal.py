__author__ = "CAN CAKAR"

from selenium import webdriver
import time


# Instagram Terminal by CAN CAKAR

print("""
    ******************************************************************
    *                   Instagram Terminal v.1.0                     *
    *                                                                *
    *    Operations:                                                 *
    *                                                                *
    *       1 - Register                                             *
    *       2 - Login                                                *
    *       3 - Get Followers and Followings(Login required)         *
    *       4 - Change Password (Login required)                     *
    *       5 - Forgot Password                                      *
    *       6 - Search on Instagram                                  *
    *       7 - Quit Application                                     *
    ******************************************************************
""")
browser = webdriver.Chrome()
while True:
    op = input("Enter a operation: ")
    if op == "7":
        break
    elif op == "1":
        try:
            user_email = input("Enter your email or mobile number: ")
            user_name = input("Enter your full name: ")
            user_username = input("Enter username: ")
            user_pss = input("Enter password: ")

            browser.get("https://www.instagram.com/")
            time.sleep(2)
            inp_email = browser.find_element_by_name("emailOrPhone")
            inp_name = browser.find_element_by_name("fullName")
            inp_username = browser.find_element_by_name("username")
            inp_pss = browser.find_element_by_name("password")
            btn_sign = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')
            btn_replace = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[5]/div/div/div/button/span')

            inp_email.click()
            inp_email.send_keys(user_email)
            inp_name.click()
            inp_name.send_keys(user_name)
            inp_username.click()
            inp_username.send_keys(user_username)
            inp_pss.click()
            inp_pss.send_keys(user_pss)
            time.sleep(2)
            btn_replace.click()
            btn_sign.click()
            print("Signing up, please wait...")
            time.sleep(5)
            browser.close()
        except Exception:
            print("Something wrong...")
    
    elif op == "2":
        user_username = input("Phone number, username or email: ")
        user_pss = input("Enter password: ")
        browser.get("https://www.instagram.com/")
        time.sleep(2)
        btn_login = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        time.sleep(1)
        inp_username = browser.find_element_by_name("username")
        inp_pss = browser.find_element_by_name("password")
        btn_login = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        inp_username.click()
        inp_username.send_keys(user_username)
        inp_pss.click()
        inp_pss.send_keys(user_pss)
        btn_login.click()
        time.sleep(10)
        browser.close()
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "5":
        pass
    elif op == "6":
        pass
    elif op == "7":
        break
    else:
        print("Invalid operation!")