IntExt : list = ['Exterior', 'Interior']
overpassAPI : str = 'http://overpass-api.de/api/interpreter'
overpassQuery : str = '[out:json];area[name="Paris"];(node[amenity="cafe"](area););out;'

thinkboardsURL : str = 'https://httpbin.org/post'