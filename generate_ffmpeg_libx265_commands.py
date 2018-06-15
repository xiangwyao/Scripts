#!/
import os

# for file in os.listdir('.'):
#     if file.endswith('mp4') or file.endswith('.avi') or file.endswith('mkv'):
#         filename = file[:-4]
#         print("ffmpeg -y -vsync 0 -i \'" + file + "\'\
#              -c:v hevc_nvenc -preset slow -rc vbr_2pass" + \
#             " -rc-lookahead 32 \'" + filename + "_HEVC.mkv\'")

#######################################
out_file_format = "mp4"
#######################################

def is_expected_format(str):
    if str.endswith('mp4') or str.endswith('mkv') or \
    str.endswith('avi') or str.endswith('mov'):
        return True
    else:
        return False

with os.scandir() as it:
    for entry in it:
        if entry.is_file() and not entry.name.startswith('.') and is_expected_format(entry.name):
            file_name, file_ext = os.path.splitext(entry)
            print("ffmpeg -y -i \'" + entry.path + \
                "\' -c:v libx265" + \
                " -crf 28 -c:s copy \'" + file_name + "_HEVC." + out_file_format + "\'")
        elif entry.is_dir() and not entry.name.startswith('@') and not entry.name.startswith('@'):
            with os.scandir(entry) as inner_it:
                for inner_entry in inner_it:
                    if inner_entry.is_file() and is_expected_format(inner_entry.name):
                        inner_file_name, inner_file_ext = os.path.splitext(inner_entry)
                        print("ffmpeg -y -i \'" + inner_entry.path + 
                            "\' -c:v libx265" + \
                        " -crf 28 -c:s copy \'" + inner_file_name + "_HEVC." + out_file_format + "\'")