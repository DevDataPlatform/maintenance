#!/bin/sh

grep "^Cached:" /proc/meminfo | awk -v now="$(date +'%Y-%m-%dT%H:%M')"  '{print now " " $2}'