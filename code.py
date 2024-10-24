
import os
from PyPDF2 import PdfFileMerger
data=os.listdir()
merger=pdfFileMerger()
for file in pdf:
   if file.endswith(".pdf"):
      merger.append(file)
merger.write("output.pdf")
merger.close()
