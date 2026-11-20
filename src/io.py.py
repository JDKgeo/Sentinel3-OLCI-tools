from pathlib import Path
import xarray as xr

BANDS = {"Oa01": 400.0, "Oa02": 412.5, "Oa03": 442.5, "Oa04": 490.0,
         "Oa05": 510.0, "Oa06": 560.0, "Oa07": 620.0, "Oa08": 665.0,
         "Oa09": 673.75, "Oa10": 681.25, "Oa11": 708.75, "Oa12": 753.75,
         "Oa13": 761.25, "Oa14": 764.375, "Oa15": 767.5, "Oa16": 778.75,
         "Oa17": 865.0, "Oa18": 885.0, "Oa19": 900.0, "Oa20": 940.0,
         "Oa21": 1020.0}

def open_l1(scene):
    """Lt (band, rows, columns) from a .SEN3 L1B directory."""
    scene = Path(scene)
    assert (scene / "xfdumanifest.xml").exists(), "not an OLCI .SEN3 scene"
    das = [xr.open_dataset(f)[f"{f.stem[:4]}_radiance"].assign_coords(band=f.stem[:4])
           for f in sorted(scene.glob("Oa*_radiance.nc"))]
    L = xr.concat(das, "band").rename("Lt")
    L = L.assign_coords(wavelength=("band", [BANDS[b] for b in L.band.values]))
    L.attrs["units"] = "mW.m-2.sr-1.nm-1"
    return L

def open_geo(scene):
    return xr.open_dataset(Path(scene) / "geo_coordinates.nc")[["latitude", "longitude"]]