#!/bin/sh

# https://stackoverflow.com/a/7180078

for file in /proc/*/status ; 
  do awk '/Tgid|VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; 
done | grep kB  | sort -k 3 -n
