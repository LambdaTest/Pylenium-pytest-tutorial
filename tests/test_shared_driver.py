import pytest
from pylenium.driver import Pylenium
from pylenium.element import Element, Elements


class TodoPage:
    def __init__(self, py: Pylenium):
        self.py = py

    def goto(self) -> "TodoPage":
        self.py.visit("https://lambdatest.github.io/sample-todo-app/")
        return self

    def get_todo_by_name(self, name: str) -> Element:
        return self.py.getx(f"(//*[contains(text(),'{name}')])[2]").parent().get("input")

    def get_all_todos(self) -> Elements:
        return self.py.find("li[ng-repeat*='todo'] > input")

    def add_todo(self, name: str) -> "TodoPage":
        self.py.get("#sampletodotext").type(name)
        self.py.get("#addbutton").click()
        return self



@pytest.fixture
def page(py: Pylenium):
    return TodoPage(py).goto()


@pytest.mark.flaky(reruns=2, reruns_delay=3)
def test_check_first_item(page: TodoPage):
    checkbox = page.get_todo_by_name("Complete initial setup")
    checkbox.click()
    assert checkbox.should().be_checked()


@pytest.mark.flaky(reruns=2, reruns_delay=3)
def test_check_many_items(py: Pylenium, page: TodoPage):
    todos = page.get_all_todos()
    todo2, todo4 = todos[1], todos[3]
    todo2.click()
    todo4.click()
    assert py.contains("3 of 5 tasks remaining")


@pytest.mark.flaky(reruns=2, reruns_delay=3)
def test_check_all_items(py: Pylenium, page: TodoPage):
    for todo in page.get_all_todos():
        todo.click()
    assert py.contains("All tasks completed! Great work!")


@pytest.mark.flaky(reruns=2, reruns_delay=3)
def test_add_new_item(py: Pylenium, page: TodoPage):
    page.add_todo("Finish the course")
    assert page.get_all_todos().should().have_length(6)
    assert py.contains("6 of 6 tasks remaining")

