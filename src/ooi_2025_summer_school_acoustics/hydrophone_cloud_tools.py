"""
Tools for openning and manipulating LF hydrophone zarr data

"""
import xarray as xr

def open_hydrophone_dataset():
    """
    open low frequency hydrophone zarr dataset
    
    Returns
    -------
    ds : xr.Dataset
        xarray dataset of the hydrophone time-series data
    """
    return