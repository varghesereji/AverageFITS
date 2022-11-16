# This code will return the list of elements in header that you needed
from astropy.io import fits


def extrat_fits(file_name):
    '''
    Parameters
    ---------------------
    file_name: Name of the file which need to extract.
    ============================================================
    Return
    ---------------------
    Data_array : Array that extracted from file_name.
    '''
    Data_array = fits.getdata(file_name)
    return Data_array


def extract_header(filename):
    '''
    Parameters
    -----------------------------------------
    filename: The file which you want to get the header
    ===================================================
    Return
    -----------------------------------------
    header: Header of input file
    '''
    hdul = fits.open(filename)
    header = hdul[0].header
    return header


def check_guider(filename):
    '''
    Parameters
    -----------------------------------------
    filename: String. Name and path of file.
    ========================================
    return: If the file is a guider image, return False. Else, true.
    It is checking by number of pixels. Spectrograph have 2048 pixels.
    '''
    file_header = extract_header(filename)
    if file_header['NAXIS1'] == 2048 and file_header['NAXIS2'] == 2048:
        return True
    else:
        return False


def remove_repeated_values(candidate_list):
    '''
    Parameters
    ----------------------------------------
    candidate_list: List to remove the repeated elements
    ====================================================
    Return
    ----------------------------------------
    filtered_list: List which repeated elements removed from candidate_list
    '''
    filtered_list = []
    for cand in candidate_list:
        if cand in filtered_list:
            pass
        else:
            filtered_list.append(cand)
    return filtered_list


def file_header_key(keys, filename):
    keys_dict = {}
    header = extract_header(filename)
    for key in keys:
        keys_dict[key] = header[key]
    return keys_dict


def ordered_header_keys(keys, file_list):
    '''
    Parameters
    -------------------------------------------
    keys: Keys in header that you wanted
    file_list: list of files with path
    =================================================
    Return
    -------------------------------------------
    filtered_list: List of dictionaries with required values and avoided
                   repetation of elements
    '''
    trimmed_list = []
    for files in file_list:
        keys_dict = file_header_key(keys, files)
        trimmed_list.append(keys_dict)
    filtered_list = remove_repeated_values(trimmed_list)
    return filtered_list


# End of the code.
