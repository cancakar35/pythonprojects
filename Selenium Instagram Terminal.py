#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

__author__ = "CAN ÇAKAR"


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
    
    def close_browser(self):
        self.driver.close()

    def login(self):
        try:
            self.driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(4)
            inp_username = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
            inp_password = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
            inp_username.click()
            inp_username.send_keys(self.username)
            inp_password.click()
            inp_password.send_keys(self.password)
            inp_password.send_keys(Keys.RETURN)
            time.sleep(3)
            not_now = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
            not_now.click()
            time.sleep(2)
        except Exception:
            print("Invalid username or password")

    def get_followers(self):
        try:
            self.driver.get("https://www.instagram.com/" + self.username + "/")
            followers_form = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
            followers_form.click()
            time.sleep(2)
            script = """
            flw_form = document.querySelector('.isgrP');
            flw_form.scrollTo(0, flw_form.scrollHeight);
            var lenPage = flw_form.scrollHeight;
            return lenPage;
            """
            page_len = self.driver.execute_script(script)
            x = False
            while (not(x)):
                page_last = page_len
                time.sleep(2)
                page_len = self.driver.execute_script(script)
                if page_last == page_len:
                    x = True
            time.sleep(3)
            followers_list = []
            followers_name = self.driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
            for i in followers_name:
                followers_list.append(i.text)

            with open("followers.txt", "w", encoding="UTF-8") as flw:
                for j in followers_list:
                    flw.write(j + "\n")
            
        except Exception:
            print("Something wrong...")
    
    def get_followings(self):
        try:
            self.driver.get("https://www.instagram.com/" + self.username + "/")
            followings_form = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
            followings_form.click()
            time.sleep(2)
            script = """
            flw_form = document.querySelector('.isgrP');
            flw_form.scrollTo(0, flw_form.scrollHeight);
            var lenPage = flw_form.scrollHeight;
            return lenPage;
            """
            page_len = self.driver.execute_script(script)
            x = False
            while (not(x)):
                page_last = page_len
                time.sleep(2)
                page_len = self.driver.execute_script(script)
                if page_last == page_len:
                    x = True
            time.sleep(3)
            followings_list = []
            followings_name = self.driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
            for i in followings_name:
                followings_list.append(i.text)
            with open("followings.txt", "w", encoding="UTF-8") as flwing:
                for j in followings_list:
                    flwing.write(j + "\n")
                
        except Exception:
            print("Something wrong...")
    
    def check_followers(self, old_list_file, new_list_file):
        with open(old_list_file, "r", encoding="UTF-8") as check:
            for i in check.readlines():
                new_flw = open(new_list_file, "r", encoding="UTF-8")
                control = False
                for j in new_flw.readlines():
                    if j.find(i) != -1:
                        control = False
                        break
                    else:
                        control = True
                if control:
                    i = i.strip("\n")
                    print("{} no longer following you".format(i))
                new_flw.close()



    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.close()


username = input("Kullanıcı adı: ")
password = input("Parola: ")

bot = InstagramBot(username=username, password=password)

bot.login()
print("""
******************************************************************
*                   Instagram Terminal v.1.0                     *
*                                                                *
*    Operations:                                                 *
*                                                                *
*       1 - Get Followers and Followings                         *
*       2 - Check users who unfollowed you                       *
*       3 - Quit Application                                     *
*                                                                *
******************************************************************
""")
while True:
    op = input("Enter a operation")
    if op == 1:
        bot.get_followers()
        bot.get_followings()
        print("Followers file: followers.txt, Followings file: followings.txt")
    elif op == 2:
        old = input("Enter old followers list file (like old.txt)")
        bot.get_followers()
        bot.check_followers(old, "followers.txt")
    elif op == 3:
        bot.close_browser()
    else:
        print("Invalid input!")
