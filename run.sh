#!/bin/bash

exitmsg () {
  echo $1
  exit
}

if [ "$#" -ne 1 ]; then
  exitmsg "Usage: ./run.sh [day]"
fi

pyfile=$1.py
infile=$1_in.txt

if [ ! -f $pyfile ]; then
  exitmsg "No python file $pyfile"
fi

if [ ! -f $infile ]; then
  exitmsg "No input file $infile"
fi

echo "pypy3 $pyfile < $infile"
pypy3 $pyfile < $infile
