""" This module contains an example of a shared, global driver.

😱 Be careful with this!
Sharing data and state between tests can have them "tripping" over each other
and affect each other's outcome which is probably not what you want.

😬 Also, don't have test function 3️⃣ be dependent on test function 2️⃣ which is dependent on 1️⃣
1️⃣ > 2️⃣ > 3️⃣

> This removes their ability to be executed in parallel because you've forced a sequential flow

Instead:
🚘 Each test should get its own instance of a driver (and any objects dependent on a driver like Page Objects)
🔀 Tests should be independent of each other
🤏 Tests should be as modular as possible, but do what makes sense for you!
💡 Tests should manage their own data and state (but that's for a different course)

Following these guidelines will enable you to run all your tests in parallel!
"""
import time
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


class TodoPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def goto(self) -> 'TodoPage':
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        return self

    def get_all_todos(self) -> List[WebElement]:
        return self.driver.find_elements_by_css_selector("li[ng-repeat*='todo'] > input")

    def add_todo(self, name: str) -> 'TodoPage':
        self.driver.find_element_by_id('sampletodotext').send_keys(name)
        self.driver.find_element_by_id('addbutton').click()
        return self


""" 😅 Shared, global driver. """
driver = webdriver.Chrome(ChromeDriverManager().install())
page = TodoPage(driver).goto()


def test_add_new_item():
    page.add_todo(name='Make tests independent')
    time.sleep(5)  # DEMO: simulate more complicated flow
    todos = page.get_all_todos()
    assert len(todos) == 6


def test_add_blank_item():
    time.sleep(3)  # DEMO: simulate more complicated flow
    page.add_todo(name='')
    todos = page.get_all_todos()
    assert len(todos) == 6


def test_add_two_items():
    page.add_todo(name='Watch module 3')
    page.add_todo(name='Watch module 4')
    todos = page.get_all_todos()
    assert len(todos) == 7
