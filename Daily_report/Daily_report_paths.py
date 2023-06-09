#!\\usr\\bin\\env python3
# -*- coding: utf-8 -*-

# Created on May 8 2023 by Michael Hemming (NSW-IMOS)

# What does this script do?

# o   
# o   

# Instructions:

# o   
# o   

# %% -----------------------------------------------------------------------------------------------
# Determine which computer this script is on

import os
if 'mphem' in os.getcwd():
    account = 'F:\\'
else:
    account = 'C:\\Users\\z3526971\\'

# %% -----------------------------------------------------------------------------------------------
# Import modules

import os
import Daily_report_setup as setup
import glob
import importlib

if hasattr(setup, 'CreationMode'):
    importlib.reload(setup) 

#------------------------------------------------------------
# Information 
#-------------

# These are modules required to get current path information

#------------------------------------------------------------

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# %% -----------------------------------------------------------------------------------------------
# Determine main paths
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

# get current directory
pwd_info = os.getcwd()
# depending on where working, create path
if ('home' in pwd_info) == 0:
    # working from Windows using mounted sci-maths-ocean
    starting_path = 'Z:\\home\\z3526971\\'
else:
    # Working from campus \\ ssh login
    z = pwd_info.find('z')
    zuser = pwd_info[z:z+8]
    starting_path = '\\home\\' + zuser
# remaining part of path
ending_path = 'sci-maths-ocean\\IMOS\\Moorings_Report\\Automatic_reporting\\'
ending_path_data = 'sci-maths-ocean\\IMOS\\DATA\\MOORINGS\\PROCESSED_2_5\\'
# check if missing '\\' at end of strings
if ('\\' in starting_path[-1]) == 0:
    starting_path = starting_path + '\\'
if ('\\' in ending_path[-1]) == 0:
    ending_path = ending_path + '\\'    
# complete path
main_path = starting_path + ending_path
main_path_data = starting_path + ending_path_data


# working directory
working_dir = ('C:\\Users\\' + account + '\\OneDrive - UNSW\\Work\\QC_reports\\')

# temporary directory
TEMPORARY_dir = 'C:\\Users\\' + account + '\\OneDrive - UNSW\\Work\\QC_reports\\TEMPORARY\\'

#------------------------------------------------------------
# Information 
#-------------
        
# Determine where script is being run from (MAC or server). 
# Does not work for windows for the time being. Gets
# the main path for folder containing code etc. and data

#------------------------------------------------------------

# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

# %% -----------------------------------------------------------------------------------------------
# netCDF files
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

# # Functions to choose correct paths to netCDF files
# #------------------------------------------------------------
# def ncdir_TEMP(site_name):
#     switcher = {
#             'BMP070': main_path_data + 'BMP070\\TEMPERATURE\\',
#             'BMP120': main_path_data + 'BMP120\\TEMPERATURE\\',
#             'CH050': main_path_data + 'CH050\\TEMPERATURE\\',
#             'CH070': main_path_data + 'CH070\\TEMPERATURE\\',
#             'CH100': main_path_data + 'CH100\\TEMPERATURE\\',
#             'PH100': main_path_data + 'PH100\\TEMPERATURE\\',
#             'SYD100': main_path_data + 'SYD100\\TEMPERATURE\\',
#             'SYD140': main_path_data + 'SYD140\\TEMPERATURE\\',
#             'ORS065': main_path_data + 'ORS065\\TEMPERATURE\\',
#             }

#     netCDF_TEMP_dir = switcher.get(site_name)
#     return netCDF_TEMP_dir
# # Functions to choose correct paths to netCDF files
# #------------------------------------------------------------
# def ncdir_SBE37(site_name):
#     switcher = {
#             'BMP070': main_path_data + 'BMP070\\SBE37\\',
#             'BMP120': main_path_data + 'BMP120\\SBE37\\',
#             'CH050': main_path_data + 'CH050\\SBE37\\',
#             'CH070': main_path_data + 'CH070\\SBE37\\',
#             'CH100': main_path_data + 'CH100\\SBE37\\',
#             'PH100': main_path_data + 'PH100\\SBE37\\',
#             'SYD100': main_path_data + 'SYD100\\SBE37\\',
#             'SYD140': main_path_data + 'SYD140\\SBE37\\',
#             'ORS065': main_path_data + 'ORS065\\SBE37\\',
#             }

