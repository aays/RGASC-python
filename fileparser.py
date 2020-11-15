class fp:
    def __init__(self, fname):
        self.fname = fname
        self.fname_length = len(fname)
        self.extension = self._get_extension()
        
    def convert_to_list(self):
        fname_lines = []
        with open(self.fname, 'r') as f:
            for line in f:
                fname_lines.append(line.rstrip('\n'))
        return fname_lines

    def _get_extension(self):
        i = self.fname.rfind('.')
        extension = self.fname[i:]
        return extension
    
def package_name():
    print('fileparser!')
    
euler = 2.71828