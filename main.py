# Import Module
from tkinter import *
from functions import functions
import os
import logging

try:
    log_folder_dir= "C:/"
    log_folder_name = "PDF MERGER LOGS"
    path = os.path.join(log_folder_dir, log_folder_name)

    log_file_name = "PDF MERGER LOGS.log"
    logfilepath = os.path.join(path, log_file_name)

    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)

    logging.basicConfig(level=logging.DEBUG, force=True, format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S', filename=logfilepath, filemode='w')

    logging.info("log file created succesfully")
    print("log file created succesfully")

except Exception as Argument:
    print(Argument)

try:
    # create root window
    root = Tk()

    # root window title and dimension
    root.title("PDF tool")

    # Set geometry (width x height)
    root.geometry('600x600')

    logging.info("root window is created with title 'PDF tool' and dimension of '600x600' ")

except Exception as Argument:
    logging.error("error happend while creating root window. error messege: " + str(Argument))

try:
    #Creating a file Explorer label
    label_file_explorer = Label(root,
                            text = "PDF MERGER USING TKINTER",
                            width = 85, height= 4,
                            fg= "blue")
    label_file_explorer.grid(column = 1, row = 1)
    logging.info("label 'PDF MERGER USING TKINTER' is created")

except Exception as Argument:
    logging.error("error happend while creating Label. error messege: " + str(Argument))

try:
    #Creating a button to select folder
    button_input = Button(root,
                        text= "Select a folder and show all files",
                        command= functions.scanallpdf)
    button_input.grid(column = 1, row = 2)

    #Creating a button to merge pdf
    button_output = Button(root,
                     text = "merge all pdf from selected folder" ,
                     command= functions.mergedpdf)
    button_output.grid(column = 1,row = 3)

    #Creating a button to close program
    button_exit = Button(root,
                     text = "Exit",
                     command = exit)
    button_exit.grid(column = 1,row = 4)

    logging.info("All three buttons are created succesfully")

except Exception as Argument:
    logging.error("error happend while creating buttons. error messege: " + str(Argument))


# Let the window wait for any events
root.mainloop()
