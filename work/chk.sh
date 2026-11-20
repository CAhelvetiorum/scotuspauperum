for i in 1 2 3 4 5; do out=$(bash /workspace/scotus/work/check.sh 2>&1); echo "$out" | grep -q "rendered: 0" || { echo "$out"; exit; }; sleep 2; done; echo "$out"
