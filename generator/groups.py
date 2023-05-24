import random
from comtypes.client import CreateObject
import os
import string


def random_string(prefix, maxlen):
    # connect letters, numbers and space
    # to get more spaces in result string, multiply " " to 10 times
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = "data/groups.xlsx"

# create excel instance
xl = CreateObject("Excel.Application")
# make it visible
# xl.Visible = True
# add a new workbook to excel
wb = xl.Workbooks.Add()

for i in range(5):
    xl.Range[f"A{i + 1}"].Value[()] = random_string("g", 9)

wb.SaveAs(os.path.join(project_dir, filename))

for wb in xl.Workbooks:
    wb.Close(0)
xl.Quit()
