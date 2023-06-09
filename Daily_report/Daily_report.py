
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created on May 8 2023 by Michael Hemming (NSW-IMOS)

# What does this script do?

# o   
# o   
# o   

# Instructions:

# o   
# o   

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# %% -----------------------------------------------------------------------------------------------
# Determine which computer this script is on

# import os
# if 'mphem' in os.getcwd():
#     account = 'F:\\'
# else:
#     account = 'C:\\Users\\z3526971\\'
    
account = 'F:\\'

# %% -----------------------------------------------------------------------------------------------
# Import modules

# set path of QC code
import os
import glob
import warnings
import importlib
os.chdir(account + '\\OneDrive - UNSW\\Work\\QC_reports\\Basic_Template_Investigator')
import runpy

# %% -----------------------------------------------------------------------------------------------
# import remaining modules

# QCreport modules
import Daily_report_setup as setup
import Daily_report_format as form
import Daily_report_paths as paths
import Daily_report_cover as cover

#------------------------------------------------------------
# Information 
#-------------

# These are the QC report modules required to run 
# this script. The QCreport modules need to be in 
# the same folder as this script.

#------------------------------------------------------------

print('Modules loaded')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# %% -----------------------------------------------------------------------------------------------
# Determine Paths

# obtain paths 
saving_dir = paths.savedir()

#------------------------------------------------------------
# Information 
#-------------

# These are the paths required to run this script, obtained
# from module QCreport_paths.py. These must be altered to 
# the correct paths before running the script. Refer to 
# script QCreport_paths.py to do this.

#------------------------------------------------------------

print('Paths loaded')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# %% -----------------------------------------------------------------------------------------------
# Create document and set Format

# call function to format PDF document
geometry_options = {"tmargin": "2cm", "lmargin": "2cm"}
doc = form.Document(geometry_options=geometry_options,
                    font_size='large')
doc.append(form.Command('fontsize', arguments = ['18', '16']))
# set TOC depth to 4
doc.preamble.append(form.Command('setcounter', arguments=['tocdepth', '4']))

# Latex packages
doc.packages.append(form.Package('rotating')) # for rotating toolbox plots
doc.packages.append(form.Package('lmodern')) # change font to 'palatino'
doc.packages.append(form.Package('sectsty'))
doc.packages.append(form.Package('titlesec','compact, big'))
doc.packages.append(form.Package('placeins','section')) # ensures plots stay in correct section, and don't float around
doc.packages.append(form.Package('graphicx')) # for front cover images
doc.packages.append(form.Package('hyperref')) # for opendap links
doc.packages.append(form.Package('morefloats')) # To allow for more floats (graphics/plots) in the report
# maxdeadcycles is a LaTeX parameter that specifies the maximum number of consecutive 
# iterations LaTeX should try to place a float before it gives up and moves it to the end 
# of the document. 
doc.preamble.append(form.Command('usepackage', 'placeins'))
# doc.preamble.append(form.Command('AtBeginDocument', '\\newcommand{\\myMaxDeadCycles}{200}'))
# doc.append(form.Command('FloatBarrier', options='[\\myMaxDeadCycles]'))

doc.preamble.append(form.NoEscape(r'\usepackage{endfloat}'))
doc.preamble.append(form.NoEscape(r'\renewcommand{\efloatseparator}{\mbox{}}'))

# doc.packages.append(form.Package('hyperref','[colorlinks=false]')) # for opendap links
# doc.packages.append(form.NoEscape(r'\usepackage[bgcolor=transparent]{minted}'))# to remove colored boxes
# doc.packages.append(form.NoEscape(r'\usepackage[colorlinks=false]{hyperref}'))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# %% -----------------------------------------------------------------------------------------------
# --------------------------------------------
# Front Cover
# --------------------------------------------

# Add content
cover.create_cover(doc)

print('Front Cover Created')

# %% -----------------------------------------------------------------------------------------------
# Create Table of Contents

# doc.append(form.Command('newpage'))
doc.append(form.Command('tableofcontents'))

print('Table of Contents added')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# %% -----------------------------------------------------------------------------------------------
# --------------------------------------------
# Create Sections
# --------------------------------------------

# doc.append(form.Command('newpage'))

with doc.create(form.Section('Results')):

    # example table
    with doc.create(form.Tabular('|l|l|')) as table:
        table.add_hline()
        table.add_row(('a', '1'))
        table.add_hline()
        table.add_row(('b','2'))
        table.add_hline()
        table.add_row(('c','3'))
        table.add_hline()
        
    # Add plot
    file = (paths.plots_dir + 'TEMP_BMP070_1711.png')
    with doc.create(form.Figure(position='htbp')) as pic:
        pic.add_image(file, 
                      width=form.NoEscape(r'0.65\linewidth'))
        pic.add_caption('This caption explains the plot.')  
     
    # Add subsections
    with doc.create(form.Subsection('subsection')):
        doc.append('This is a new subsection') 

print('Sections added')


# %% -----------------------------------------------------------------------------------------------
# --------------------------------------------
# Section: Appendix
# --------------------------------------------

# with doc.create(form.Appendix()):
#     with doc.create(form.Section('Appendix: Ocean Current Images')):
#         Addp.addOCplots(doc)    
#     with doc.create(form.Section('Appendix: Deployment Photographs')):
#         DepPhoto.include_photos(depphoto_dir,doc)
        
# print('Section added: ''Appendix''')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# %% -----------------------------------------------------------------------------------------------
# Save report

print('Saving report in: ' + saving_dir)

filename = (saving_dir + setup.site_name + '_' + setup.deployment_file_date_identifier + 
            '_QC_report')
# First time to create the TOC file
try:
    # try/except bypasses the non-terminal CalledProcessError
    doc.generate_pdf(filename,compiler='pdflatex')
except:
    # check file was created, if not create warning
    check = os.path.exists(filename + '.pdf')
    if check == False:
        warnings.warn('Warning!! file: ' + filename + '.pdf was not created. Investigation required.')
    pass
# second time to include the TOCs
try:
    # try/except bypasses the non-terminal CalledProcessError
    doc.generate_pdf(filename,compiler='pdflatex')
except:
    pass
doc.generate_tex(filename)
print('Report saved.')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# %% -----------------------------------------------------------------------------------------------
# tidy-up (remove unnecessary files in directory)

# os.chdir(saving_dir)
# aux_files = glob.glob(saving_dir + '*.aux')
# toc_files = glob.glob(saving_dir + '*.toc')
# out_files = glob.glob(saving_dir + '*.out')
# log_files = glob.glob(saving_dir + '*.log')
# tex_files = glob.glob(saving_dir + '*.tex')

# # remove all but PDFs
# for n in range(len(aux_files)):
#     os.remove(aux_files[n])
# for n in range(len(toc_files)):
#     os.remove(toc_files[n])    
# for n in range(len(out_files)):
#     os.remove(out_files[n])      
# for n in range(len(log_files)):
#     os.remove(log_files[n])      
# for n in range(len(tex_files)):
#     os.remove(tex_files[n])      

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
