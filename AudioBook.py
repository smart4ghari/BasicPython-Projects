import pyttsx3                          #This package is known as python text to speech
import PyPDF2                           #This package will help us to work with pdf files
book_name = open("PDF file name","rb") #Create a variable book_name to open the book
pdfReader = PyPDF2.PdfFileReader(book_name) #This will allow to read the pdffile (ie) book
page = pdfReader.getPage(page number)             #Mention the page from where you need to start
text_extract = page.extractText()       #This variable helps to extract the text from pdf
speaker = pyttsx3.init()                #Initializing the pyttsx3 module
speaker.say(text_extract)               #Get the output as speech
speaker.runAndWait()                    #runAndWait is a defa   ult command


#Note
"""Inside the "pdf file name" enter the pdf which you want to read and instead of page number denote the page number from where you want to begin"""
