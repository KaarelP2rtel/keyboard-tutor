#!/bin/bash

for file in $(echo src/*); do
    minify "$file" > $(basename "$file")
done 