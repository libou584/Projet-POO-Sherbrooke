from abc import ABC, abstractmethod
from models.Users.Employee import Employee


class ReportFactory(ABC):
    """
    Abstract Factory for generating reports.
    """

    @abstractmethod
    def create_report(self, employee_id: int):
        """
        Create a report of the specified type.
        """
        pass