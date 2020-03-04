## How to use CNMF-E
### Once the python environemnt is set up
1. Open the Run_CNMFE.py file 
2. You will be asked to choose a Project Directory. This is the folder that contains the project data folder. 
3. You will then be asked to choose a data an IDPS Project_data Folder. This is the folder within the Project Directory that contains the processed calcium imaging recording data (with extension '.isxd'). Select this folder.
4. You will then be asked to choose an IDPS Movie file. Navigate back to the IDPS Project_data Folder that you selected in step 3. Choose the movie file that has already been run through the preprocess, spatial filter, and motion correction steps in the IDPS GUI. Select this file.
5. The file dialog will then ask you again to choose and IDPS Movie file. Repeat the stesp 4 and choose the same movie file.
6. The file dialog will then ask you to choose a Project Directory. Repeat the steps in 2 and choose the same folder.
7.The file dialog will then ask you to choose an IDPS Project_data folder. Repeat the steps in 3 and choose the same data folder. 
8. The code will run (it may take a while depending on the size of the movie file). Once finished running, a file dialog window will appear asking you to choose and output directory. Navigate back to the IDPS Project_data folder from step 3 and 7 and select the folder.

The CNMF-E processed movie file as well as the CNMF-E event detection file will now be available in the data folder. The CNMF-E movie file will end in 'CNMFE.isxd' and the event detection file will end in 'CNMFE-ED.isxd'. You can then import these files back into the IDPS GUI.
 
