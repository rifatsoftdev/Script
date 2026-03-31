

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import os
import uvicorn
import socket



app = FastAPI()

VIDEO_DIR1 = "/home/rifatsoftdev/Temporary"
# VIDEO_DIR2 = "/storage/8991-1600/RIFAT-S-WINDOWS/Videos"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/videos", StaticFiles(directory=VIDEO_DIR1), name="videos")



@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    files1 = [
        f for f in os.listdir(VIDEO_DIR1)
        if os.path.isfile(os.path.join(VIDEO_DIR1, f)) and f.lower().endswith(('.mp4', '.mkv', '.webm'))
    ]
    # files2 = [
    #     f for f in os.listdir(VIDEO_DIR2)
    #     if os.path.isfile(os.path.join(VIDEO_DIR2, f)) and f.lower().endswith(('.mp4', '.mkv', '.webm'))
    # ]
    
    # files1.extend(files2)
    files = set(files1)
    
    video_cards = ""
    for f in files:
        video_cards += f"""
        <div class="video-card">
            <a href="/watch?name={f}">
                <video class="thumb" muted>
                    <source src="/videos/{f}" type="video/mp4">
                </video>
                <p>{f}</p>
            </a>
        </div>
        """

    return f"""
    <html>
    <head>
        <title>Video Gallery</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
            }}
            h2 {{
                text-align: center;
                padding: 20px;
            }}
            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 20px;
                padding: 20px;
            }}
            .video-card {{
                background: white;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                transition: transform 0.2s;
            }}
            .video-card:hover {{
                transform: scale(1.03);
            }}
            .thumb {{
                width: 100%;
                height: auto;
                display: block;
            }}
            .video-card p {{
                margin: 10px;
                font-size: 14px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }}
            a {{
                text-decoration: none;
                color: inherit;
            }}
        </style>
    </head>
    <body>
        <h2>Video Gallery</h2>
        <div class="grid">
            {video_cards}
        </div>
    </body>
    </html>
    """

@app.get("/watch", response_class=HTMLResponse)
async def watch(name: str):
    return f"""
    <html>
        <head>
            <title>Watching {name}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    padding: 20px;
                    text-align: center;
                }}
                video {{
                    width: 90%;
                    max-width: 800px;
                    height: auto;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
                }}
                a {{
                    display: inline-block;
                    margin-top: 20px;
                    text-decoration: none;
                    color: #007bff;
                }}
            </style>
        </head>
        <body>
            <h2>{name}</h2>
            <video controls autoplay>
                <source src="/videos/{name}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <br><a href="/">Back to gallery</a>
        </body>
    </html>
    """


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception as e:
        print(f"Error occurred while getting IP: {e}")
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    uvicorn.run(
        "video-server:app",
        host=get_ip(),
        port=8000,
        reload=True,
        log_level="info"
    ) 
