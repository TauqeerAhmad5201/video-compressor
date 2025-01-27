import subprocess
import os

def compress_video(input_file, output_file, target_size_mb):
    # Calculate the bitrate (in bits/s) needed for the target file size
    target_size_bytes = target_size_mb * 1024 * 1024
    duration_cmd = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {input_file}"
    duration = float(subprocess.check_output(duration_cmd, shell=True))
    
    # Calculate target bitrate
    target_bitrate = (target_size_bytes * 8) / duration  # Bits per second

    # Execute FFmpeg to compress the video
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,                     # Input file
        "-b:v", f"{int(target_bitrate)}",     # Target bitrate for the video
        "-b:a", "128k",                       # Set a fixed bitrate for audio
        "-preset", "slow",                    # Compression speed/efficiency
        output_file                           # Output file
    ]
    
    subprocess.run(ffmpeg_cmd)
    print(f"Video compressed successfully! Saved to {output_file}")

# Input video file
input_file = "IMG_1730.MOV"  # Replace with your file path
output_file = "compressed_video1.MOV"  # Output file name

# Compress to 50 MB
compress_video(input_file, output_file, 45)