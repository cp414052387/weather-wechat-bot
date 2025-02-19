import weather
import wechat_bot
import config

def main():
    try:
        weather_info = weather.get_weather(config.API_KEY, config.CITY)
        if "无法获取" in weather_info or "失败" in weather_info:
            print(weather_info)
            wechat_bot.send_message(weather_info, config.WEBHOOK_KEY)
        else:
            if not wechat_bot.send_message(weather_info, config.WEBHOOK_KEY):
                print("发送消息失败")

    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    main()