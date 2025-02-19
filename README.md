# Weather WeChat Bot (Cloudflare Workers 版)

本项目是一个使用 Cloudflare Workers 实现的每日天气预报微信机器人。它会定时查询指定城市的天气，并通过企业微信 webhook 将天气信息发送给您。

## 功能

-   每日定时查询天气。
-   通过企业微信 webhook 发送消息。
-   使用 Cloudflare Workers 部署，无需服务器。

## 前提条件

-   和风天气 API Key ([https://dev.qweather.com/](https://dev.qweather.com/))
-   企业微信 webhook URL
-   Cloudflare 账号 ([https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up))

## 部署步骤

1.  **创建 Cloudflare Worker**:
    -   登录 Cloudflare Dashboard。
    -   点击左侧导航栏的 "Workers & Pages"。
    -   点击 "Create application"。
    -   点击 "Create Worker"。
    -   为您的 Worker 命名 (例如：`weather-wechat-bot`)。
    -   选择 "HTTP handler" 作为 starter。
    -   点击 "Deploy"。

2.  **复制代码**:
    -   将 `worker.js` 文件中的代码复制到 Cloudflare Worker 编辑器中。

3.  **配置环境变量**:
    -   在 Worker 的编辑页面，点击 "Settings" 标签。
    -   点击 "Variables"。
    -   在 "Environment Variables" 部分，点击 "Add variable"。
    -   添加以下环境变量：
        -   `API_KEY`: 您的和风天气 API Key。
        -   `CITY`: 您要查询的城市名称 (例如：`贵阳市白云区`)。
        -   `WEBHOOK_KEY`: 您的企业微信 webhook key。
    -   点击 "Save"。

4.  **设置定时触发器**:
    -   在 Worker 的编辑页面，点击 "Triggers" 标签。
    -   点击 "Add Cron Trigger"。
    -   在 "Cron expression" 中输入 `58 23 * * *`。  **注意：** Cloudflare Workers 使用 UTC 时间，所以 7:58 AM (北京时间) 对应的是前一天的 23:58 (UTC 时间)。
    -   点击 "Add trigger"。

5.  **测试**:
    您可以在 Cloudflare Workers 界面上测试您的 Worker。

## 注意事项

-   Cloudflare Workers 的免费套餐有每日请求次数限制，请注意使用量。
-   企业微信 webhook 有发送频率限制，请避免过于频繁地发送消息。