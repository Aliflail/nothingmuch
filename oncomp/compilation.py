from subprocess import call
from models import answer
class play():
    def __init__(prog,pname,lan,outp):
        self.pgm=prog
        self.name=pname
        self.language=lan
        self.output=outp
    def compiler():
             pgm=self.name
             c=self.language
             prog=self.pgm
             out=pgm+".txt"
        if(c is 1):
	        pgm+=".c"
            f=open(pgm,"w")
            f.write(prog)
            f.close()
	        call("./ccompile.sh %s %s %s" %(pgm,str(c),out),shell=True)
        elif(c is 2):
	        pgm+=".py"
            f=open(pgm,"w")
            f.write(prog)
            f.close()
	        call("./ccompile.sh %s %s %s" %(pgm,str(c),out),shell=True)
        elif(c is 3):
	        pgm+=".cpp"
            f=open(pgm,"w")
            f.write(prog)
            f.close()
	        call("./ccompile.sh %s %s %s" %(pgm,str(c),out),shell=True)
        elif(c is 4):
	        pgm+=".java"
            f=open(pgm,"w")
            f.write(prog)
            f.close()
	        call("./ccompile.sh %s %s %s" %(pgm,str(c),out),shell=True)
        else:
            print "\nLanguage not supported"
        
    def getoutput():
        o=self.name
        o=o+"out"
        o=o+".txt"
        f=open(o,"r")
        f.read(p)
        return p