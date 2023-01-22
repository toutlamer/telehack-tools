# telehack-tools
telehack random tools, to simplify myself everyday tasks
## ascii.py
Decode the satan.exe hex-dump with a simple copy and paste !

WARNING : the copy and paste should look like this :


    00 | 53 31 69 70 3c 4a 27 48 2d 45 47 1d 04 58 57 7d
    01 | 6e 79 5a 58 06 6e 2f 50 4f 69 17 07 69 1a 5b 6d
    ...
    
Do not put these 2 first lines :

    0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    
The script will regroup the characters by 8, and put a counter on each line.
