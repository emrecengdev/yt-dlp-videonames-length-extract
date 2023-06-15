
Metadata extractor python script for [yt-dlp](https://github.com/yt-dlp/yt-dlp). It extracts only the video title and duration (in seconds) from the resulting `output.json` file. Of course, the playlist track will be written before the video title.

Usage ;
Install [Yt-dlp](https://github.com/yt-dlp/yt-dlp) on your system with its own instructions.

```python

yt-dlp --skip-download -J "playlistlink" > output.json
```

Replace `playlistlink` with the youtube playlist link you want.
After the process is complete ;

```python

python3 extract_video_info.py > video_info.md 
```

to get the final output.
Congratulations, that was all.
