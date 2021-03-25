#!/bin/bash

for file in $(echo src/*); do
    target=$(basename "$file")
    minify "$file" > "$target"
    sed -i 's/tutor-window/a/g' "$target"
    sed -i 's/tutor-container/b/g' "$target"
    sed -i 's/tutor-completed/c/g' "$target"
    sed -i 's/tutor-cursor/d/g' "$target"
    sed -i 's/tutor-uncompleted/e/g' "$target"
    sed -i 's/tutor-result/f/g' "$target"
    sed -i 's/tutor-status/g/g' "$target"
    sed -i 's/current-layout/h/g' "$target"
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
