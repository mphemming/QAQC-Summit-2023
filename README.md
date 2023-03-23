# QAQC Summit 2023

 NSW-IMOS code that might be useful for the 2023 IMOS QAQC summit.
 
### aggregated_profiles.py
 
The main function to use is 'AggregateProfiles'. This function first uses 'get_thredds_filenames' to get a list of all CTD profiles in a directory on thredds. It then concatenates these files using xarray for a particular variable (and quality control variable). 

This code has only been tested for TEMP and PSAL. Profiles are concatendated using dim 'DEPTH', rather than 'OBSERVATION' as with other LTSPs. Global attributes are missing, as is an instrument index. Also no 'PROFILE' variable included, which may be useful to have. 

Example NetCDF file produced for PH100 TEMP:

```
{'TEMP': <xarray.DataArray 'TEMP' (DEPTH: 17975)>
 array([17.7441, 17.7176, 17.6956, ..., 14.1045, 14.1047, 14.1113],
       dtype=float32)
 Coordinates:
   * DEPTH      (DEPTH) float32 26.81 27.8 28.79 29.78 ... 110.2 111.2 112.2
     TIME       (DEPTH) datetime64[ns] 2011-08-29T00:03:40.396008448 ... 2020-...
     LATITUDE   (DEPTH) float64 -34.12 -34.12 -34.12 ... -34.12 -34.12 -34.12
     LONGITUDE  (DEPTH) float64 151.2 151.2 151.2 151.2 ... 151.2 151.2 151.2
 Attributes:
     standard_name:        sea_water_temperature
     long_name:            sea_water_temperature
     units:                Celsius
     valid_min:            -2.5
     valid_max:            40.0
     ancillary_variables:  TEMP_quality_control
     _ChunkSizes:          72,
 'TEMP_quality_control': <xarray.DataArray 'TEMP_quality_control' (DEPTH: 17975)>
 array([1., 1., 1., ..., 1., 1., 1.], dtype=float32)
 Coordinates:
   * DEPTH      (DEPTH) float32 26.81 27.8 28.79 29.78 ... 110.2 111.2 112.2
     TIME       (DEPTH) datetime64[ns] 2011-08-29T00:03:40.396008448 ... 2020-...
     LATITUDE   (DEPTH) float64 -34.12 -34.12 -34.12 ... -34.12 -34.12 -34.12
     LONGITUDE  (DEPTH) float64 151.2 151.2 151.2 151.2 ... 151.2 151.2 151.2
 Attributes:
     long_name:                           quality flag for sea_water_temperature
     standard_name:                       sea_water_temperature status_flag
     valid_min:                           0
     valid_max:                           9
     quality_control_set:                 1.0
     quality_control_conventions:         IMOS standard set using the IODE flags
     flag_values:                         [0 1 2 3 4 5 6 7 8 9]
     flag_meanings:                       No_QC_performed Good_data Probably_g...
     quality_control_global_conventions:  Argo reference table 2a (see http://...
     quality_control_global:              A
     _ChunkSizes:                         72}
```

### velocity_gridded_timeseries.py

This is very similar to the AODN code used to create other gridded products. 
It works the same way as other gridded products, except 'UCUR','VCUR','TIME', and 'DEPTH' variables are specifically selected. The groupby method is used similarly to grid the data every hour and linear interplation is used to get data at target depths. Longitude and latitude are added, and then interpolated 'UCUR' and 'VCUR' for each hour is then merged together into the same dataset. Global attributes are copied over from the hourly velocity LTSP, but the title, abstract and lineage is modified to reflect changes. Variable attributes are copied over from the hourly product, and then the gridded velocity product is saved. 

This code is slow, taking 30 - 60 mins to create a product depending on the length. 

### UpdateLTSP_example.py

This script first determines what's the latest deployment date on thredds and what's the end date of the LTSP stored locally. This is done using functions 'get_latest_deployment_date' which is used in 'determUpdate'. Functions 'updateAggregatedLTSP' / 'updateHourlyLTSP' / 'updateGriddedLTSP' are then used to update the LTSP rather than create from scratch. 

A new LTSP is created locally for the period that is new (between the end date of the LTSP stored locally and the end date of the latest deployment on thredds). This new recent LTSP is then concatenated with the previous longer LTSP. Two 'OBSERVATION' and 'INSTRUMENT' datasets are concatenated first, then these are merged together. Global attributes are copied over from the previous LTSP version, but some are modified to reflect changes. The filename is also updated with the latest deployment end date. The dataset is then saved as a netCDF file. 

If you want to see an example of how I am using this for the QAQC auto reporting, you can check out this script [here](https://github.com/mphemming/QAQC_report_code/blob/master/Code/QCreport_checkLTSPs.py)


