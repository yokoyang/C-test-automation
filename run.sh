#!/bin/bash

dir_name="./data/C"
target_dir_name="./data/OUT"

files=$(ls $dir_name)
echo $files
for filename in $files
do
    echo $filename
    name=`echo $filename | cut -d \. -f 1`
    echo $name
    fullname=$target_dir_name"/"$name
    filename=$dir_name"/"$filename
    echo $fullname
    echo $filename
    command `gcc $filename -o $fullname`
done

