#!/bin/bash
# This script is used to batch convert the April tag images to SVG files
#
# Usage: ./batch_convert.sh -b <start_tag> -e <end_tag> -s <size> -d <output_dir>
# Example: ./batch_convert.sh -b 00050 -e 00070 -s 100mm -d tag36h11/svg
#
########################################################################
# Parsing args
########################################################################
while getopts b:e:s: flag
do
    case "${flag}" in
        b) start_tag_arg=${OPTARG};;
        e) end_tag_arg=${OPTARG};;
        s) size_arg=${OPTARG};;
        d) dir_arg=${OPTARG};;
    esac
done

if [ -z "$start_tag_arg" ];
then
    start_tag=00000
    echo "Start tag not set, using default value: $start_tag";
else
    start_tag=$start_tag_arg
    echo "Start tag: $start_tag";
fi

if [ -z "$end_tag_arg" ];
then
    end_tag=00004
    echo "End tag not set, using default value: $end_tag";
else
    end_tag=$end_tag_arg
    echo "End tag: $end_tag";
fi

if [ -z "$size_arg" ];
then
    size=100mm
    echo "Size not set, using default value: $size";
else
    size=$size_arg
    echo "Size: $size";
fi

if [ -z "$dir_arg" ];
then
    output_dir="tag36h11/svg"
    echo "Output directory not set, using default value: $output_dir";
else
    output_dir=$dir_arg
    echo "Output directory: $output_dir";
fi

########################################################################
# Create output directory if it doesn't exist
########################################################################
wd="$PWD"
cd "$wd"

if [ ! -d "$output_dir" ];
then
    echo "Output directory doesn't exist, creating directory..."
    mkdir -p "$output_dir"
fi

########################################################################
# Batch conversion
########################################################################
echo "Starting batch conversions from tag $start_tag to $end_tag..."

for tag_id in $(seq -w $start_tag $end_tag);
do
    cd "$wd"
    python3 tag_to_svg.py tag36h11/tag36_11_"$tag_id".png "$output_dir"/tag36_11_"$tag_id"_"$size".svg --size="$size"
done

echo "Finished conversions"
