from models.DayOffApproval.ApproveAllStrategy import ApproveAllStrategy
from models.DayOffApproval.HRToApproveStrategy import HRToApproveStategy


class ApprovalStrategyProvider:

    @staticmethod
    def get_approval_strategy(approval_type: str):
        if approval_type == "HRToApprove":
            return HRToApproveStategy()
        elif approval_type == "ApproveAll":
            return ApproveAllStrategy()
        else:
            raise ValueError(f"Unknown approval type: {approval_type}")