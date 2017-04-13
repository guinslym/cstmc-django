import timeago
import timeago, datetime
from dateutil import parser
import os, time

def cleaning_this_directory():
    """After downloading all the XML dataset
    and after parsing the xml file to be able to create a
    json file. This FUNCTION will move all the .xml and .json
    to the directory ./json or ./xml
    """
    import os, shutil
    files = os.listdir(".")
    for f in files:
        if os.path.isfile(f):
            extension = f.split(".")[-1]
            if extension == 'png':
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(f)
                im2 = time.ctime(ctime)
                im2  = parser.parse(im2)
                now = datetime.datetime.now()
                res = timeago.format(im2, now)
                if 'minutes' in res:
                    print('moving {0}'.format(f))
                    #move the file
                    os.rename(f, "images/"+f)

while True:
    cleaning_this_directory()
    print("Starting waiting at {0}: ".format(datetime.datetime.now()))
    time.sleep(60*3)