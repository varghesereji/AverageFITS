# This code will group the files in a directory in the basis of keys in
# the header you are giving.

import os

from extracting_header_values import ordered_header_keys, file_header_key
from extracting_header_values import check_guider


def list_of_files(path='/home/varghese/Desktop/DP2_TANSPEC/Data/P76'):
    '''
    Parameter
    -------------------------------
    path: Path of the directory
    ==============================
    Returns
    ------------------------------
    dir_list: List of files with path in the directory
    '''
    dir_list = []
    for files in os.listdir(path):
        dir_list.append(os.path.join(path, files))
    return dir_list


def header_keys_SpecTANSPEC():
    '''
    Returns
    -------------------------
    List of header keys to group the files. Specific for TANSPEC Spectrograph.
    '''
    return ['SLIT', 'GRATING', 'OBJECT', 'CALMIR', 'ARGONL', 'NEONL', 'CONT2L']


def grouping_files(key=header_keys_SpecTANSPEC(), files_list=list_of_files()):
    '''
    Parameters
    ------------------------
    keys: List of header keys which is the basis of grouping.
    files_list: list of files to group
    ===============================
    Returns
    file_groups_list: Files are grouped in the basis of header keys made
    sepaeate groups. All groups added to list, file_groups_list.
    '''
    filtered_list = ordered_header_keys(key, files_list)
    no_of_groups = len(filtered_list)
    files_list = list_of_files()
    grouped_headers = []
    file_groups_list = []
    for n in range(no_of_groups):
        grouped_headers.append(filtered_list[n])
        grouped_files = []
        for files in files_list:
            if check_guider(files) is True:
                file_header = file_header_key(header_keys(), files)
                if file_header == grouped_headers[n]:
                    grouped_files.append(files)
        grouped_files.sort()
        file_groups_list.append(grouped_files)
    return file_groups_list


# End of the code.
