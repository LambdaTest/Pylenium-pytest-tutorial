import pytest
from pylenium.driver import Pylenium


def search(py, query):
    py.visit('https://google.com')
    py.get('[name="q"]').type(query)
    py.get('[name="btnK"]').submit()
    return py.should().contain_title(query)


browser_targets = [
    {
        "platform": "Windows 10",
        "browserName": "Chrome",
        "version": "85",
        "resolution": "1280x1024"
    },
    {
        "platform": "Windows 10",
        "browserName": "Firefox",
        "version": "81",
        "resolution": "1280x1024"
    }
]


@pytest.mark.parametrize('browser', browser_targets)
def test_google_search(py: Pylenium, browser):
    py.config.driver.capabilities.update(browser)
    assert search(py, 'puppies')
