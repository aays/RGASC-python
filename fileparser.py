"""
fileparser.py
contains a file object class and more
"""

class fo:
    def __init__(self, fname):
        self.fname = fname
        self.fname_length = len(fname)
    
    def get_extension(self):
        i = self.fname.rfind('.')
        extension = self.fname[i:]
        return extension