from pylenium.driver import Pylenium


def search(py, query):
    py.visit('https://google.com')
    py.get('[name="q"]').type(query)
    py.get('[name="btnK"]').submit()
    return py.should().contain_title(query)


def test_google_search_in_chrome(py: Pylenium):
    target = {
        "platform": "Windows 10",
        "browserName": "Chrome",
        "version": "85",
        "resolution": "1280x1024"
    }
    py.config.driver.capabilities.update(target)
    assert search(py, 'puppies')


def test_google_search_in_firefox(py: Pylenium):
    target = {
        "platform": "Windows 10",
        "browserName": "Firefox",
        "version": "81",
        "resolution": "1280x1024"
    }
    py.config.driver.capabilities.update(target)
    assert search(py, 'puppies')
