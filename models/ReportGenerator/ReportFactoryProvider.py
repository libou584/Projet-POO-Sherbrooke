from models.ReportGenerator.PDFReportFactory import PDFReportFactory
from models.ReportGenerator.HTMLReportFactory import HTMLReportFactory


class ReportFactoryProvider:

    @staticmethod
    def get_report_factory(report_type: str):
        """
        Factory method to get the appropriate report factory based on the report type.
        """
        if report_type == "pdf":
            return PDFReportFactory()
        elif report_type == "html":
            return HTMLReportFactory()
        else:
            raise ValueError(f"Unknown report type: {report_type}")