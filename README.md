# PDF-Manipulator
PDF Manipulator is a versatile Python project that allows users to merge PDFs, convert PDFs to text, and generate speech from text, offering options to adjust sound rate and volume for a personalized experience using two libraries, PyPDF2, and pyttsx3.

When the user selects the option to merge PDF files (presses 1), the program will prompt for the paths of the two PDF files that they want to merge. Next, a PdfFileMerger object is created as the merger. The input PDF files are appended to the union using the append method. Finally, the merged PDF file is written by calling the write method of the merger and providing the desired output file path. This completes the process of merging the PDF files.

When the user selects option 2, the program asks for the path of the PDF file to be converted. An empty string called text is initialized to store the extracted text. Using the PdfReader from PyPDF2, the program determines the number of pages in the PDF and iterates over each page, extracting the text and appending it to the text string. Finally, the accumulated text is printed as the output.

If the user selects option 3, the program prompts the user to input the desired text. The program initializes the text-to-speech functionality, allowing speech rate and volume customization. The provided text is then spoken using the say() function and the program waits until the speech is completed using runAndWait() before finishing the execution.

When the user selects option 4, the program prompts the user to provide the path of the PDF file they want to convert. The program utilizes PDF extraction methods to extract the content from the PDF and convert it into text. The extracted text is then passed to the text-to-speech functionality to generate speech output based on user preferences for speech rate and volume.

If the user selects an option more significant than 4, the program displays a message indicating that the input is out of range. This serves as a validation mechanism to inform the user that they have entered an invalid choice and ensures that the program executes only within the defined functionality range.
