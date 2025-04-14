from models.ReportGenerator.ReportFactory import ReportFactory
from models.Application import Application


class HTMLReportFactory(ReportFactory):
    """
    Concrete Factory for generating HTML reports.
    """

    def create_report(self, employee_id: int):
        """
        Create an HTML report for the given employee.
        """
        application = Application()
        employee = application.repository_facade.get_user_by_id(employee_id)
        # Here you would implement the logic to generate an HTML report
        # For demonstration purposes, we will just print a string
        print(f"Rapport HTML pour {employee.first_name} {employee.last_name}\nCette fonctionnalité n'est pas encore implémentée.")