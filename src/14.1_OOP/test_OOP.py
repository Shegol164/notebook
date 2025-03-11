import pytest

from OOP import Employee


@pytest.fixture()
def employee_ivan():
    return Employee("Ivan","Ivanov","50000")

def test_init(employee_ivan):
    assert employee_ivan.name == "Ivan"
    assert employee_ivan.surname == "Ivanov"
    assert employee_ivan.pay == "50000"
    assert employee_ivan.email == f"Ivan.Ivanov@mail.com"

def test_is_work(employee_ivan):
    assert employee_ivan.is_work == False
    employee_ivan.work()
    assert employee_ivan.is_work == True

def test_is_vacation(employee_ivan):
    assert employee_ivan.is_vacation == False
    employee_ivan.go_to_vacation()
    assert employee_ivan.is_vacation == True

def test_is_work_not_vacation(employee_ivan):
    assert employee_ivan.is_vacation == False
    employee_ivan.go_to_vacation()
    employee_ivan.work()

def test_is_work_not_work(employee_ivan):
    assert employee_ivan.is_work == False
    employee_ivan.work()
    employee_ivan.go_to_vacation()
