#/usr/bin/bash

##########################################

OUTPUT_FILE=$(basename "$(pwd)").mp4

##########################################

if [ -e mylist.txt ]
then
	rm mylist.txt
fi

if [ -e "${OUTPUT_FILE}" ]
then rm "${OUTPUT_FILE}"
fi



##########################################
tree . > Table_Of_Contents.txt
find . -name '*.mp4' | sort -k 1.3,1.4 -n > TOC.txt

##########################################

while read video; do
    printf "file '%s'\n" "$video" >> mylist.txt
done < TOC.txt

##########################################


##########################################
ffmpeg -f concat -safe 0 -i mylist.txt -c copy -c:s copy "${OUTPUT_FILE}"
##########################################



rm TOC.txt mylist.txt
##########################################