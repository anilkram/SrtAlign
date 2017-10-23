#!/usr/bin/env python

'''
Anil Ramakrishna | akramakr@usc.edu
Extract text from srt files using pysrt
to prepare them for gentle
'''

import os
import sys
import pysrt
import argparse

class extract_text:
    def __init__(self, srt_file, out_file):
        self.srt_file = srt_file
        self.out_file = out_file

        if not os.path.exists(self.srt_file):
            sys.exit("Srt file doesn't exist")

        if not os.path.exists(os.path.dirname(self.out_file)):
            sys.exit("Output folder doesn't exist")

    def process(self):
        with open(self.out_file, 'w') as outptr:
            subs = pysrt.open(self.srt_file)
            diags = []
            for s in subs:
                d = s.text.strip()
                d = ' '.join([x.strip() for x in d.split('\n')])
                diags.append(d)
            outptr.write('\n'.join(diags))

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Creates srt files from gentle output')
    p.add_argument("srt_file_path", type=str, help="Full path for the srt file")
    p.add_argument("output_file_path", type=str, help="Full path for the output text file")

    a=p.parse_args()

    extract_t = extract_text(a.srt_file_path, a.output_file_path)
    extract_t.process()
