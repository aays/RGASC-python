'''
fileparser.py - contains basic functions to perform file operations
'''

class fo:
    def __init__(self, fname):
        self.fname = fname
        self.fname_length = len(fname)
        self.fname_extension = self.get_extension(fname)
    
    def get_extension(self, fname):
        # use this to introduce methods and attributes
        i = fname.rfind('.')
        extension = fname[i+1:]
        return extension
    
    def convert_to_list(self):
        lines = []
        with open(self.fname) as f:
            for line in f:
                lines.append(line.rstrip('\n'))
        return lines
    
    def convert_to_dict(self):
        dict_out = {}
        with open(self.fname) as f:
            for i, line in enumerate(f):
                dict_out[i] = line.rstrip('\n')
        return dict_out
