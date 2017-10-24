SrtAlign
========

Fix out of sync subtitles using the gentle speech to text force aligner.

Requirements:
------------

* Gentle force aligner: https://github.com/lowerquality/gentle
* PySrt: https://pypi.python.org/pypi/pysrt
* ffmpeg: https://www.ffmpeg.org/download.html

Usage:
-----
This module was designed to align several srt files in a batch; 
it takes as input three directories:
* ```<gentledir>```: Directory containing gentle installation,
            specially the ```align.py``` file
* ```<videodir>```: Directory containing video/audio files to align with the 
            corresponding srt file; the module automatically extracts 
            wav files for each video file in this directory and stores them 
            under a new directory named ```wavfiles```
* ```<srtdir>```: Directory containing srt files to be aligned; srt files 
            should have the same name as the media files in ```<videodir>```.
            For example: If mov_a.mp4 is a file in ```<videodir>```, the module
            expects a corresponding file mov_1.srt in ```<srtdir>```.

The run the script, use the following command:
```fix_subtitle_timestamps.py <gentledir> <videodir> <srtdir>```

Output:
------

The aligned subtitles are written in a newly created directory named ```alignedsrt``` in the same path as ```<srtdir>```.
