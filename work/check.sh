#!/bin/bash
curl -s -o /dev/null localhost:8765/ || (cd /workspace/scotus/docs && nohup python3 -m http.server 8765 >/tmp/srv.log 2>&1 & sleep 1)
google-chrome --headless=new --disable-gpu --no-sandbox --virtual-time-budget=8000 --enable-logging=stderr --v=0 --dump-dom http://localhost:8765/ > /tmp/dom.html 2> /tmp/chrome.err
grep -o "Lemma not found[^\"]*" /tmp/chrome.err | head -20
echo "notes rendered: $(grep -o 'class="note ' /tmp/dom.html | wc -l)"
grep -i "error" /tmp/chrome.err | grep -v "dbus\|gpu\|GPU\|Fontconfig\|sandbox" | head -5
