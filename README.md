# Any Video Downloader

A lightweight **FastAPI** app that downloads videos without the watermark. It ships with a tiny web UI and a simple REST endpoint.

> Currently supports TikTok watermark-free downloads. More platforms coming soon.

## Features

- Download videos without watermark
- Simple web interface (`index.html`)
- FastAPI REST endpoint (`POST /download`)
- Easy setup with PowerShell scripts

## Requirements

- Python 3.x

## Setup (PowerShell / Windows)

```powershell
# 1. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the FastAPI server
# Starts on http://127.0.0.1:8000
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Or simply run the helper script:

```powershell
.\start_server.ps1
```

## Usage

Once the server is running, open the web UI and paste a video link, or call the API directly:

```powershell
curl -X POST "http://127.0.0.1:8000/download" -d "video_url=https://www.tiktok.com/@user/video/123456789"
```

The endpoint returns the video file as a response.

## Project Structure

```
main.py                 # FastAPI app and download logic
index.html              # Web interface
requirements.txt        # Python dependencies
start_server.ps1        # Setup venv and run the server
run_static_server.ps1   # Serve the folder as a static site
```

## Notes

- The server exposes `POST /download` which accepts a `video_url` parameter and returns the video file.
- To serve `index.html` statically only:

```powershell
python -m http.server 8000
```

## Hire Me / Connect

If you want a **custom project or a custom AI model**, I'm available for freelance work.

- **Follow me on LinkedIn** for more projects: [Muhammad Fahad](https://www.linkedin.com/in/muhammad-fahad-8b6258370/)
- **Order on Fiverr**: [https://www.fiverr.com/s/0DDdmQE](https://www.fiverr.com/s/0DDdmQE)
- **Hire me on Upwork**: [https://www.upwork.com/freelancers/~018454f81ddfcb4416](https://www.upwork.com/freelancers/~018454f81ddfcb4416)

## License

This project is open source. See the repository for details.
