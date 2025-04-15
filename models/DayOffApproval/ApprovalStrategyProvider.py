from models.DayOffApproval.ApproveAllStrategy import ApproveAllStrategy
from models.DayOffApproval.HRToApproveStrategy import HRToApproveStategy
from models.DayOffApproval.RejectAllStrategy import RejectAllStrategy


class ApprovalStrategyProvider:

    @staticmethod
    def get_approval_strategy(approval_type: str):
        if approval_type == "HRToApprove":
            return HRToApproveStategy()
        elif approval_type == "ApproveAll":
            return ApproveAllStrategy()
        elif approval_type == "RejectAll":
            return RejectAllStrategy()
        else:
            raise ValueError(f"Unknown approval type: {approval_type}")