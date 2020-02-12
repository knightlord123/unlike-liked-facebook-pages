from selenium import webdriver
from time import sleep

class deleter():
    def __init__(self):
       # self.driver=webdriver.Chrome("D:/python/chromedriver.exe")
       chrome_options = webdriver.ChromeOptions()
       chrome_options.add_argument("--disable-notifications")
       self.driver = webdriver.Chrome("D:/python/chromedriver.exe",chrome_options=chrome_options)
        
    def login(self):
        self.driver.get('https://www.facebook.com/')
        fb_button = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_button.click()
        fb_button.send_keys("EMAIL")//ENTER EMAIL
        pas_button = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pas_button.click()
        pas_button.send_keys("PASSWD")//ENTER PASSWORD
        nxt_button = self.driver.find_element_by_xpath('//*[@id="u_0_b"]')
        nxt_button.click()
        arrow_button = self.driver.find_element_by_xpath('//*[@id="navItem_250100865708545"]/a/div[2]')
        arrow_button.click()
        sleep(3)
        act_button = self.driver.find_element_by_xpath('//*[@id="u_fetchstream_3_0"]/div/div/div/div[1]/ul/li[3]/a/div')
        act_button.click()
        sleep(2)
        for i in range (1,100):
          link= '//*[@id="all_liked_pages"]/div/div[' + str(i) + ']/div/div/div[2]/div[1]/button'
          dis_like = self.driver.find_element_by_xpath(link)
          dis_like.click()

bot = deleter()
bot.login()


