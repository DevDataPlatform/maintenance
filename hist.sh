#!/bin/sh

# https://unix.stackexchange.com/a/177781

perl -pe 's/ (\d+)$/"="x($1\/100000)/e' disk-cache.log
