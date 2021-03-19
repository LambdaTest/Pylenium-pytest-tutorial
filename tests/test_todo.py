import os
import pytest
from selenium import webdriver
from pylenium.config import PyleniumConfig
from pylenium.driver import Pylenium
from pylenium.element import Element, Elements


class TodoPage:
    def __init__(self, py: Pylenium):
        self.py = py

    def goto(self) -> 'TodoPage':
        self.py.visit('https://lambdatest.github.io/sample-todo-app/')
        return self

    def get_todo_by_name(self, name: str) -> Element:
        return self.py.getx(f"//*[text()='{name}']").parent().get('input')

    def get_all_todos(self) -> Elements:
        return self.py.find("li[ng-repeat*='todo'] > input")

    def add_todo(self, name: str) -> 'TodoPage':
        self.py.get('#sampletodotext').type(name)
        self.py.get('#addbutton').click()
        return self


@pytest.fixture
def selenium():
    # 1. Define the 3 pieces needed to connect to LambdaTest
    username = os.getenv('LT_USERNAME')
    access_key = os.getenv('LT_ACCESS_KEY')
    remote_url = "https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)

    # 2. Define the Desired Capabilities for this Test Run
    desired_caps = {
        "build": 'PyunitTest sample build',  # Change your build name here
        "name": 'Py-unittest',  # Change your test name here
        "platform": 'Windows 10',  # Change your OS version here
        "browserName": 'Chrome',  # Change your browser here
        "version": '87.0',  # Change your browser version here
        "resolution": '1024x768',  # Change your resolution here
        "console": 'true',  # Enable or disable console logs
        "network": 'true'   # Enable or disable network logs
    }

    # 3. Instantiate a new Remote WebDriver that is connected to LambdaTest
    driver = webdriver.Remote(
        command_executor=remote_url,
        desired_capabilities=desired_caps)

    # 4. Yield the driver so the test can use it, then quit() when the test is complete
    yield driver
    driver.quit()


@pytest.fixture
def LT(py_config: PyleniumConfig):
    # 1. Define the 3 pieces needed to connect to LambdaTest
    username = os.getenv('LT_USERNAME')
    access_key = os.getenv('LT_ACCESS_KEY')
    remote_url = f'https://{username}:{access_key}@hub.lambdatest.com/wd/hub'
    # update Pylenium's config with this URL
    # * You can also set this in pylenium.json or via the CLI! *
    py_config.driver.remote_url = remote_url

    # 2. Update the Desired Capabilities for this Test Run
    desired_caps = {
        "build": 'pytest build',
        "name": 'pytest tutorial',
        "platform": 'Windows 10',
        "browserName": 'Chrome',
        "version": '87.0',
        "resolution": '1024x768',
        "console": 'true',
        "network": 'true'
    }
    # update Pylenium's config with this dictionary
    # * You can also set this in pylenium.json or via the CLI! *
    py_config.driver.capabilities.update(desired_caps)

    # 3. Instantiate a new instance of Pylenium that is connected to LambdaTest
    py = Pylenium(py_config)

    # 4. Yield the driver so the test can use it, then quit() when the test is complete
    yield py
    py.quit()


@pytest.fixture
def page(py: Pylenium):
    return TodoPage(py).goto()


def test_check_first_item(page: TodoPage):
    checkbox = page.get_todo_by_name('First Item')
    checkbox.click()
    assert checkbox.should().be_checked()


def test_check_many_items(py: Pylenium, page: TodoPage):
    todos = page.get_all_todos()
    todo2, todo4 = todos[1], todos[3]
    todo2.click()
    todo4.click()
    assert py.contains('3 of 5 remaining')


def test_check_all_items(py: Pylenium, page: TodoPage):
    for todo in page.get_all_todos():
        todo.click()

    assert py.contains('0 of 5 remaining')


def test_add_new_item(py: Pylenium, page: TodoPage):
    page.add_todo('Finish the course')
    assert page.get_all_todos().should().have_length(6)
    assert py.contains('6 of 6 remaining')
