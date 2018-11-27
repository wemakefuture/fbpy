#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .urls import get_facebook_url
from .urls import get_facebook_url_wish
import random
import time

class Facebook:

    def __init__(self, headless=False):
        # chrome initialization
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        if headless:
            options.add_argument('headless')
            options.add_argument('window_size=1024x768')
        self.driver = webdriver.Chrome('./assets/chromedriver.exe',
                                       chrome_options=options)
        #for windows use chromedriver.exe

    def login(self, user, passwd):
        self.driver.get(get_facebook_url())
        user_field = self.driver.find_element_by_xpath("//input[@id='email']")
        passwd_field = self.driver.find_element_by_xpath("//input[@id='pass']")
        ActionChains(self.driver).move_to_element(
            user_field).click().send_keys(user).perform()
        ActionChains(self.driver).move_to_element(
            passwd_field).click().send_keys(passwd).perform()
        self.driver.find_element_by_id('loginbutton').click()

    def wishes(self, greetings):
        self.driver.get(get_facebook_url_wish())
        wishbox = self.driver.find_elements_by_tag_name("textarea")
        boxIndex = 0
        for commentBox in wishbox:
            boxIndex += 1
            if (self):
                commentBox.click()
                print('clicked first box')
                time.sleep(2)
                if (self):
                    time.sleep(2)
                    commentInput = self.driver.find_element_by_tag_name("textarea")
                    ActionChains(self.driver).move_to_element(commentInput).click()
                    commentInput.send_keys(random.choice(greetings))
                    print('worked')
                    """commentInput.submit()"""
                    commentInput.submit()
                    time.sleep(2)
                    print('wished happy bday')
        self.driver.close()
        return None

"""
                    commentInput.click()
                wish.submit()
                print('wished happy bday')
                time.sleep(5)
                .perform())
                """
#       now wishes needs to repeat till it doesnt find anymore "textArea"
#       //*[@id="birthdays_content"]/div[1]  it should find the amount of People / "textArea"s in this and exactly this often repeat to post the greetings
#       if amount people is not equal amout of text boxes it should find the person "who blocked their time line" and write them a PM
#       self.driver.send_keys(random.choice(greetings_keys).ENTER) <-- why does this not work?
