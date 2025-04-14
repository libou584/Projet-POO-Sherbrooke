from datetime import datetime
from models.DayOffApproval.DayOffApprovalStrategy import DayOffApprovalStrategy


class ApproveAllStrategy(DayOffApprovalStrategy):
    """
    Approve all day off requests.
    """
    def approve(self, employee_id: int, day: datetime) -> None:
        """
        Approve a day off request for the given employee.
        This method always approve the day off.
        """
        from models.Application import Application
        application = Application()
        application.repository_facade.approve_day_off(employee_id, day, -1)
        application.notify_observers("employee", employee_id, f"Your day off on {day} has been approved by the system.")