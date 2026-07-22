from pylenium.driver import Pylenium


def test_google(py: Pylenium):
    py.visit('https://www.testmuai.com/selenium-playground/todo-app/')
    py.get('[id="sampletodotext"]').type('Pylenium-PyTest')
    py.get('[id="addbutton"]').submit()
    assert py.should().contain_title('Selenium Grid Online | Run Selenium Test On Cloud')
