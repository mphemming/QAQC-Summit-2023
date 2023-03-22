# %% -------------------------------------------------------------
# Packages

import xarray as xr
import numpy as np
import requests
import re

# %% -------------------------------------------------------------
# download and concatenate CTD profiles

# function to get file names
def get_thredds_filenames(link):
    # scrape thredds server
    res = requests.get(link)
    txt = res.text
    # identify file names
    start_file = []
    end_file = []
    files = []
    # get start and end locations of file names in text
    for m in re.finditer('IMOS_ANMN', txt):
        start_file.append(m.start())
    for m in re.finditer('.nc', txt):
        end_file.append(m.end())  
    # get file names
    for n_file in range(len(start_file)):
        files.append(txt[start_file[n_file]:end_file[n_file]])
    # Only use unique file names
    files = np.unique(files)
    locs = []
    dates = []
    for n in range(len(files)):
        locs.append(link.replace('catalog.html','') +  files[n])
        locs[n] = locs[n].replace('catalog','dodsC')
        f_und = []
        for m in re.finditer('_', files[n]):
            f_und.append(m.end()) 
        fus = f_und[2]
        
        yr = files[n][fus:fus+4]
        mn = files[n][fus+4:fus+6]
        dy = files[n][fus+6:fus+8]
        hr = files[n][fus+9:fus+11]
        mins = files[n][fus+11:fus+13] 
        dates.append(np.datetime64(yr + '-' + mn + '-' + dy + ' ' + hr + ':' + mins))
        
    return files, locs, dates

def AggregateProfiles(link,variable):
    files, locs, dates = get_thredds_filenames(link)
    CTD_data = []
    CTD_data_QC = []
    variables_in_file = []
    for l in locs:
        print('Loading:' + l)
        data = xr.open_dataset(l)
        CTD_data.append(data[variable])
        variables_in_file = list(data.variables)
        if (variable + '_quality_control') in variables_in_file:
            CTD_data_QC.append(data[variable + '_quality_control'])
    print('                ')
    print('Aggregating CTD profiles.')
    Profs = xr.concat(CTD_data,dim='DEPTH')
    Profs_QC = xr.concat(CTD_data_QC,dim='DEPTH')
    # merge QC
    AggProfs = {}
    AggProfs[variable] = Profs
    AggProfs[variable + '_quality_control'] = Profs_QC
    print('Done.')
    # Save data file (to complete later, need path input)
    # AggProfs.to_netCDF(filename)
    
    return AggProfs

# %% -------------------------------------------------------------
# Use the code to get concatenated data sets

# PH100
link = 'https://thredds.aodn.org.au/thredds/catalog/IMOS/ANMN/NSW/PH100/Biogeochem_profiles/catalog.html'
PH_AggProfs_TEMP = AggregateProfiles(link,'TEMP')
PH_AggProfs_PSAL = AggregateProfiles(link,'PSAL')


# MAI
link = 'https://thredds.aodn.org.au/thredds/catalog/IMOS/ANMN/NRS/NRSMAI/Biogeochem_profiles/catalog.html'
MAI_AggProfs_TEMP = AggregateProfiles(link,'TEMP')
MAI_AggProfs_PSAL = AggregateProfiles(link,'PSAL')

# %% -------------------------------------------------------------
# Notes

# profiles concatenated by 'DEPTH', not 'OBSERVATION' like LTSPs
# No concatenation of global attributes or instrument information etc
# There's no profile number variable
# Only tried for TEMP and PSAL at PH and MAI








