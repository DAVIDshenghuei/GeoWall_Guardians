"""Utils for Raster Visualisation."""

import datashader as ds
import datashader.transfer_functions as tf
import matplotlib.cm
import plotly.graph_objects as go
import rasterio
import xarray as xr
from pyproj import CRS, Transformer

epsg3857_to_epsg4326 = Transformer.from_crs(3857, 4326, always_xy=True)

def get_crs(filepath: str) -> CRS:
    """Retrieves the CRS of a GeoTiff data.

    Args:
        filepath: Path to a GeoTiff file.

    Returns:
        CRS of data stored in `filepath`
    """
    src = rasterio.open(filepath)
    return src.crs

def add_raster_to_plotly_figure(
    xarr_dataset: xr.Dataset,
    from_crs: CRS,
    column_name: str = "band_data",
    scale: float = 1.0,
) -> tuple[go.Figure, list]:
    """Add a raster plot on a Plotly graph object figure.

    Args:
        xarr_dataset (xr.Dataset): xarray dataset containing the raster data.
        from_crs (CRS): Coordinate Reference System of data stored in xarr_dataset.
        column_name (str): Name of the column in `xarr_dataset` to be plotted.
        scale (float): Scale factor for adjusting the plot resolution.

    Returns:
        tuple: The image and coordinates for Mapbox overlay
    """
    # Reproject to EPSG:3857 CRS
    xarr_dataset = xarr_dataset.rio.write_crs(from_crs).rio.reproject("EPSG:3857")
    xarr_dataset = xarr_dataset.where(xarr_dataset <= 1, 0)
    
    # Get Raster dimension and range
    numpy_data = xarr_dataset[column_name].squeeze().to_numpy()
    plot_height, plot_width = numpy_data.shape

    # Data aggregation
    canvas = ds.Canvas(
        plot_width=int(plot_width * scale), plot_height=int(plot_height * scale)
    )
    agg = canvas.raster(xarr_dataset[column_name].squeeze(), interpolate="linear")

    coords_lat_min, coords_lat_max = (
        agg.coords["y"].values.min(),
        agg.coords["y"].values.max(),
    )
    coords_lon_min, coords_lon_max = (
        agg.coords["x"].values.min(),
        agg.coords["x"].values.max(),
    )
    
    (
        coords_lon_min,
        coords_lon_max,
    ), (
        coords_lat_min,
        coords_lat_max,
    ) = epsg3857_to_epsg4326.transform(
        [coords_lon_min, coords_lon_max], [coords_lat_min, coords_lat_max]
    )
    
    # Corners of the image for mapbox
    coordinates = [
        [coords_lon_min, coords_lat_max],
        [coords_lon_max, coords_lat_max],
        [coords_lon_max, coords_lat_min],
        [coords_lon_min, coords_lat_min],
    ]

    # Apply color map
    img = tf.shade(
        agg,
        cmap=matplotlib.colormaps["Reds"],
        alpha=100,
        how="linear",
    )[::-1].to_pil()
    
    return img, coordinates

def read_geotiff_to_xarray(filepath: str) -> tuple[xr.Dataset, CRS]:
    """Read a GeoTIFF file into an xarray Dataset.

    Args:
        filepath (str): Path to the GeoTIFF file.

    Returns:
        tuple: The loaded xarray dataset and its CRS.
    """
    return xr.open_dataset(filepath).sel(band=1), get_crs(filepath)

def create_map_with_geotiff_tiles(tiles_to_overlay: list[str]) -> go.Figure:
    """Create a map with multiple GeoTIFF tiles overlaid.

    Args:
        tiles_to_overlay (list[str]): Path to tiles to overlay on map.

    Returns:
        Figure: A Plotly figure with overlaid GeoTIFF tiles.
    """
    fig = go.Figure(go.Scattermapbox())
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox=dict(center=go.layout.mapbox.Center(lat=0, lon=20), zoom=2.0),
    )
    fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})
    
    mapbox_layers = []
    for tile in tiles_to_overlay:
        if tile.endswith(".tif") or tile.endswith(".tiff"):
            xarr_dataset, crs = read_geotiff_to_xarray(tile)
            img, coordinates = add_raster_to_plotly_figure(
                xarr_dataset, crs, "band_data", scale=1.0
            )
            mapbox_layers.append(
                {"sourcetype": "image", "source": img, "coordinates": coordinates}
            )
    
    # Overlay the resulting image
    fig.update_layout(mapbox_layers=mapbox_layers)
    return fig 