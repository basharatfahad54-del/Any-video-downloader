from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import re
import os
import requests
import uuid

app = FastAPI()

def get_tiktok_no_watermark(url):
    # Step 1: Fetch page source
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    # Step 2: Extract video URLs using regex
    no_wm = re.findall(r'"playAddr":"(.*?)"', r.text)
    if not no_wm:
        raise Exception("Cannot find video URL")

    # Clean URL
    video_url = no_wm[0].replace("\\u0026", "&")

    # TikTok returns watermarked sometimes; alternative:
    video_url = video_url.replace("watermark=1", "watermark=0")

    return video_url


@app.post("/download")
def download_video(video_url: str):
    try:
        direct_url = get_tiktok_no_watermark(video_url)

        # Download
        filename = f"{uuid.uuid4()}.mp4"
        video_data = requests.get(direct_url).content

        with open(filename, "wb") as f:
            f.write(video_data)

        return FileResponse(filename, media_type="video/mp4", filename=filename)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    # Allow running via `python main.py` and also when uvicorn isn't installed globally
    try:
        import uvicorn
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    except Exception:
        print("Uvicorn is not installed in the current environment.\nStart the server using: python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000")
