"""Upload-ready reels (smaller file; the cover goes separately as cover_url). Usage: python3 -m publish.prep_videos S1E01 ..."""
import glob, os, subprocess, sys

def prep(eid):
    src = glob.glob(f'out/{eid}_*.mp4')[0]; dst, tmp = f'videos/{eid}.mp4', f'videos/{eid}.part.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27', '-maxrate', '3M',
                    '-bufsize', '6M', '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', tmp], check=True)
    os.replace(tmp, dst); print(dst, os.path.getsize(dst) // 1024, 'KB', flush=True)

if __name__ == '__main__':
    os.makedirs('videos', exist_ok=True)
    for e in sys.argv[1:]: prep(e.upper())
