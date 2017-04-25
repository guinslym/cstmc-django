import unittest
import os
import sys
from bs4 import BeautifulSoup
import lxml
import pdb
import codecs
import time
import datetime
import numpy as np
import pandas as pd
import json
import wget
from threading import Thread
import io

import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s - (%(lineno)d) - %(message)s')

logFile = 'myapp.log'

my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, 
                                 backupCount=2, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)

app_log.addHandler(my_handler)


app_log.info('Started')
app_log.error('Started')
app_log.warn('Started')
app_log.critical('Finished')

def read_ddi_file(filename):
	"""
	Read the XML file

	return: return the content of the XML file
	"""
	soup = BeautifulSoup(codecs.open(filename), 'xml')
	return False

start_time = time.time()



from pprint import pprint

d = {}
with open("cstmc-CSV-en.csv") as f:
    headers = [header.strip() for header in next(f).split("|")[1:]]

    for line in f:
        values = [value.strip() for value in line.split("|")]
        d[values[0]] = dict(zip(headers, values[1:]))

images =[]
for i in d.keys():
	if len(d.get(i).get('image') )  != 0:
		#pprint(d.get(i).get('image'))
		#pprint(d.get(i).get('thumbnail'))
		#logger.info(d.get(i).get('image'))
		images.append(d.get(i).get('image'))
		images.append(d.get(i).get('thumbnail'))

images = set(images)
pprint(len(images))
pprint(len(set(images)))

def write_a_json_file_for_the_database(artefact, dataset_name):
    with io.open(dataset_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(artefact, ensure_ascii=True, indent=4 ))


def create_a_list_of_list(data):
    final_list=[]
    b =[]
    # You don't need `a` to be a list here, just iterate the `range` object
    for num in data:
        if len(b) < 10:
            b.append(num)
        else:
            # Add `b` to `final_list` here itself, so that you don't have
            # to check if `b` has 3 elements in it, later in the loop.
            final_list.append(b)

            # Since `b` already has 3 elements, create a new list with one element
            b = [num]

    # `b` might have few elements but not exactly 3. So, add it if it is not empty
    if len(b) != 0:
        final_list.append(b)

    return final_list

def send_this_data_to_the_thread_function(data_list_json):
    for list_of_list in data_list_json:
        threadlist = []
        #for u in list_of_list:
        #download_image(u)
        for u in list_of_list:
            t = Thread(target=download_image, args=(u,))
            t.start()
            threadlist.append(t)
        for b in threadlist:
            b.join()

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
                #move the file
                os.rename(f, "images/"+f)

def download_image(url):
    try:
    	wget.download(url)
    except:
    	app_log.critical(url)

#write_a_json_file_for_the_database(images, 'images.json')

#images = list(images)
#data_list_json = create_a_list_of_list(images)
#send_this_data_to_the_thread_function(data_list_json)
#cleaning_this_directory()
#seconds = (time.time() - start_time)
#time_in_total = str(datetime.timedelta(seconds=seconds))
#print("Time took to download\nall the dataset => {0}".format(time_in_total))

write_a_json_file_for_the_database(d, 'hello-fr.json')
#total images 128,366