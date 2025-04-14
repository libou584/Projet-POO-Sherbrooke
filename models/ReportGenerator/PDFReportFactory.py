from models.ReportGenerator.ReportFactory import ReportFactory
from models.Application import Application


class PDFReportFactory(ReportFactory):
    """
    Concrete Factory for generating PDF reports.
    """

    def create_report(self, employee_id: int):
        """
        Create a PDF report for the given employee.
        """
        application = Application()
        employee = application.repository_facade.get_user_by_id(employee_id)
        # Here you would implement the logic to generate a PDF report
        # For demonstration purposes, we will just print a string
        print(f"Rapport PDF pour {employee.first_name} {employee.last_name}\nCette fonctionnalité n'est pas encore implémentée.")