import numpy as np
import xarray as xr

DEFAULT_BAD = ["CLOUD", "CLOUD_AMBIGUOUS", "CLOUD_MARGIN", "INVALID",
               "COSMETIC", "SATURATED", "SUSPECT", "HISOLZEN",
               "HIGHGLINT", "SNOW_ICE", "AC_FAIL", "WHITECAPS", "ADJAC"]

def wqsf_mask(wqsf, bad=DEFAULT_BAD):
    """True = bad pixel. Reads CF flag_masks/flag_meanings (no hardcoded bits)."""
    bits = dict(zip(wqsf.attrs["flag_meanings"].split(),
                    np.asarray(wqsf.attrs["flag_masks"], dtype="uint32")))
    v = wqsf.values.astype("uint32")
    m = np.zeros(v.shape, bool)
    for n in bad:
        if n in bits:
            m |= (v & bits[n]) != 0
    return xr.DataArray(m, dims=wqsf.dims, coords=wqsf.coords)