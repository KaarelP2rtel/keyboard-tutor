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
done 

# .tutor-window{
#     width: 75vw;
#     padding: 1vh;
#     position: absolute;
#     top: 50%;
#     left: 50%;
#     transform: translate(-50%, -50%);
#     font-family: 'Courier New', Courier, monospace;
# }
# .tutor-container{
#     font-size: 0;
#     display: inline;
#     white-space: nowrap;
# }
# .tutor-completed{
#     color: gray;
#     font-size: 4vh;
#     white-space: pre-wrap;
# }
# .tutor-cursor{
#     color: red;
#     font-size: 4vh;
#     text-decoration: underline;
#     white-space: pre-wrap;

# }
# .tutor-uncompleted{
