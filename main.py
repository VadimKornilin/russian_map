import folium
import json
from folium import GeoJson

# Загружаем geojson с данными о регионах России
with open('russia_regions.geojson', 'r', encoding='utf-8') as f:
    regions_geojson = json.load(f)

# Создаем карту, центрированную на России
m = folium.Map(location=[55.7558, 37.6176], zoom_start=4)

# Добавляем регионы России на карту
folium.GeoJson(
    regions_geojson,
    name="region",
    popup=folium.GeoJsonPopup(fields=["region"]),  # Для отображения имени региона при клике
    tooltip=folium.GeoJsonTooltip(fields=["region"], sticky=True)  # Для отображения имени региона при наведении
).add_to(m)

# Сохраняем карту в HTML файл
m.save("russia_map.html")
