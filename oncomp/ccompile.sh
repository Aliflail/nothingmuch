#!/bin/bash
if [ $2=="1" ]
then
	gcc $1
	./a.out<in.txt>$3
elif [ $2=="2" ]
then
	python $1<in.txt>$3
elif [ $2=="3" ]
then
	g++ $1
	./a.out<in.txt>$3
elif [ $2=="4" ]
then
	javac $1
	java $1<in.txt>$3
else
	echo Programming language not supported
fi

