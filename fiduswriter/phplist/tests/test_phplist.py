import time

from selenium.webdriver.common.by import By
from testing.testcases import LiveTornadoTestCase
from testing.selenium_helper import SeleniumHelper

from django.core import mail


class PHPlistTest(LiveTornadoTestCase, SeleniumHelper):
    fixtures = [
        'initial_documenttemplates.json',
        'initial_styles.json'
    ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.base_url = cls.live_server_url
        driver_data = cls.get_drivers(1)
        cls.driver = driver_data["drivers"][0]
        cls.client = driver_data["clients"][0]
        cls.driver.implicitly_wait(driver_data["wait_time"])
        cls.wait_time = driver_data["wait_time"]

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_signup_yes_not_available(self):
        self.driver.get(self.base_url + "/account/sign-up/")
        self.driver.find_element_by_id(
            'id_username'
        ).send_keys('username_yes')
        self.driver.find_element_by_id(
            'id_password1'
        ).send_keys('password')
        self.driver.find_element_by_id(
            'id_password2'
        ).send_keys('password')
        self.driver.find_element_by_id(
            'id_email'
        ).send_keys('my.yes@email.com')
        self.driver.find_element_by_id(
            'signup-submit'
        ).click()
        time.sleep(1)
        signup_link = self.find_urls(mail.outbox[-1].body)[0]
        self.driver.get(signup_link)
        self.driver.find_element(
            By.ID,
            'terms-check'
        ).click()
        self.driver.find_element(
            By.ID,
            'test-check'
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            'input[name="emaillist"][value="yes"]'
        ).click()
        self.driver.find_element(
            By.ID,
            'submit'
        ).click()
        time.sleep(1)
        self.assertEqual(
            self.driver.find_element_by_css_selector(
                '.fw-contents h1'
            ).text,
            'Thanks for verifying!'
        )

    def test_signup_no_not_available(self):
        self.driver.get(self.base_url + "/account/sign-up/")
        self.driver.find_element_by_id(
            'id_username'
        ).send_keys('username_no')
        self.driver.find_element_by_id(
            'id_password1'
        ).send_keys('password')
        self.driver.find_element_by_id(
            'id_password2'
        ).send_keys('password')
        self.driver.find_element_by_id(
            'id_email'
        ).send_keys('my.no@email.com')
        self.driver.find_element_by_id(
            'signup-submit'
        ).click()
        time.sleep(1)
        signup_link = self.find_urls(mail.outbox[-1].body)[0]
        self.driver.get(signup_link)
        self.driver.find_element(
            By.ID,
            'terms-check'
        ).click()
        self.driver.find_element(
            By.ID,
            'test-check'
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            'input[name="emaillist"][value="no"]'
        ).click()
        self.driver.find_element(
            By.ID,
            'submit'
        ).click()
        time.sleep(1)
        self.assertEqual(
            self.driver.find_element_by_css_selector(
                '.fw-contents h1'
            ).text,
            'Thanks for verifying!'
        )
