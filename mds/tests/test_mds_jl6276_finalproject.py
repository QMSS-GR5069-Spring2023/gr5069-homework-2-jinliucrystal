from mds_jl6276_finalproject import mds_jl6276_finalproject
import folium
from folium.plugins import MarkerCluster
def test():

    # Create a folium Map object at specified longitude and latitude
    # Set the Map as the expected result
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
    expected = m

    # Call the get_map function from the module
    actual = mds_jl6276_finalproject.get_map('spanish')

    # Verify that the type of the actual is a Map object like expected
    assert type(actual) == type(expected), "Result should be an map object"

    # Return the actual result
    return actual


    
