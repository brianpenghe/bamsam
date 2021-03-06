##################################
#                                #
# Last modified 04/27/2012       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
import pysam
import string

def main(argv):

    if len(argv) < 2:
        print 'usage: python %s SAM[,SAM2,SAM3,....,SAMN] outfilename' % argv[0]
        sys.exit(1)

    files = argv[1]
    outputfilename = argv[2]

    outfile = open(outputfilename, "w")

    i=0
    filelist = files.split(',')
    S=0
    for SAM in filelist:
        print SAM
        S+=1
        linelist = open(SAM)
        for line in linelist:
           i+=1
           if i % 5000000 == 0:
               print str(i/1000000) + 'M alignments processed'
           if line.startswith('@'):
               if S==1:
                   outfile.write(line)
               else:
                   pass
               continue
           fields = line.strip().split('\t')
           if fields[2] == '*':
               continue
           else:
               outfile.write(line)

    outfile.close()

if __name__ == '__main__':
    main(sys.argv)

