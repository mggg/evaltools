from gerrychain import (
    Graph, 
    Partition, 
)
from gerrychain.updaters import (
    boundary_nodes,
    Tally, # TODO: ask why this isn't already in GeographicPartition
)

from geopandas import GeoDataFrame
from cv2 import minEnclosingCircle
from shapely.ops import unary_union
from math import pi
import numpy as np

def _reock(partition: Partition, gdf: GeoDataFrame, crs: str):
    """
    TODO: Add documentation.
    """
    gdf = gdf.to_crs(crs)
    gdf_graph = Graph.from_geodataframe(gdf)
    geo_partition = Partition(graph=gdf_graph,
                              assignment=partition.assignment,
                              updaters={
                                  "boundary_nodes": boundary_nodes,
                                  "area": Tally("area", alias="area"),
                              }
                             )
    geometries = dict(gdf.geometry.apply(lambda p: p.convex_hull))

    boundary = set.union(*(set(e) for e in geo_partition["cut_edges"])).union(
        geo_partition["boundary_nodes"]
    )
    part_scores = {}
    for part, nodes in geo_partition.parts.items():
        geom = unary_union([
            geometries[node] for node in nodes if node in boundary
        ]).convex_hull
        coords = np.array(geom.exterior.coords.xy).T.astype(np.float32)
        _, radius = minEnclosingCircle(coords)
        score = float(geo_partition['area'][part] / (pi * radius**2))
        assert 0 < score < 1
        part_scores[part] = score
    return part_scores