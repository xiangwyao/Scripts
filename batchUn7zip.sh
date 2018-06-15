#/usr/bin/bash

for file in *.7z
do
	while IFS='' read -r line || [[ -n "$line" ]]; do
		7z x -aoa -p"$line" "$file"
		if [[ $? = 0 ]]; then break
		fi
	done < pass.txt

done
