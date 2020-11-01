# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

#This is defining the fuction that im going use
def write_to_thing():

    do_write_exspense = input('Do you wanna write all the exspenses for today')

    if do_write_exspense == 'yes':

        exspense = input('input the exspense:')

        sheet1.write(1, 0, exspense)

        wb.save('xlwt example.xls')

write_to_thing()
