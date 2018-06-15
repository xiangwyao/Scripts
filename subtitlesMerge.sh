#/usr/bin/bash

##########################################
find . -name '*.mp4' | sort -k 1.3,1.4 -n > TOC.txt
find . -name '*.srt' | sort -k 1.3,1.4 -n > subtitles.txt

##########################################

sleep 1

##########################################
while read video && read sub <&3; do
	name=$(basename "${video}")
	file_name="${name%.*}"
    ffmpeg -i "${video}" -i "${sub}" -map 0 -map 1 -c copy -c:s mov_text "${file_name}"new.mp4
    mv "${file_name}"new.mp4 "${video}"
done < TOC.txt 3<subtitles.txt

##########################################


