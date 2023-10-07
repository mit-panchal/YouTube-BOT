import os
import subprocess

# Run Reel_Downloader.py
reel_downloader_path = r"Program Files\Reel_Downloader.py"
subprocess.run(["python", reel_downloader_path], check=True)

reel_renamer = r"Program Files\Rename_account_name.py"
subprocess.run(["python", reel_renamer], check=True)

# Run final video maker.py
final_video_maker_path = r"Program Files\final video maker.py"
subprocess.run(["python", final_video_maker_path], check=True)

tags_maker_path = r"Program Files\Tags_maker.py"
subprocess.run(["python", tags_maker_path], check=True)
# Run Youtube_Uploder.py
youtube_uploader_path = r"Program Files\Youtube_Uploder.py"
subprocess.run(["python", youtube_uploader_path], check=True)
