import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options  # Added import for headless mode

class TestSmokeTest():
    def setup_method(self, method):
        # Configure Chrome to run in headless mode
        options = Options()
        options.add_argument("--headless=new")  # Set headless mode
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_directoryTest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1440, 778)
        self.driver.find_element(By.LINK_TEXT, "Directory").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
        self.driver.find_element(By.ID, "directory-list").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    
    def test_informationTest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1440, 778)
        self.driver.find_element(By.LINK_TEXT, "Join").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".myinput:nth-child(2)")
        assert len(elements) > 0
        self.driver.find_element(By.NAME, "fname").click()
        self.driver.find_element(By.NAME, "fname").send_keys("Kylie")
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(By.NAME, "lname").send_keys("Chatman")
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(By.NAME, "bizname").click()
        self.driver.find_element(By.NAME, "bizname").click()
        self.driver.find_element(By.NAME, "bizname").send_keys("Smiling Friends")
        self.driver.find_element(By.NAME, "biztitle").click()
        self.driver.find_element(By.NAME, "biztitle").send_keys("Smile Coordinator")
        self.driver.find_element(By.NAME, "submit").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".myinput:nth-child(2)")
        assert len(elements) > 0
    
    def test_joinUsLinkTest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1440, 778)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > .centered-image")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.LINK_TEXT, "Join Us!")
        assert len(elements) > 0
        self.driver.find_element(By.LINK_TEXT, "Join Us!").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "section > h3").text == "Welcome to the Teton Chamber of Commerce Signup Wizard!"
    
    def test_nameandLogoTest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1440, 778)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
        assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
        assert self.driver.title == "Teton Idaho CoC"
    
    def test_usernametest(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1440, 778)
        self.driver.find_element(By.LINK_TEXT, "Admin").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("crazyfrog")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".errorMessage")
        assert len(elements) > 0
