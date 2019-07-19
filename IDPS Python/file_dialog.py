# File Dialog for Run_CNMFe
import os
from tkinter import *
from tkinter import filedialog


def choose_file():
    project = Tk()
    project.filename = filedialog.askopenfilename(initialdir="/", title="Choose an IDPS Movie file",
                                                  filetypes=[("IDPS Files", "*.isxd")])
    file = project.filename
    isxd_file = os.path.basename(file)
    return str(isxd_file)


def choose_directory():
    project_directory = Tk()
    project_directory.directory = filedialog.askdirectory(title="Choose a Project Directory")
    return str(project_directory.directory)


def choose_data_folder():
    data_folder = Tk()
    data_folder.directory = filedialog.askdirectory(title="Choose an IDPS Project _data Folder")
    path = data_folder.directory
    folder = os.path.basename(path)
    return str(folder)


choose_directory()
choose_data_folder()
choose_file()
