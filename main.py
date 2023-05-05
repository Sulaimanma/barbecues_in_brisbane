import json

# Read the GeoJSON data from the file
with open('Park_%E2%80%94_Barbeque_locations.geojson', 'r') as file:
    geojson_data = file.read()

data = json.loads(geojson_data)
filtered_features = []

for feature in data["features"]:
    if "ELECTRIC" not in feature["properties"]["ITEM_DESCRIPTION"]:
        filtered_features.append(feature)

data["features"] = filtered_features

# Save the filtered GeoJSON data to a new file
with open('filtered_geojson_data.geojson', 'w') as file:
    json.dump(data, file)

print("Filtered GeoJSON data has been saved to 'filtered_geojson_data.geojson'")
