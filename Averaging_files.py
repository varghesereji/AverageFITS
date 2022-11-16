
from astropy.io import fits
import os

from extracting_header_values import extract_header
from grouping_files import grouping_files, list_of_files


def header_keys():
    '''
    Returns
    -------------------------
    List of header keys to group the files
    '''
    return ['SLIT', 'GRATING', 'OBJECT', 'CALMIR', 'ARGONL', 'NEONL', 'CONT2L']


def averaging_fits_files(keys=header_keys(),
                         input_path='/home/varghese/Desktop/DP2_TANSPEC/Data/\
                         P76',
                         output_path='/home/varghese/Desktop/DP2_TANSPEC/Data/\
                         Averaged_files',):
    '''
    Parameters
    --------------------------------
    keys: List of header keys which is to be used for grouping of files.
    input_path: Path of directory of files to average.
    output_path: The path to the directory which the output files should
    be saved.
    ================================
    Return
    Average files will be saved in the given path.
    -------------------------------
    '''
    files_list = list_of_files(input_path)
    grouped_files_list = grouping_files(keys, files_list)
    q = 0
    for groups in grouped_files_list:
        print('groups', groups)
        if groups == []:  # Exclude the case where the list is empty
            pass
        else:
            # Initialize variable to make the array of sum of data
            Data_candidate = None
            length = 0
            for files in groups:
                print(files)
                data = fits.getdata(files)
                file_header = extract_header(files)
                if Data_candidate is None:
                    Data_candidate = data
                else:
                    Data_candidate = Data_candidate + data
                length += 1
            mean_data = Data_candidate / length  # Averaging the data
            # Filename is generating by blinting the string Avg_ fame from
            # file header and q, which is just a number to show the
            # chronological order to avoid overwriting.
            filename = 'Avg_' + file_header['FNAME'] + '_' + str(q) + '.fits'
            filename_path = os.path.join(output_path,
                                         filename)
            file_header['FNAME'] = filename
            hdu = fits.PrimaryHDU(mean_data, file_header)
            hdul = fits.HDUList([hdu])
            hdul.writeto(filename_path, overwrite=True)
            print('saved_as', filename_path)
        q += 1
