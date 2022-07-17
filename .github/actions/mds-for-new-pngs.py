import sys, getopt, re
from os import listdir
from os.path import isfile, join

def combDir_unmatchedPngs(inDir):
    files_present = [file for file in listdir(inDir) if isfile(join(inDir, file))]
    pngCheck = lambda a: re.match(".*\.png"gm, a)
    pngFiles = list(filter(pngCheck, files_present))

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "i:")
    except getopt.GetoptError:
        print "mds-for-new-pngs.py -i <directory> -r <True for total refresh|False for only new .pngs>"
        sys.exit(2)
    
    dir = ""

    for opt, arg in opts:
        if opt == "-i":
            dir = arg
        else:
            assert False, "Unknown option"


if __name__ == '__main__':
    main(sys.argv[1:])