SrtAlign
========

Uses gentle force aligner to correct time stamps in subtitles

Requirements:
------------

* Gentle force aligner: https://github.com/lowerquality/gentle
* PySrt: https://github.com/lowerquality/gentle
* ffmpeg: https://github.com/lowerquality/gentle

Prep:
----

Extract audio from the media file using ffmpeg:

```ffmpeg -i <mp4dir>/input.mp4 -vn <wavdir>/out.wav```

Usage:
-----

```force_align_subtitles.py <gentledir> <audiodir> <srtdir>```

Output:
------

The aligned subtitles are written in a newly created directory named alignedsrt in the same path as ```<srtdir>```.
