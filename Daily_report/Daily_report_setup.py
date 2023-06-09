# -*- coding: utf-8 -*-

# Created on May 8 2023 by Michael Hemming (NSW-IMOS)

# %% -----------------------------------------------------------------------------------------------
# Import packages

# Python Packages
import datetime

# %% -----------------------------------------------------------------------------------------------
# Choose site, deployment, add name of report maker 
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

# site_name = 'BMP120'
# deployment = ''
# # deployment_file_date_identifier = '2209'
# name_of_reportmaker = 'NSW-IMOS'

# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________


# %% -----------------------------------------------------------------------------------------------
# Add Comments to Report 
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

# QCcomment = 'Automatic, Manual'
# # options: 'None','Automatic', 'Manual' (can be more than one choice e.g. 'Automatic, Manual')
# Expert_QC = 'Yes, see comments'
# # options: 'yes' or 'no'
# Fieldwork_issues = 'None'
# # default: 'None', if issues add text here
# Sensor_damage = 'None'
# # default: 'None', if damage add text here
# Lost_equipment = 'None'
# # default: 'None', if lost equipment add text here
# Biofouling = 'Moderate, see photographs'
# # options: 'None', 'Some', 'Moderate', 'Substantial', 'see photographs' (can be more than one choice e.g. 'Moderate, see photographs')
# Other_issues = 'None'
# # default: 'None', if other issues add text here

# Keep information above short (no more than 4 words). If there
# is a neeed to add more information, add this in the 'comments' string below  


# comments =  'Post deployment processing of the data identified significant pressure drift in the top PT logger ' + \
#             '(PT8 - Nominally 12m depth, 62m above the bottom). Closer inspection indicates a 0.24m ' + \
#             'offset between PT8 (0.117m) and PT7 (0.357m - similar with the other PT sensors) ' + \
#             'prior to the instruments being deployed. It also indicates that once deployed, PT7 (21.29m) and PT8 (14.70m) are ' + \
#             'actually only separated by 6.59m not the nominal 8m. Inspection of the mooring line indicates that some shrinkage has ' + \
#             'occurred and that the loggers were separated by 7m (all other logger positions confirmed to be within spec). Deployment ' + \
#             'logs and metadata have been amended accordingly. The pressure data were corrected by ....'

# comments = 'no comments.'

# default: 'None', if comments add text here   
# tips: copy & paste might not work - only use characters in 'latin-q' codec
# e.g. commas copied over from somewhere else may be different to commas in latin-1
# use '' instead       

#------------------------------------------------------------
# Information 
#-------------
        
# Information added here will be included in the introduction 
# comments at the start of the deployment report

#------------------------------------------------------------               
            
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

# %% -----------------------------------------------------------------------------------------------
# get date of document creation for cover

now = datetime.date.today().strftime("%B %d, %Y")
now_year = datetime.date.today().strftime("%Y")

# __________________________________________________________________________________________________
# __________________________________________________________________________________________________
# __________________________________________________________________________________________________

