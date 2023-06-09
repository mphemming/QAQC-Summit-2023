#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created on May 8 2023 by Michael Hemming (NSW-IMOS)

# %% -----------------------------------------------------------------------------------------------
# Import packages

# Python Packages
# QC report modules
import Daily_report_paths as paths
import Daily_report_setup as setup
import Daily_report_format as form

# %% -----------------------------------------------------------------------------------------------
# Create front cover

def create_cover(doc):

      #-----------------------------------------------
      # Front Cover
      #-----------------------------------------------
      doc.append(form.Command('begin','titlepage'))
      doc.append(form.Command('begin','center'))      
      doc.append(form.Command('LARGE'))
      doc.append(form.Command('textbf',('Daily report of results' +
             ' during RV Investigator Cruise <cruise identifier here>')))
      doc.append(form.Command('\\'))  
      doc.append(form.Command('\\')) 
      doc.append(form.Command('vfill'))
      doc.append(form.Command('vfill'))
      doc.append(form.Command('newline'))
      doc.append(form.Command('textbf',(setup.now)))
      doc.append(form.Command('vfill'))    
      file = paths.plots_dir + 'RVinvestigator.png'
      file = file.replace('\\','/')
      doc.append(form.StandAloneGraphic(file,'scale=0.55'))
      # doc.append(form.Command('vfill'))
      # doc.append(form.Command('vfill'))
      # file = paths.main_path + 'Cover_images\\NCRIS.png'
      # file = file.replace('\\','/')
      # doc.append(form.StandAloneGraphic(file,'scale=0.4'))   
      doc.append(form.Command('end','center'))          
      doc.append(form.Command('end','titlepage'))  
    