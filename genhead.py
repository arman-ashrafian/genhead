#!/usr/bin/python3.7

import sys
import os

def main():
    if len(sys.argv) == 1: 
        print('missing argument')
        sys.exit(1)
    
    for fi in sys.argv[1:]:
        if "." in fi: genhead(fi)
            
def genhead(fileName):
    f = open(fileName, "w")

    dirName = os.path.basename(os.getcwd()).upper()
    fileName = fileName[:fileName.index('.')].upper()
    headerName = '%s_%s_H' % (dirName, fileName) 
    
    ifndef = '#ifndef %s' % (headerName)
    define = '#define %s' % (headerName)
    endif  = '#endif /* %s */' % (headerName)

    f.write('%s\n%s\n\n\n%s' % (ifndef, define, endif))
    f.close()

if __name__ == '__main__':
    main()


