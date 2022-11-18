from pylenium.driver import Pylenium


def test_google(py: Pylenium):
    py.visit('https://lambdatest.github.io/sample-todo-app/')
    py.get('[id="sampletodotext"]').type('Pylenium-PyTest')
    py.get('[id="addbutton"]').submit()
    assert py.should().contain_title('lambdatest')
