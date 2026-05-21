import folium
import pandas as pd

# ── STATION COORDINATES (from your actual data) ──────────────
casual_stations = {
    "Navy Pier": [41.8917, -87.6086],
    "DuSable Lake Shore Dr & Monroe St": [41.8810, -87.6167],
    "Michigan Ave & Oak St": [41.9010, -87.6238],
    "DuSable Lake Shore Dr & North Blvd": [41.9118, -87.6268],
    "Streeter Dr & Grand Ave": [41.8923, -87.6120],
    "Millennium Park": [41.8827, -87.6233],
    "Shedd Aquarium": [41.8676, -87.6139],
    "Theater on the Lake": [41.9263, -87.6308],
    "Dusable Harbor": [41.8855, -87.6128],
    "Michigan Ave & 8th St": [41.8728, -87.6240],
    "Montrose Harbor": [41.9632, -87.6380],
    "Adler Planetarium": [41.8663, -87.6067],
    "Field Museum": [41.8662, -87.6170],
    "Clark St & Lincoln Ave": [41.9156, -87.6340],
    "Clark St & Armitage Ave": [41.9182, -87.6363],
}

member_stations = {
    "Kingsbury St & Kinzie St": [41.8891, -87.6385],
    "Canal St & Madison St": [41.8820, -87.6397],
    "Clinton St & Washington Blvd": [41.8833, -87.6411],
    "Clinton St & Madison St": [41.8820, -87.6411],
    "State St & Chicago Ave": [41.8966, -87.6279],
    "Wells St & Elm St": [41.9030, -87.6344],
    "Clark St & Elm St": [41.9030, -87.6313],
    "Clinton St & Jackson Blvd": [41.8779, -87.6411],
    "Wells St & Concord Ln": [41.9120, -87.6344],
    "Wells St & Huron St": [41.8948, -87.6344],
    "Canal St & Adams St": [41.8794, -87.6397],
    "Kingsbury St & Erie St": [41.8940, -87.6385],
    "University Ave & 57th St": [41.7915, -87.5990],
    "Desplaines St & Kinzie St": [41.8891, -87.6440],
    "Wells St & Hubbard St": [41.8902, -87.6344],
}

# ── CREATE MAP ───────────────────────────────────────────────
m = folium.Map(location=[41.8827, -87.6233], zoom_start=13, tiles="CartoDB positron")

# ── ADD TITLE ────────────────────────────────────────────────
title_html = """
<div style="position: fixed; top: 15px; left: 50%; transform: translateX(-50%);
     z-index: 1000; background-color: white; padding: 10px 20px;
     border-radius: 8px; box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
     font-family: Arial; font-size: 16px; font-weight: bold; color: #333;">
     Cyclistic Bike-Share: Top Start Stations by Rider Type
</div>
"""
m.get_root().html.add_child(folium.Element(title_html))

# ── ADD LEGEND ───────────────────────────────────────────────
legend_html = """
<div style="position: fixed; bottom: 30px; left: 30px; z-index: 1000;
     background-color: white; padding: 12px 16px; border-radius: 8px;
     box-shadow: 2px 2px 6px rgba(0,0,0,0.3); font-family: Arial; font-size: 13px;">
     <b>Rider Type</b><br>
     <span style="color:#e74c3c;">●</span> Casual Rider (Leisure/Tourist)<br>
     <span style="color:#2980b9;">●</span> Annual Member (Commuter)
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# ── PLOT CASUAL STATIONS ─────────────────────────────────────
for station, coords in casual_stations.items():
    folium.CircleMarker(
        location=coords,
        radius=10,
        color="#e74c3c",
        fill=True,
        fill_color="#e74c3c",
        fill_opacity=0.8,
        tooltip=f"🔴 CASUAL: {station}",
        popup=folium.Popup(f"<b>Casual Rider Station</b><br>{station}", max_width=200)
    ).add_to(m)

# ── PLOT MEMBER STATIONS ─────────────────────────────────────
for station, coords in member_stations.items():
    folium.CircleMarker(
        location=coords,
        radius=10,
        color="#2980b9",
        fill=True,
        fill_color="#2980b9",
        fill_opacity=0.8,
        tooltip=f"🔵 MEMBER: {station}",
        popup=folium.Popup(f"<b>Member Station</b><br>{station}", max_width=200)
    ).add_to(m)

# ── SAVE MAP ─────────────────────────────────────────────────
output = "/Users/macbook/Downloads/Cyclistic-analysis/cyclistic_station_map.html"
m.save(output)
print(f"✅ Interactive map saved to: {output}")
print("Open the HTML file in your browser to view the map.")