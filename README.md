# Video Compressor

A simple yet powerful Python script to compress video files to a target size while maintaining quality using FFmpeg.

## Prerequisites

- Python 3.6 or higher
- FFmpeg installed on your system
- ffprobe (typically comes with FFmpeg)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/video-compressor.git
cd video-compressor
```

2. Ensure FFmpeg is installed:
   - **macOS**: `brew install ffmpeg`
   - **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
   - **Windows**: Download from [FFmpeg official website](https://ffmpeg.org/download.html)

## Usage

1. Place your video file in the project directory
2. Update the input and output file names in `compressor.py`:
```python
input_file = "your_video.MOV"
output_file = "compressed_video.MOV"
```

3. Run the script:
```bash
python compressor.py
```

## How It Works

The script:
1. Calculates the optimal bitrate based on your target file size
2. Uses FFmpeg to compress the video while maintaining quality
3. Preserves audio quality with a 128k bitrate
4. Uses the 'slow' preset for better compression efficiency

## Parameters

- `input_file`: Path to your input video file
- `output_file`: Desired path for the compressed video
- `target_size_mb`: Target size in megabytes (default: 50MB)

## License

MIT

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.