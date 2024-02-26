# import PyPDF2 for pdf to text conversion and pyttsx3 for text to speech conversion
import PyPDF2
import pyttsx3

# Define a function to merge two files and give merged output file
def merge_pdfs(input_files, output_file):
    merger = PyPDF2.PdfMerger()

    for file in input_files:
        with open(file, 'rb') as f:
            merger.append(f)

    with open(output_file, 'wb') as f:
        merger.write(f)

# Define a function to add up all the pages and make a combined text string
def pdf_to_text(pdf_path):
    # for combining all text
    text = ""
    # Open the PDF file in binary mode using the open function
    # and a with statement to ensure proper file handling. The file is assigned to the file variable.
    with open(pdf_path, 'rb') as file:
        # reading pdf file
        reader = PyPDF2.PdfReader(file)

        # counting number of pages in pdf
        num_pages = len(reader.pages)
        print(num_pages)

        # extracting pages one by one and adding text in text variable defined above
        for page in range(num_pages):
            page_obj = reader.pages[page]
            text += page_obj.extract_text()

    return text

def text_to_speech(text):
    # reading the text
    speak = pyttsx3.init()

    # custmize according to you

    print("You can change the speech according to you.")

    # Sets speed percent Can be more than 100
    a = int(input("Enter the speed percent of speech(can be more than 100):- "))
    speak.setProperty('rate', a)

    # Set volume 0-1
    b = int(input("Enter the volume of speech(0-10):- "))
    speak.setProperty('volume', b/10)

    print("Now reading....")

    speak.say(text)
    speak.runAndWait()

    print("Ended")

print("Enter 1 for merge two pdf")
print("Enter 2 for pdf to text conversion and print them")
print("Enter 3 for text to speech conversion")
print("Enter 4 for pdf to text and then text to speech conversion")

a = int(input("Enter index number according to your operation: "))
print("a = ",a)

if(a==1):
    x = input("Enter the path to the first PDF file: ")
    y = input("Enter the path to the second PDF file: ")

    input_files = [x, y]
    output_file = 'merged.pdf'  # Output file name
    merge_pdfs(input_files, output_file)
elif(a==2):
    x = input("Enter the path to the PDF file: ")
    text = pdf_to_text(x)
    print(text)
    print("Completed")
elif(a==3):
    x = input("Enter the text to convert into speech: ")
    text_to_speech(x)
elif(a==4):
    x = input("Enter the path to the PDF file: ")
    text = pdf_to_text(x)
    print(text)
    text_to_speech(text)
else:
    print("Your index is not in range([1,5]).")
