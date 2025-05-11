# 🎬 YT2Poster 使用指南

## 🌟 简介
YT2Poster 是一款基于 AI 的 YouTube 视频摘要工具，支持从视频链接中自动提取字幕与上传时间，并调用 DeepSeek 大模型生成结构化中文摘要与精彩故事内容，最终一键导出为可分享的精美内容海报。

---

## 🚀 功能特点
- ✅ 自动提取 YouTube 视频标题与封面图
- ✅ 自动获取字幕与视频上传时间（使用 Google API）
- ✅ 支持 DeepSeek API 生成中文摘要与五段故事内容
- ✅ 美观地渲染为 Tailwind 风格海报，可导出为 PNG
- ✅ 支持用户编辑标题、摘要、故事内容

---

## 🔧 使用前准备
1. 确保PC可以访问Youtube，并且准备好 YouTube 视频链接（如：https://youtu.be/abc12345678）
2. 申请 [DeepSeek API Key](https://platform.deepseek.com/)
3. （可选）申请 Google YouTube Data API Key，用于获取上传时间

---

## 📦 文件结构说明

```
YT2Poster/
├── start_server.bat               ← Windows 用户双击启动后端服务
├── .env.template                  ← 示例 Google API Key 文件
├── requirements.txt               ← Python 依赖列表
├── README_使用说明.txt            ← 本使用文档
├── server/
│   └── transcript_server.py       ← Flask 后端服务
└── web/
    ├── index.html                 ← 主界面（打开即可使用）
    └── banner.jpg                 ← 顶部横幅图
```

---

## 🛠️ 安装与运行步骤

### 第一步：安装 Python 环境
- 安装 [Python 3.10+](https://www.python.org/)
- 可使用 Portable Python，无需管理员权限

### 第二步：将整个zip目录copy到本地，或者从Github clone下来。

### 第三步：启动本地服务
- Windows 用户：双击运行 `start_server.bat`

### 第四步：使用页面功能
- 进入http://127.0.0.1:5000/ 主页（推荐用 Chrome 浏览器）
- 按照界面步骤：
  1. 输入视频链接，点击“提取视频封面图和 Title”
  2. 点击“自动获取字幕与上传时间”
  3. 点击“生成摘要与故事”
  4. 点击“导出海报”保存为 PNG 图片

可选：填写 Google API Key（主要为了获得视频上传时间，https://console.cloud.google.com/）
- 编辑 `.env` 文件，填入你的 Key：
  YOUTUBE_API_KEY=你的key
---

---

## ⚠️ 注意事项

- 所有处理逻辑均在本地执行，不上传任何用户数据
- DeepSeek API Key 和 Google API Key 均不会被发送至服务器
- 本工具仅用于学习与研究，生成内容不得用于商业用途
- 原视频及转录内容版权归 YouTube 原创作者所有


## 📮 技术支持

如有问题或建议欢迎联系：

- 📧 邮箱：geospecial@gmail.com
- 🧑‍💻 开发者：Kaytune k.AI
