# -*- coding: utf-8 -*-
# 
# The MIT License (MIT)
# 
# (C) முத்தையா அண்ணாமலை 2013-2015
# 

import codecs
from tamil import utf8

class Corpus:
    def __init__(self,filename):
        self.filename = filename
        self.handle = None
    def __del__(self):
        try:
            self.handle.close()
        except Exception as e:
            pass    
    def next_tamil_letter(self):
        self.handle = codecs.open(self.filename,'r','utf-8')
        for letter in utf8.get_letters(self.handle.read()):
            if ( utf8.istamil( letter ) ):
                yield letter
        raise StopIteration