#     netCDF_SBE37_dir = switcher.get(site_name)
#     return netCDF_SBE37_dir
# #------------------------------------------------------------
# def ncdir_CURR(site_name):
#     switcher = {
#             'BMP070': main_path_data + 'BMP070\\CURRENT\\',
#             'BMP120': main_path_data + 'BMP120\\CURRENT\\',
#             'CH050': main_path_data + 'CH050\\CURRENT\\',
#             'CH070': main_path_data + 'CH070\\CURRENT\\',
#             'CH100': main_path_data + 'CH100\\CURRENT\\',
#             'PH100': main_path_data + 'PH100\\CURRENT\\',
#             'SYD100': main_path_data + 'SYD100\\CURRENT\\',
#             'SYD140': main_path_data + 'SYD140\\CURRENT\\',
#             'ORS065': main_path_data + 'ORS065\\CURRENT\\',
#             }

#     netCDF_CURR_dir = switcher.get(site_name)
#     return netCDF_CURR_dir
# #------------------------------------------------------------
# def ncdir_BGC(site_name):
#     switcher = {
#             'BMP070': main_path_data + 'BMP070\\BGC\\',
#             'BMP120': main_path_data + 'BMP120\\BGC\\',
#             'CH050': main_path_data + 'CH050\\BGC\\',
#             'CH070': main_path_data + 'CH070\\BGC\\',
#             'CH100': main_path_data + 'CH100\\BGC\\',
#             'PH100': main_path_data + 'PH100\\BGC\\',
#             'SYD100': main_path_data + 'SYD100\\BGC\\',
#             'SYD140': main_path_data + 'SYD140\\BGC\\',
#             'ORS065': main_path_data + 'ORS065\\BGC\\',
#             }

#     netCDF_BGC_dir = switcher.get(site_name)
#     return netCDF_BGC_dir
# #------------------------------------------------------------
# def ncdir_CTD(site_name):
#     switcher = {
#             'BMP070': main_path_data + 'BMP070\\CTD\\',
#             'BMP120': main_path_data + 'BMP120\\CTD\\',
#             'CH050': main_path_data + 'CH050\\CTD\\',
#             'CH070': main_path_data + 'CH070\\CTD\\',
#             'CH100': main_path_data + 'CH100\\CTD\\',
#             'PH100': main_path_data + 'PH100\\CTD\\',
#             'SYD100': main_path_data + 'SYD100\\CTD\\',
#             'SYD140': main_path_data + 'SYD140\\CTD\\',
#             'ORS065': main_path_data + 'ORS065\\CTD\\',
#             }

#     netCDF_CTD_dir = switcher.get(site_name)
#     return netCDF_CTD_dir
# #------------------------------------------------------------
# # get netCDF paths
# netCDF_TEMP_dir = ncdir_TEMP(setup.site_name) 
# netCDF_SBE37_dir = ncdir_SBE37(setup.site_name) 
# netCDF_CURR_dir = ncdir_CURR(setup.site_name) 
# netCDF_BGC_dir = ncdir_BGC(setup.site_name) 
# netCDF_CTD_dir = ncdir_CTD(setup.site_name) 

#------------------------------------------------------------
# Information 
#-------------
        
# Select paths for site selected

#------------------------------------------------------------

# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

# %% -----------------------------------------------------------------------------------------------
# plots paths
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

plots_dir = ('F:\\OneDrive - UNSW\\Work\\QC_reports\\Basic_Template_Investigator\\Plots\\')

# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________


# %% -----------------------------------------------------------------------------------------------
# Report saving location
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

def savedir():
#    save_dir = main_path + 'Reports\\'
    save_dir = 'F:\\OneDrive - UNSW\\Work\\QC_reports\\Basic_Template_Investigator\\Reports\\'; # for testing
    return save_dir

# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

# %% -----------------------------------------------------------------------------------------------
# Double-check if paths include '\\' at end (unless a single file)


