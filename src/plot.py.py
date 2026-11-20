import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def map_var(da, lat, lon, vmin=None, vmax=None, cmap="viridis", title="", **kw):
    ax = plt.axes(projection=ccrs.PlateCarree(), figsize=(7, 6))
    p = ax.pcolormesh(lon, lat, da, cmap=cmap, vmin=vmin, vmax=vmax,
                      transform=ccrs.PlateCarree(), shading="auto", **kw)
    ax.coastlines(resolution="10m")
    ax.gridlines(draw_labels=True)
    plt.colorbar(p, ax=ax, shrink=0.7, label=da.attrs.get("units", ""))
    ax.set_title(title)
    return ax