import win32ui
import win32con
# X from the left margin, Y from top margin
# both in pixels
X=100; Y=30
multi_line_string = 'sadasd d asdfdas  herl'.split()
#heigt 字体大小
fontdata = { 'name':'Arial', 'italic':True, 'weight':win32con.FW_NORMAL}
hDC = win32ui.CreateDC()
hDC.CreatePrinterDC ('Gprinter GP-1324D')
font = win32ui.CreateFont(fontdata);
hDC.SelectObject(font)
hDC.StartDoc ('alex')
hDC.StartPage ()
for line in multi_line_string:
     hDC.TextOut(X,Y,line)
     Y += 100
hDC.EndPage ()
hDC.EndDoc ()