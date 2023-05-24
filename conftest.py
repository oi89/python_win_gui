import pytest
import os
from comtypes.client import CreateObject

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Users\\olegi\\Documents\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


# pytest hook for parametrization (called when collect a test method)
def pytest_generate_tests(metafunc):
    # go through all parameters of test method
    for param in metafunc.fixturenames:
        if param.startswith("excel_"):
            # load test data from file removing "excel_" (for example, "excel_groups" -> "groups")
            test_data = load_from_excel(param[6:])
            # add parametrization to test method
            metafunc.parametrize(param, test_data, ids=[str(x) for x in test_data])


def load_from_excel(filename):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{filename}.xlsx")
    xl = CreateObject("Excel.Application")
    wb = xl.Workbooks.Open(file)
    worksheet = wb.Worksheets[1]
    data_list = []
    for row in range(1, 6):
        data = worksheet.Cells[row, 1].Value()
        data_list.append(data)

    for wb in xl.Workbooks:
        wb.Close(0)
    xl.Quit()

    return data_list
