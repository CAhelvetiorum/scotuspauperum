#!/bin/bash
# usage: pg.sh page [n]  -> 3 strips of page text block
for p in "$@"; do python3 /workspace/scotus/work/cropA.py $p 0.03 0.97 0.05 0.83 3 s; done
