from tkinter import *

#to import filedialog module
from tkinter import filedialog

#importing os module
import os

#importing PdfFileMerger
from PyPDF2 import PdfFileMerger, PdfFileReader

import logging

list_of_files = []

#creating function to open file explorer window to select folder
def selectDIR():
    try:
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        logging.info(folder_selected+" is selected by user to merge PDF")
    except Exception as Argument:
        logging.error("error happend while selecting pdf folder: " + str(Argument))
    # change label contents
    label_file_explorer = Label(root)
    label_file_explorer.configure(text="Folder selcted:" + folder_selected)
    global inputfolder
    inputfolder = str(folder_selected)
    return folder_selected


#Creating function to scan all pdf files from selected folder
def scanallpdf():
    try:
        logging.info("user has pressed 'Select a folder and show all files' button")
        dir = selectDIR()
        for root, dirs, files in os.walk(dir):
            for filename in files:
                list_of_files.append(filename)
        logging.info("all files have been scaned and selected for futher operations")


        # Creating the root window
        root = Tk()
        # Creating a Listbox and attaching it to root window
        listbox = Listbox(root)

        # Adding Listbox to the left side of root window
        listbox.pack(side=LEFT, fill=BOTH)
        listbox.config(width=100, height=20)


        # Creating a Scrollbar and attaching it to root window
        scrollbar = Scrollbar(root)


        # Adding Scrollbar to the right side of root window
        scrollbar.pack(side=RIGHT, fill=BOTH)


        # Insert elements into the listbox
        for values in list_of_files:
            listbox.insert(END, values)

        # Attaching Listbox to Scrollbar Since we need to have a vertical scroll we use yscrollcommand
        listbox.config(yscrollcommand=scrollbar.set)

        # setting scrollbar command parameter to listbox.yview method its yview because we need to have a vertical view
        scrollbar.config(command=listbox.yview)
        logging.info("scrollable list containing all files from folder is created")

    except Exception as Argument:
        logging.error("error happend while creating list of all files. error messege: " + str(Argument))




#Creating fuction which will mearge all pdf files from selected folder and create new pdf called merged inside
#dir called mergedpdf which will be created inside selected folder.
#If it is already exist, it will be deleted and created new one again.


def mergedpdf():
    try:
        logging.info("'merge all pdf from selected folder' button is pressed by user")
        root = Tk()
        out = inputfolder
        merger = PdfFileMerger()
        pdffiles = []
        for filename in os.listdir(out):
            F = os.path.join(out, filename)
            if filename.endswith(".pdf") and os.stat(F).st_size != 0:
                pdffiles.append(filename)
                merger.append(PdfFileReader(open(F, 'rb')))
        logging.info(f"All PDF files selected from list are: {pdffiles}")
        logging.info("All PDF files are merged into one")

    except Exception as Argument:
        logging.error("error happend while merging PDF. error messege: " + str(Argument))


    try:
        folder_dir = out
        folder_name = "mergedpdf"
        path = os.path.join(folder_dir, folder_name)

        pdf_file_name = "merged.pdf"
        pdffilepath = os.path.join(path, pdf_file_name)

        if os.path.exists(path):
            logging.info(f"dir {path} is already there")
        else:
            os.mkdir(path)
            logging.info(f"dir {path} is created")

    except Exception as Argument:
        logging.error(f"error happend while creating dir {path}. error messege: " + str(Argument))

    try:
        if os.path.isfile(pdffilepath):
            os.remove(pdffilepath)
            logging.info(f"previous merged PDF file 'merged.pdf' is deleted from location: {pdffilepath}")
            merger.write(path + "\merged.pdf")
            logging.info(f"new merged PDF file 'merged.pdf' is created in location: {pdffilepath}")


        else:
            merger.write(path + "\merged.pdf")
            logging.info(f"merged PDF file 'merged.pdf' is created in location: {pdffilepath}")

    except Exception as Argument:
        logging.error(f"error happend while creating 'merged.pdf'. error messege: " + str(Argument))

    label_file_explorer2 = Label(root,
                                text="merged PDF saved successfully at:" + pdffilepath ,
                                width=85, height=4,
                                fg="blue")
    label_file_explorer2.grid(column=1, row= 5)
    logging.info(f"merged PDF saved successfully at: {pdffilepath}")



