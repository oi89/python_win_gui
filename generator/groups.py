from comtypes.client import CreateObject
import os


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = "data/groups.xlsx"

# create excel instance
xl = CreateObject("Excel.Application")
# make it visible
# xl.Visible = 1
# add a new sheet to excel
wb = xl.Workbooks.Add()

for i in range(10):
    xl.Range[f"A{i+1}"].Value[()] = f"group{i}"

wb.SaveAs(os.path.join(project_dir, filename))
xl.Quit()
