from datetime import datetime
from models.DayOffApproval.DayOffApprovalStrategy import DayOffApprovalStrategy


class RejectAllStrategy(DayOffApprovalStrategy):
    """
    Reject all day off requests.
    """
    def approve(self, employee_id: int, day: datetime) -> None:
        """
        Approve a day off request for the given employee.
        This method always reject the day off.
        """
        from models.Application import Application
        application = Application()
        application.repository_facade.reject_day_off(employee_id, day, -1)
        application.notify_observers("employee", employee_id, f"Votre demande de jour de congé le {day} a été rejetée par le système.")