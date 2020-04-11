import win32print

# printers = win32print.GetDefaultPrinter()
printers = win32print.EnumPrinters(2)

for p in printers:
    print(p[2])



default_printer = win32print.GetDefaultPrinter()
print('current: ' + default_printer)
# win32print.SetDefaultPrinter('Gprinter GP-1324D')
# default_printer = win32print.GetDefaultPrinter()
# print('new: ' + default_printer)
# p = win32print.OpenPrinter('Gprinter GP-1324D')
# job = win32print.StartDocPrinter(p, 1, ("test of raw data", None, "RAW"))
# win32print.StartPagePrinter(p)
# win32print.WritePrinter(p, "data to print".encode('utf-8'))
# win32print.EndPagePrinter(p)

import os, sys
import win32print

printer_name = win32print.GetDefaultPrinter()
#
# raw_data could equally be raw PCL/PS read from
#  some print-to-file operation
#
# if sys.version_info >= (3,):
#     raw_data = bytes("This is a test", "utf-8")
# else:
#     raw_data = "This is a test"
#
# hPrinter = win32print.OpenPrinter(printer_name)
# try:
#     hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, "RAW"))
#     try:
#         win32print.StartPagePrinter(hPrinter)
#         win32print.WritePrinter(hPrinter, raw_data)
#         win32print.EndPagePrinter(hPrinter)
#     finally:
#         win32print.EndDocPrinter(hPrinter)
# finally:
#     win32print.ClosePrinter(hPrinter)


import win32print
import win32ui
import win32con
import tempfile

INCH = 1440

hDC = win32ui.CreateDC()
hDC.CreatePrinterDC(win32print.GetDefaultPrinter())
hDC.StartDoc("Test doc")
hDC.StartPage()
hDC.SetMapMode(win32con.MM_TWIPS)
hDC.DrawText("TEST HELLO  WORLD! CORSS FIREWALL, WE TOUCH THE WORLD!",
             (0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
hDC.EndPage()
hDC.EndDoc()