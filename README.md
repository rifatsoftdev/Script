# My Linux Utility Scripts

A personal collection of custom Bash and Python scripts I use to automate daily Linux tasks.
This toolkit covers backup/restore, media tools, security helpers, QR utilities, networking checks, and productivity automation.

## Scripts At A Glance

| Script | Purpose |
|---|---|
| `audiobook` | Convert PDF text to MP3 audiobook (gTTS) |
| `backup` | Sync selected local folders to Google Drive (`rclone sync`) |
| `clean` | Clean system cache, logs, temp files, and browser cache |
| `cloudinary_storage.py` | Upload/delete files with Cloudinary |
| `download` | Download YouTube video/audio using `yt-dlp` |
| `duplicate_remove` | Move duplicate files from a sub-folder into `duplicate/` |
| `file2binary` | Convert file to binary text and binary text back to file |
| `ftpserver` | Start a local FTP server |
| `gettotp` | Generate live TOTP code from a secret |
| `imcrop` | Export image with rounded corners (PNG) |
| `network` | Show public/local IP and run internet speed test |
| `pdf2png` | Convert each PDF page into PNG images |
| `pixels4` | Shortcut to launch Android emulator `Pixel_4` |
| `qrmack` | Generate QR code image from text |
| `qrread` | Read/decode QR code from image |
| `restoe` | Restore local folders from cloud backup (`rclone copy`) |
| `rest_reminder` | Play periodic break reminder audio |
| `securefile` | Password-based file encryption/decryption (Fernet) |
| `takephoto` | Capture photo from webcam |
| `text2speech` | Convert input text to MP3 |
| `video-server.py` | Local FastAPI video gallery server |

## Quick Start

```bash
git clone <your-repo-url>
cd Script
chmod +x *
```

Optional: make scripts globally accessible by adding this directory to `PATH`.

```bash
echo 'export PATH="$PATH:/absolute/path/to/Script"' >> ~/.bashrc
source ~/.bashrc
```

## Dependencies

### System packages

- `python3` (recommended 3.10+)
- `rclone`
- `yt-dlp`
- `ffmpeg`
- `mpv`
- `poppler` (required by `pdf2image`)
- `zbar` (required by `pyzbar`)

### Python packages

```bash
pip install \
  PyPDF2 gTTS cloudinary pyftpdlib pyotp Pillow \
  speedtest-cli requests psutil pdf2image qrcode pyzbar \
  cryptography opencv-python fastapi uvicorn
```

## Common Usage

```bash
# YouTube download
./download video "https://youtube.com/watch?v=..."
./download audio "https://youtube.com/watch?v=..."

# QR tools
./qrmack
./qrread

# Encrypt / decrypt file
./securefile

# Start local video server
python3 video-server.py
```

## Configuration Notes

Some scripts contain hardcoded paths or local environment references.
Update these before daily use:

- `backup`, `restoe`: `BASE_PATH`, `REMOTE`
- `video-server.py`: `VIDEO_DIR1`
- `cloudinary_storage.py`: `PATH` and `Secure` module location
- `rest_reminder`: audio paths (`$HOME/MyLinux/Audio/...`)
- `takephoto`, `text2speech`, `audiobook`: output directories

## Safety Notes

- `clean` runs `sudo` commands and deletes cache/temp data.
- `securefile` deletes the source file after encrypt/decrypt.
- `duplicate_remove` moves matched files into `duplicate/`.

Review any script before running it on important data.

## Why This Repo

This repo is my personal Linux toolkit for faster daily workflows, reusable automation, and practical scripting experiments.
