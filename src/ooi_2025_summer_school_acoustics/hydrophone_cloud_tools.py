"""
Tools for openning and manipulating LF hydrophone zarr data

"""
import xarray as xr
import warnings
import pandas as pd
import numpy as np

def slice_lf_hydrophones(ds, start_time, end_time, include_coord=True, time_base=pd.Timestamp('2015-01-01')):
    '''
    slice_lf_hydrophones - slices dataset using time slice and assigns coordinates to time dimension

    Parameters
    ----------
    ds : xarray.dataset
        dataset to slice
    start_time : pd.Timestamp
        start time for slice
    end_time : pd.Timestamp
        end time for slice
    include_coord : bool
        whether or not to include time coordinate or not (Default is True)
        - when True, best use would be for slice to be no larger than one month
    time_base : pd.Timestamp
        start time of the dataset
    '''

    ds_sliced = ds.isel({'time':__int_idx(start_time, end_time, time_base=time_base)})
    if include_coord:
        if (end_time - start_time) > pd.Timedelta(31, 'd'):
            warnings.warn('slice is longer than 1 month, include_coord=True might cause memory issues')
        time_coord = pd.to_datetime(np.arange(start_time.value, end_time.value, int(5e6)))
        ds_sliced = ds_sliced.assign_coords({'time':time_coord})

    return ds_sliced

def open_lfhydrophones():
    fn = '/home/jovyan/ooi/rsn_cabled/SummerSchool2025/lowfrequency_hydrophone_data/ooi_lfhydrophones.zarr'
    lf_hydrophones = xr.open_zarr(fn)
    return lf_hydrophones


def open_lfspectrograms():
    fn = '/home/jovyan/ooi/rsn_cabled/SummerSchool2025/lowfrequency_hydrophone_data/1hr_20150101_20230101_16192pt_HPcorrected.zarr'
    specs = xr.open_zarr(fn)
    return specs

    
def __int_idx(start_date, end_date, time_base=pd.Timestamp('2015-01-01')):
    '''
    int_idx - get integer indices for zarr store given date bounds

    Parameters
    ----------
    start_date : pd.Timestamp
        start date for integer slice
    end_date : pd.Timestamp
        end date for integer slice

    Returns
    -------
    idx_slice : slice
        slice between start_idx and end_idx
    '''

    start_idx = int((start_date - time_base).value/1e9*200)
    end_idx = int((end_date - time_base).value/1e9*200)

    return slice(start_idx,end_idx)