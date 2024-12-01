import folium
import json
from folium import GeoJson

# Загружаем geojson с данными о регионах России
with open('russia_regions.geojson', 'r', encoding='utf-8') as f:
    regions_geojson = json.load(f)

# Создаем карту, центрированную на России
m = folium.Map(location=[55.7558, 37.6176], zoom_start=4)

# Функция для установки стиля для каждого региона
def style_function(feature):
    # Получаем название региона из geojson
    region_name = feature['properties']['region']
    
    # Если это Пермский край, применяем особый стиль
    if region_name == "Пермский край":
        return {
            'fillColor': '#FF6347',  # Красный цвет
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.6
        }
    else:
        # Для остальных регионов стандартный стиль
        return {
            'fillColor': '#3186cc',  # Синий цвет
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.6
        }

# Добавляем регионы России на карту с кастомным стилем
folium.GeoJson(
    regions_geojson,
    name="region",
    style_function=style_function,  # Используем функцию для стилизации
    popup=folium.GeoJsonPopup(fields=["region"]),  # Для отображения имени региона при клике
    tooltip=folium.GeoJsonTooltip(fields=["region"], sticky=True)  # Для отображения имени региона при наведении
).add_to(m)

# Добавляем слой управления
folium.LayerControl().add_to(m)

# Сохраняем карту в HTML файл
m.save("russia_map_with_perm_colored.html")