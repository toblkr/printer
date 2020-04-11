from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

import html
import tempfile
import win32api
import win32print

source_file_name = "temp.txt"
pdf_file_name = tempfile.mktemp(".pdf")

styles = getSampleStyleSheet()
h1 = styles["h1"]
normal = styles["Normal"]

doc = SimpleDocTemplate(pdf_file_name)
#
# reportlab expects to see XML-compliant
#  data; need to escape ampersands &c.
#
text = html.escape(open (source_file_name).read ()).splitlines ()
default_printer = win32print.GetDefaultPrinter()
print(default_printer)

#
# Take the first line of the document as a
#  header; the rest are treated as body text.
#
story = [Paragraph(text[0], h1)]
for line in text[1:]:
    story.append(Paragraph (line, normal))
    story.append(Spacer(1, 0.2 * inch))

doc.build (story)
win32api.ShellExecute (0, "printto", pdf_file_name, None, ".", 0)