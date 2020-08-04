import unittest
from selenium import webdriver
import time

class TestLetsTalkTea(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\Chrome\chromedriver')
        self.url = self.driver.get("http://www.practiceselenium.com/welcome.html")

    def test_talk_tea(self):
        lets_talk_tea_button = self.driver.find_element_by_xpath('//ul[@class="wsb-navigation-rendered-top-level-menu "]/li[4]')
        lets_talk_tea_button.click()
        fields = self.driver.find_elements_by_xpath('//input[@type="text"]')
        one_field = []
        for i in fields:
            one_field.append(i)
        one_field[0].send_keys('Artem')
        one_field[1].send_keys('art@gmail.com')
        one_field[2].send_keys('Green tea')
        message = self.driver.find_element_by_xpath('//textarea[@class="form-value"]')
        message.send_keys('HELLO')
        submit = self.driver.find_element_by_xpath('//input[@class="form-submit"]')
        submit.click()
