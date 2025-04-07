from datetime import datetime
from models.DayOffApproval.DayOffApprovalStrategy import DayOffApprovalStrategy


class HRToApproveStategy(DayOffApprovalStrategy):
    """
    Leave requests to be approved by HR.
    """
    def approve(self, employee_id: int, day: datetime) -> None:
        """
        Approve a day off request for the given employee.
        This method always do nothing (not approving nor rejecting).
        """
        return None