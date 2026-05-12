from openpyxl import Workbook   

wb = Workbook()

sheet = wb.active
sheet["a1"]="name"
sheet["b1"]="role"

wb.save("sample.xlsx")