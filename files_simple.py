import sys
import re

def function(files):
    count=0
    for line in open(files ,'r'):
        count+=1
        line=line.strip()
        r1=re.compile('^.*error.*$|^.*Error.*$')
        
        if r1.match(line):
            s=r1.match(line).groups()
            print count,':',line
   
def main():
    function(sys.argv[1])

if __name__ == "__main__":
    main()
    
