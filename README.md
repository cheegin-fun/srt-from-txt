# .srt file from text files
This only makes it into the srt file format so *certain subtitle editors* do not
complain about "Unable to detect the subtitle format". Note that each line from
the text file becomes one line in the subtitle file.

#### Usage:
Make sure you have Python installed.
1. `./sub.py inputFile1 outputFile1 inputFile2 outputFile2` etc.
   * If you use this method, make sure you have execute permissions on your file.
     Give yourself execute permission on the file by issuing `chmod +x sub.py` at
     the command line if you don't already have it.
2. `python3 sub.py inputFile1 outputFile1 inputFile2 outputFile2` etc.
