import openpyxl
wb = openpyxl.load_workbook('store_original.xlsx')
sheet = wb['Products']
print(sheet)
