#!/Users/anil/anaconda3/bin/python

# coding: utf-8

'''
Anil Ramakrishna | akramakr@usc.edu
Creates srt files with corrected time boundaries from gentle output
Derived from code by Krishna Somandepalli | somandep@usc.edu
'''

import os
import re
import sys
import pdb
import json
import math
import pysrt
import argparse

def extract_time_tuple(seconds):
    srt_time_elem = pysrt.SubRipTime()
    srt_time_elem.hours = math.floor(seconds/3600)
    srt_time_elem.minutes = math.floor((seconds%3600)/60)
    srt_time_elem.seconds = math.floor((seconds%3600)%60)
    srt_time_elem.milliseconds = math.floor(math.modf((seconds%3600)%60)[0]*1000)

    return srt_time_elem

class extract_srt:
    def __init__(self, json_file_path, output_file_path, input_srt_file_path):
        self.jsonfile = json_file_path
        self.outfile = output_file_path
        self.srtfile = input_srt_file_path

        if not os.path.exists(self.jsonfile):
            sys.exit("Json file doesn't exist")

        if not os.path.exists(os.path.dirname(self.outfile)):
            sys.exit("Output folder doesn't exist")

        if not os.path.exists(self.srtfile):
            sys.exit("Input srt file doesn't exist")

    def process(self):
        gentle_file = self.jsonfile
        out_file = self.outfile
        srt_file = self.srtfile
        
        g = json.load(open(gentle_file,'r'))
        t = g['transcript']
        g_words = [w for w in g['words'] if w['case'] != 'not-found-in-transcript']
        
        sentences = t.split('\n')
        sentences = [sent.replace('-',' ') for sent in sentences]

        inputsrt_elems = pysrt.open(srt_file)        
        assert(len(inputsrt_elems) == len(sentences))

        srt_elems = pysrt.SubRipFile()
        counter = 0
        for sent_i,sent in enumerate(sentences):
            if type(sent) != type(u''):
                sent = sent.decode('utf-8')
        
            words = sent.split()
            start_time_found = False
            for cur_word in words:
                if not re.search(r'(\w|\’\w|\'\w)+', cur_word, re.UNICODE):
                    continue
        
                for w in re.finditer(r'(\w|\’\w|\'\w)+', cur_word, re.UNICODE):
                    word = w.group()
                    gentle_word = g_words[counter]
                    clean_word = re.search(r'(\w|\’\w|\'\w)+', word, re.UNICODE).group()
                    if False:
                        if (clean_word.lower() != gentle_word['word'].lower()):
                            pdb.set_trace()
                            print("Error")
                    else:
                        assert(clean_word.lower() == gentle_word['word'].lower())
            
                    if gentle_word['case']=='success':
                        #Retain first valid time boundary
                        if start_time_found == False:
                            start_time = gentle_word['start']
                            start_time_found = True
            
                        #keep scanning until the last valid time bounday
                        end_time = gentle_word['end']
            
                    counter += 1
       
            if start_time_found == False:
                start_time = inputsrt_elems[sent_i].start
                end_time = inputsrt_elems[sent_i].end
            else:
                start_time = extract_time_tuple(start_time)
                end_time = extract_time_tuple(end_time)
 
            elem = pysrt.SubRipItem()
            elem.index = sent_i +1
            elem.text = sent
            elem.start = start_time
            elem.end = end_time
        
            srt_elems.append(elem)
        
        srt_elems.save(out_file, encoding='utf-8') 

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Creates srt files from gentle output')
    p.add_argument("json_file_path", type=str, help="Full path for json file produced by gentle")
    p.add_argument("output_file_path", type=str, help="Full path for the output srt file")
    p.add_argument("input_srt_file_path", type=str, \
        help="Full path for the srt file input to gentle")

    a=p.parse_args()

    extract_s = extract_srt(a.json_file_path, a.output_file_path, a.input_srt_file_path)
    extract_s.process()

