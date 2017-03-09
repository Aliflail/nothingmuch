from subprocess import call
import os
from models import answer
class play():
    def __init__(prog,pname,lan,outp):
        self.pgm=prog
        self.name=pname
        self.language=lan
        self.output=outp
    def run(pgm,out,c):
            f=open(pgm,"w")
            f.write(prog)
            f.close()
	        call("./ccompile.sh %s %s %s" %(pgm,str(c)),shell=True)
            self.output=getoutput(out)
            os.remove(out)
            os.remove(pgm)
    
    def compiler():
             pgm=self.name
             c=self.language
             prog=self.pgm
             out=pgm+"out"
             out=out+".txt"
             run(pgm,out,c)
             if c>4:
                 print "\nLanguage not supported"
        
    def getoutput(o):
        f=open(o,"r")
        p=f.read()
        return p