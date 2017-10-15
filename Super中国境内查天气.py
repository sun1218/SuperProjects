import urllib.request
import gzip
import json
print('天气查询')
def get_weather() :
    city_name = input('请输入要查询的城市名称：')
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
    weather_data = urllib.request.urlopen(url1).read()
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    weather_dict = json.loads(weather_data)
    return weather_dict

def show_weather(weather_data):
    weather_dict = weather_data 
    if weather_dict.get('desc') == 'invilad-citykey':
        print('你输入的城市名有误，或者天气中心未收录你所在城市')
    elif weather_dict.get('desc') =='OK':
        forecast = weather_dict.get('data').get('forecast')
        print('城市：',weather_dict.get('data').get('city'))
        print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
        print('感冒：',weather_dict.get('data').get('ganmao'))
        print('风向：',forecast[0].get('fengxiang'))
        print('风级：',forecast[0].get('fengli'))
        print('高温：',forecast[0].get('high'))
        print('低温：',forecast[0].get('low'))
        print('天气：',forecast[0].get('type'))
        print('日期：',forecast[0].get('date'))
        print('*******************************')
        four_day_forecast =input('是否要显示未来四天天气，是/否：')
        if four_day_forecast == 'Y' or 'y':
            for i in range(1,5):
                print('日期：',forecast[i].get('date'))
                print('风向：',forecast[i].get('fengxiang'))
                print('风级：',forecast[i].get('fengli'))
                print('高温：',forecast[i].get('high'))
                print('低温：',forecast[i].get('low'))
                print('天气：',forecast[i].get('type'))
                print('--------------------------')

show_weather(get_weather_data())
