from mds_jl6276_finalproject import mds_jl6276_finalproject
import folium
from folium.plugins import MarkerCluster
def test():



      """
     Tests the get_map function from the mds_jl6276_finalproject module.

     Returns
     -------
     folium.Map
         A map object showing user's location.
     """
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
    expected = m
    actual = mds_jl6276_finalproject.get_map('Spanish')


    m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
    expected = m
    actual = mds_jl6276_finalproject.get_map('spanish')
    assert type(actual) == type(expected), "Result should be an map object"
    return actual


    
