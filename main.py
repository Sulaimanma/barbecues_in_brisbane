import json

geojson_data = """
{
"type": "FeatureCollection",
"name": "Park___Barbeque_locations",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [
{ "type": "Feature", "properties": { "OBJECTID": 1, "SAP_EQUIPMENT": "200479102", "ITEM_DESCRIPTION": "BBQ - ELECTRIC SINGLE", "ITEM_TYPE": "BARBEQUE", "SAP_FUNCTIONAL_LOCATION": "B-RE-1866-N002", "PARK_NUMBER": "D0287", "PARK_NAME": "SHEPHERD PLACE PARK", "SUBURB": "SHORNCLIFFE", "POWER_TYPE": "MAINS POWER", "NUMBER_OF_PLATES": 1, "LONG": 153.080779807, "LAT": -27.322802682 }, "geometry": { "type": "Point", "coordinates": [ 153.080779807000113, -27.322802681999974 ] } },
{ "type": "Feature", "properties": { "OBJECTID": 2, "SAP_EQUIPMENT": "100293721", "ITEM_DESCRIPTION": "BBQ - ELECTRIC DOUBLE", "ITEM_TYPE": "BARBEQUE", "SAP_FUNCTIONAL_LOCATION": "B-RE-0169-N003", "PARK_NUMBER": "D2007", "PARK_NAME": "CASCADE DRIVE PARK (NO.20)", "SUBURB": "FOREST LAKE", "POWER_TYPE": "MAINS POWER", "NUMBER_OF_PLATES": 2, "LONG": 152.96464914500001, "LAT": -27.629073494999901 }, "geometry": { "type": "Point", "coordinates": [ 152.964649145000067, -27.629073494999943 ] } }
]
}

"""

data = json.loads(geojson_data)
filtered_features = []

for feature in data["features"]:
  if "ELECTRIC" not in feature["properties"]["ITEM_DESCRIPTION"]:
    filtered_features.append(feature)

data["features"] = filtered_features
filtered_geojson_data = json.dumps(data)

print(filtered_geojson_data)
