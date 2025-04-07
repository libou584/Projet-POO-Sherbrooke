from abc import ABC
from datetime import datetime


class DayOffApprovalStrategy(ABC):
    """
    Abstract base class for day off approval strategies.
    """
    def approve(self, employee_id: int, day: datetime) -> None:
        """
        Approve a day off request for the given employee.
        This method should be implemented by subclasses.
        """
        pass