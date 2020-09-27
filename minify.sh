#!/bin/bash

for file in $(echo src/*); do
    target=$(basename "$file")
    minify "$file" > "$target"
    sed -i 's/tutor-window/tw/g' "$target"
    sed -i 's/tutor-container/tc/g' "$target"
    sed -i 's/tutor-completed/tm/g' "$target"
    sed -i 's/tutor-cursor/tr/g' "$target"
    sed -i 's/tutor-uncompleted/tu/g' "$target"
    sed -i 's/tutor-result/te/g' "$target"
    sed -i 's/tutor-status/ts/g' "$target"
    sed -i 's/current-layout/cl/g' "$target"

    sed -i 's/KEYS/K/g' "$target"
    sed -i 's/BACKSPACE/B/g' "$target"
    sed -i 's/SHIFT/S/g' "$target"
    sed -i 's/SPACE/C/g' "$target"
    sed -i 's/KEY_O/N/g' "$target"
    sed -i 's/KEY_Z/Z/g' "$target"
    sed -i 's/COMMA/M/g' "$target"
    sed -i 's/DASH/D/g' "$target"
    sed -i 's/PERIOD/P/g' "$target"
    sed -i 's/FORWARD_SLASH/F/g' "$target"

done 


script=$(grep -Eoz "<script>.*</script>" index.html | tr "\0" "\n" )

script=${script#"<script>"}
script=${script%"</script>"}
script=$(curl -X POST -s --data-urlencode "input=${script}" https://javascript-minifier.com/raw)

script="<script>$script</script>"
export script
html=$(<index.html)
echo "$html" | tr -d "\n" | sed 's;<script>.*</script>;${script};g' | envsubst > index.html
wc -c index.html
