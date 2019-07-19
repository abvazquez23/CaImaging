import os
import isx
import isx.cnmfe
from file_dialog import choose_file, choose_directory, choose_data_folder

file = choose_file()
directory = choose_directory()
data_folder = choose_data_folder()


def cnmfe():
    # Process the data further than it already has been, to reduce memory consumption
    # Define the recording path to the cell set and event data
    data_dir = os.path.join(directory,
                            data_folder)

    # Pick out a movie from a particular session.
    mov_file = os.path.join(data_dir, file)

    # spatially downsample the movie 2X, making sure to set fix_defective_pixels to False because the movie has already
    # been preprocessed, and we don't want to median filter the movie a second time.
    pp_mov_file = os.path.join(data_dir, file)
    if not os.path.exists(pp_mov_file):
        isx.preprocess(mov_file, pp_mov_file, temporal_downsample_factor=1,
                       spatial_downsample_factor=2, fix_defective_pixels=False)

    # Set the output file names for the cell set and event set, deleting the files that already exist
    cellset_file = os.path.join(data_dir, file.replace("isxd", "") + '-CNMFE.isxd')
    events_file = os.path.join(data_dir, file.replace("isxd", "") + '-CNMFE-ED.isxd')

    # remove output files if they already exist
    if os.path.exists(cellset_file):
        os.remove(cellset_file)
    if os.path.exists(events_file):
        os.remove(events_file)

    # Run CNMFe (refer to IDPS manual isx.cnfme.run_cnfme() function for info about input values)
    isx.cnmfe.run_cnmfe(pp_mov_file, cellset_file, events_file, num_processes=1, K=20, rf=[25, 25], stride=6,
                        gSig=5, gSiz=10, min_pnr=5, min_corr=0.9, event_threshold=0.1)


cnmfe()
