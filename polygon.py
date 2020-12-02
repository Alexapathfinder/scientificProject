#%%

import geopandas as gpd
gdf = gpd.read_file('../Inter-settlement_territories.shp')
print(gdf.type)

import fiona
shape = fiona.open("../Inter-settlement_territories.shp")
print(shape.schema)
#first feature of the shapefile
first = shape.next()
print(first) 