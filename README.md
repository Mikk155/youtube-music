# youtube-music
 Python script for downloading music from a youtube playlist

```
pip install -r requirements.txt
```

Run the script:
```
python3 main.py
```
It will now ask you for a youtube playlist url, provide one and press enter.

All the videos as ``mp3`` files will now be downloaded into ``music/``

You can alternativelly run the script with the argument ``-ignore`` to ignore all errors and keep iterating the playlist:
```
python3 main.py -ignore
```

I use [pytubefix](https://github.com/JuanBindez/pytubefix) due to pytube's issue [#1894](https://github.com/pytube/pytube/issues/1894) that seems unsolved yet.