from models.ReportGenerator.ReportFactoryProvider import ReportFactoryProvider
from models.ReportGenerator.PDFReportFactory import PDFReportFactory
from models.ReportGenerator.HTMLReportFactory import HTMLReportFactory
import pytest


def test_get_report_factory_pdf():
    factory = ReportFactoryProvider.get_report_factory("pdf")
    assert isinstance(factory, PDFReportFactory)


def test_get_report_factory_html():
    factory = ReportFactoryProvider.get_report_factory("html")
    assert isinstance(factory, HTMLReportFactory)


def test_get_report_factory_invalid():
    with pytest.raises(ValueError):
        ReportFactoryProvider.get_report_factory("invalid")

