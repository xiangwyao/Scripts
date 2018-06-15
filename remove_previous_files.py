import os

def is_expected_format(str):
    if str.endswith('mp4') or str.endswith('mkv') or \
    str.endswith('avi') or str.endswith('mov'):
        return True
    else:
        return False

with os.scandir() as it:
    for entry in it:
        if entry.is_file() and is_expected_format(entry.name) and '_HEVC' not in entry.name:
            print("removing => " + entry.path)
            # os.remove(entry.path)
        elif entry.is_dir() and not entry.name.startswith('@') and not entry.name.startswith('.'):
            with os.scandir(entry) as inner_it:
                for inner_entry in inner_it:
                    if inner_entry.is_file() and is_expected_format(inner_entry.name) and \
                        '_HEVC' not in inner_entry.name:
                        print("removing => " + inner_entry.path)
                        # os.remove(inner_entry.path)
                        