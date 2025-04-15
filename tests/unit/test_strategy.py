from models.DayOffApproval.ApproveAllStrategy import ApproveAllStrategy

from models.DayOffApproval.ApprovalStrategyProvider import ApprovalStrategyProvider
from models.Application import Application
from models.Observers.EmployeeNotificationObserver import EmployeeNotificationObserver
from models.Users.Employee import Employee
import pytest
from models.DayOffApproval.HRToApproveStrategy import HRToApproveStategy
from models.DayOffApproval.ApproveAllStrategy import ApproveAllStrategy


def test_get_approval_strategy_hr_to_approve():
    strategy = ApprovalStrategyProvider.get_approval_strategy("HRToApprove")
    assert isinstance(strategy, HRToApproveStategy)

def test_get_approval_strategy_approve_all():
    strategy = ApprovalStrategyProvider.get_approval_strategy("ApproveAll")
    assert isinstance(strategy, ApproveAllStrategy)

def test_get_approval_strategy_invalid():
    with pytest.raises(ValueError):
        ApprovalStrategyProvider.get_approval_strategy("InvalidStrategy")

def test_notification_observers(mock_repository_facade):
    application = Application()
    while len(application.observers) > 0:
        application.remove_observer(application.observers[0])
    application.repository_facade = mock_repository_facade
    application.register_observer(EmployeeNotificationObserver(application))
    application.day_off_approval_strategy = ApproveAllStrategy()
    employee = Employee(0, "john", "doe", 25)
    application.approve_day_off(employee.id, "2023-10-01")
    assert len(application.observers) == 1
    assert isinstance(application.observers[0], EmployeeNotificationObserver)
    assert len(application.repository_facade.get_all_notifications()) == 1