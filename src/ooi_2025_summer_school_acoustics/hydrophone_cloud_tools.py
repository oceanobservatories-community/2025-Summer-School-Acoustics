"""
Tools for openning and manipulating LF hydrophone zarr data

"""
import xarray as xr

def open_lf_hydrophones():
    """
    open low frequency hydrophone zarr dataset. By default, this dataset does not have a time coord.
    
    Returns
    -------
    ds : xr.Dataset
        xarray dataset of the hydrophone time-series data
    """
    return

def slice_lf_hydrophones():
    """
    slice the low frequency hydrophone zarr dataset to a specific time slice.

    Parameters
    ----------
    start_time : pd.Timestamp
        start time of the slice
    end_time : pd.Timestamp
        end time of the slice
    include_coords : bool
        if True, include the coordinates in the slice. Default is False.

    Returns
    -------
    ds_slice : xr.Dataset
        xarray dataset of the hydrophone time-series data
    """

    return