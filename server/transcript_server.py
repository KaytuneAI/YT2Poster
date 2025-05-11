
from flask import Flask, request, jsonify, send_from_directory
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()

app = Flask(__name__)
CORS(app)

# 从环境变量获取 YouTube API 密钥
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# 移除强制要求 API key 的检查
# if not YOUTUBE_API_KEY:
#     raise ValueError("YouTube API 密钥未设置。请在 .env 文件中设置 YOUTUBE_API_KEY")

@app.route("/transcript", methods=["GET"])
def get_transcript():
    video_id = request.args.get("videoId")
    if not video_id:
        return jsonify({"error": "Missing videoId"}), 400

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        try:
            transcript = transcript_list.find_transcript(['en', 'en-US'])
        except NoTranscriptFound:
            transcript = transcript_list.find_generated_transcript(['en', 'en-US'])

        result = transcript.fetch()
        full_text = " ".join(item.text for item in result)
        return jsonify({"videoId": video_id, "transcript": full_text})

    except (TranscriptsDisabled, NoTranscriptFound) as e:
        return jsonify({"error": f"Transcript not available: {str(e)}"}), 404
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.route("/published_at", methods=["GET"])
def get_published_at():
    # 如果没有设置 API key，直接返回空结果
    if not YOUTUBE_API_KEY:
        return jsonify({
            "warning": "未设置 YouTube API Key，无法获取发布时间",
            "publishedAt": None
        })

    video_id = request.args.get("videoId")
    if not video_id:
        return jsonify({"error": "Missing videoId"}), 400

    url = (
        f"https://www.googleapis.com/youtube/v3/videos"
        f"?part=snippet&id={video_id}&key={YOUTUBE_API_KEY}"
    )

    try:
        res = requests.get(url)
        data = res.json()
        items = data.get("items", [])
        if not items:
            return jsonify({"error": "No data found"}), 404
        published_at = items[0]["snippet"]["publishedAt"]
        return jsonify({"videoId": video_id, "publishedAt": published_at})
    except Exception as e:
        return jsonify({"error": f"Failed to fetch published date: {str(e)}"}), 500

# 添加根路由
@app.route("/")
def index():
    return send_from_directory('../web', 'index.html')

# 添加静态文件路由
@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory('../web', filename)

if __name__ == "__main__":
    app.run(debug=True)
