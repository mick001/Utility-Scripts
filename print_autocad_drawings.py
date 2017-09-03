# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:20:04 2017

@author: Michy
@name: AutoCAD drawing printer BOT. 
@description:
    
    This program is a BOT that prints to pdf all the .dwg files in a given folder.
    Given a folder (data_wd) the program will try to print every .dwg file in that
    folder.
    
    IMPORTANT NOTE: This program works assuming that your AutoCAD installation is
    configured as mine. Which is a very bold assumption. The program works in the
    following manner:
        
        1) It gathers all the .dwg files in the given directory.
        2) For each file, it opens the file with the default program (which,
        is assumed to be AutoCAD) then CTRL + P is pressed to open the print menu.
        Then, the keys "m" and "i" are pressed in sequence, since this is enough
        to select the PDF printer in my case. Then "Enter" is pressed, the name
        of the output pdf file is entered, "enter" is pressed again, and then finally
        the drawing is closed using "CTRL + F4".
        
    Please make sure that this procedure applies to your machine as well. Otherwise
    make custom adjustments to the Pyautogui procedure as needed.
    
    The program outputs a log in a file named logfile.log (how original!). Example of
    a log file output is given below:

	INFO:DWG Printer bot V. 1.0:Program ran at 2017-09-03 21:35:09. Directory chosen: C:\Users\Michy\Desktop\autocad_tutorial
	INFO:DWG Printer bot V. 1.0:Printed Drawing2.dwg
	INFO:DWG Printer bot V. 1.0:Printed Drawing2_1.dwg
	INFO:DWG Printer bot V. 1.0:Printed Drawing3.dwg
	INFO:DWG Printer bot V. 1.0:Printed Drawing3_1.dwg
	INFO:DWG Printer bot V. 1.0:Program ended at 2017-09-03 21:36:14

@examples:
	Example and more details will be provided soon at www.firsttimeprogrammer.blogspot.com

"""

#-------------------------------------------------------------------------------
# Imports

import os
import sys
import time
import psutil
import logging
import pyautogui as pgui
from datetime import datetime

VERSION = '1.0'

#-------------------------------------------------------------------------------
# Functions

def extract_selected_format(directory_path, file_extension='dwg'):
    
    # This function extracts all the files of the selected format from the
    # directory specified in the variable data_wd. Format is recognized through
    # the extension.
    # 
    # Arguments:
    #  directory_path - string - path from where to extract files.
    #  file_extension - string - extension of the file. Example: 'dwg'
    # 
    # Returns: List of complete path to each file.
    # 
    
    files = os.listdir(directory_path)
    files = [file for file in files if file.split('.')[1] == file_extension]
    files = [os.path.join(directory_path, file) for file in files]
    return files
        
def check_program_running(p_name):
    
    # Checks if the program p_name is currently running.
    #
    # Arguments:
    #   p_name - string - name of the program. Example: 'acad.exe'
    #
    # Returns: True if the program is running, False otherwise.
    #
    
    processes = [psutil.Process(p) for p in psutil.pids()]
    processes = [p.name().lower() for p in processes]
    if p_name in processes:
        return True
    else:
        return False
    
def check_file_exist(directory_path ,file_name):
    
    # Checks if the file file_name exists
    # 
    # Arguments:
    #   directory_path - string - directory where to check.
    #   file_name - string - name of the file to be checked.
    #
    # Returns: True if it exists, False otherwise
    #
    
    files = os.listdir(directory_path)
    printed = file_name in files
    return printed

def print_file_pdf(file_path, directory_path, logger):
    
    # Prints to pdf all the dwg files in the path specified
    #
    # Arguments:
    #   file_path - string - path containing the dwg files.
    #   directory_path - string - directory where the file is.
    #   logger - a logger.
    # 
    #   Returns: exit_status - int - 1 if Critical error occurred, 0 otherwise
    # 
    #
    
    file_name = file_path.split("\\")[-1]                        # Get name of the file
    file_name_pdf = file_name.replace("dwg", "pdf")              # Get name of the output file
    is_printed = check_file_exist(directory_path, file_name_pdf) # Check if already existing
    exit_status = 0                                              # 1 only if critical error occurs
    
    if not is_printed:    
        
        program_runs = check_program_running("acad.exe")
        
        # Opens file with default program (Autocad for .dwg files).
        # If opening fails, returns 1, else 0.
        exit_status = os.system(" ".join(["start", file_path]))
        
        if exit_status == 0:
            if program_runs:
                time.sleep(5)
            else:
                # Autocad is slow to start up if it is not already running.
                time.sleep(30)
            
            print(" ".join(["Now printing file", file_name]))
            
            # Starting printing sequence
            pgui.hotkey("ctrl","p")
            pgui.typewrite("mi")
            pgui.keyDown("enter")
            pgui.keyUp("enter")
            time.sleep(1)
            pgui.typewrite(file_name_pdf)
            pgui.keyDown("enter")
            pgui.keyUp("enter")
            time.sleep(3)
            # Closing current drawing
            pgui.hotkey("ctrl", "F4")
            pgui.keyDown("n")
            pgui.keyUp("n")
        
            is_printed = check_file_exist(directory_path, file_name_pdf)
            if is_printed:
                logger.log(logging.INFO, " ".join(["Printed", file_name]))
            else:
                logger.log(logging.CRITICAL, " ".join(["NOT Printed", file_name]))
                exit_status = 1
        else:
            logger.log(logging.ERROR, "".join(["Could not open ", file_name]))
            logger.log(logging.ERROR, " ".join(["NOT Printed", file_name]))
    else:
        logger.log(logging.INFO, " ".join(["Already printed", file_name]))
    
    time.sleep(1)
    
    return exit_status

def handle_critical_errors(error_count, check_at_count=2):
    
    # Two or more critical errors may indicate a severe malfunctioning in the 
    # program. This function displays a confirmation box asking the user if
    # they want to continue or stop the program after check_at_count critical
    # errors occurred.
    #
    # Arguments:
    #   error_count - string - count of the critical errors.
    #   check_at_count - int - check after check_at_count critical errors occurred.
    # 
    #   Returns: void
    # 
    if error_count >= check_at_count:
        value = pgui.confirm("""2 or more critical errors have occurred.
                             Would you like to continue (click "ok")
                             or cancel?""")
        if value == 'Cancel':
            sys.exit()

#-------------------------------------------------------------------------------
# Main

if __name__ == '__main__':
    
    # Setting input data directory
    data_wd = "C:\\Users\\Michy\\Desktop\\autocad_tutorial"
    full_file_path = extract_selected_format(data_wd)
    print("\nFollowing files will be printed: {}".format([full_file_path]))
    
    pgui.PAUSE = 0.5
    time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    error_count = 0
    logging.basicConfig(filename = 'logfile.log', level=logging.DEBUG)
    logger = logging.getLogger('DWG Printer bot V. {}'.format(VERSION))
    logger.log(logging.INFO,
               "Program ran at {}. Directory chosen: {}".format(time_stamp, data_wd))

    # Start printing
    
    for file in full_file_path:
        try:
            error_count += print_file_pdf(file, data_wd, logger)
            print("Exiting current printing call...\n")
            handle_critical_errors(error_count, 2)
        except Exception as e:
            print(str(e))
    
    final_time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.log(logging.INFO, "Program ended at {}\n\n".format(final_time_stamp))
    pgui.alert("Job ended!")
    
