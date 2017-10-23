SrtAlign
========

Uses gentle force aligner to correct time stamps in subtitles

Requirements:
------------

* Gentle force aligner: https://github.com/lowerquality/gentle
* PySrt: https://pypi.python.org/pypi/pysrt
* ffmpeg: https://www.ffmpeg.org/download.html

Usage:
-----
This module was designed to convert several srt files in a batch; 
it takes as input three directories:
* gentledir: Directory containing gentle installation,
            specially the align.py dir
* mp4dir: Directory containing video/audio files to align with srt
* srtdir: Directory containing srt files to be aligned

The run the script, use the following command:
```force_align_subtitles.py <gentledir> <audiodir> <srtdir>```

Output:
------

The aligned subtitles are written in a newly created directory named alignedsrt in the same path as ```<srtdir>```.
