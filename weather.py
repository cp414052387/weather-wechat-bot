import requests
import json

def get_weather(api_key, city):
    # 获取 location ID
    location_url = f"https://geoapi.qweather.com/v2/city/lookup?key={api_key}&location={city}"
    location_response = requests.get(location_url)
    
    if location_response.status_code != 200:
        return "无法获取位置信息"

    location_data = json.loads(location_response.text)
    if location_data['code'] != '200':
        return f"获取位置失败: {location_data['code']}"
    
    location_id = location_data['location'][0]['id']

    # 获取天气
    weather_url = f"https://devapi.qweather.com/v7/weather/now?key={api_key}&location={location_id}"
    weather_response = requests.get(weather_url)

    if weather_response.status_code != 200:
        return "无法获取天气信息"

    weather_data = json.loads(weather_response.text)
    if weather_data['code'] != '200':
        return f"获取天气失败：{weather_data['code']}"

    now = weather_data['now']
    return f"{city}当前天气：{now['text']}，温度：{now['temp']}°C，体感温度：{now['feelsLike']}°C，湿度：{now['humidity']}%"