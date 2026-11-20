#!/bin/bash
# bcol.sh leaf  -> crops B leaf both columns, 3 parts each (tags L,R)
for i in "$@"; do
python3 /workspace/scotus/work/cropB.py $i 0.10 0.53 0.10 0.88 3 L
python3 /workspace/scotus/work/cropB.py $i 0.48 0.93 0.10 0.88 3 R
done
