#!/bin/bash
crun()
{
	./a.out<in.txt>$1
}
jrun()
{
	java $1<in.txt>$2
}
prun()
{
	python $1<in.txt>$2
}
pgm=$1
out=$pgm"out.txt"
err=$pgm"err.txt"
if [ $2=="1" ]
then
	prog=$pgm".c"
	gcc $1>$err
	crun $out &
	kid=$!
elif [ $2=="2" ]
then
	prog=$pgm".py"
	prun $prog $out &
	kid=$!
elif [ $2=="3" ]
then
	prog=$pgm".cpp"
	g++ $prog>$err
	crun $out &
	kid=$!
elif [ $2=="4" ]				
then
	prog=$pgm".java"
	javac $prog>$err
	jrun $1 $out &
	kid=$!
else
	echo "Programming language not supported"
fi
sleep 15
kill -15 $kid