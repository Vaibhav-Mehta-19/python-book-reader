import pyttsx3
import PyPDF2

print("Enter the name of the pdf to open here: ")
bookname = input()
book  = open(bookname,'rb')
speaker = pyttsx3.init()
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
for num in range(15,pages):
	speaker.say((reader.getPage(num)).extractText())
	speaker.runAndWait()