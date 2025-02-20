// worker.js

async function getWeather(apiKey, city) {
  const locationUrl = `https://geoapi.qweather.com/v2/city/lookup?key=${apiKey}&location=${encodeURIComponent(city)}`;
  const locationResponse = await fetch(locationUrl);

  if (!locationResponse.ok) {
    return "无法获取位置信息";
  }

  const locationData = await locationResponse.json();
  if (locationData.code !== '200') {
    return `获取位置失败: ${locationData.code}`;
  }

  const locationId = locationData.location[0].id;
  const weatherUrl = `https://devapi.qweather.com/v7/weather/now?key=${apiKey}&location=${locationId}`;
  const weatherResponse = await fetch(weatherUrl);

  if (!weatherResponse.ok) {
    return "无法获取天气信息";
  }

  const weatherData = await weatherResponse.json();
    if (weatherData.code !== '200') {
        return `获取天气失败：${weatherData.code}`;
    }

  const now = weatherData.now;
  return `${city}当前天气：${now.text}，温度：${now.temp}°C，体感温度：${now.feelsLike}°C，湿度：${now.humidity}%`;
}

async function sendMessage(message, webhookKey) {
  const url = `https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=${webhookKey}`;
  const headers = { "Content-Type": "application/json" };
  const data = {
    msgtype: "text",
    text: {
      content: message,
    },
  };

  const response = await fetch(url, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(data),
  });

  if (response.ok) {
    const result = await response.json();
    if (result.errcode === 0) {
      console.log("消息发送成功");
      return true;
    } else {
      console.log(`消息发送失败: ${result.errmsg}`);
      return false;
    }
  } else {
    console.log(`请求失败，状态码：${response.status}`);
    return false;
  }
}

addEventListener("scheduled", (event) => {
  event.waitUntil(handleScheduled(event));
});

async function handleScheduled(event) {
    try {
      const weatherInfo = await getWeather(env.API_KEY, env.CITY);
      await sendMessage(weatherInfo, env.WEBHOOK_KEY)
    } catch (e) {
        console.error("Error:", e)
    }
}