from selenium import webdriver
from base.browser_setup import browser_setup


class BaseSetup:

    def setUp(self):
        if browser_setup["browser"] == "firefox":
            self.driver = webdriver.Firefox()
        elif browser_setup["browser"] == "chrome":
            self.driver = webdriver.Chrome("/home/crazydogretro/PycharmProjects/SiteAutomated/drivers/chromedriver")
        else:
            raise Exception("Selected browser not supported")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(browser_setup["url"])

    def tearDown(self):
        self.driver.quit()
