import os
import collections
from pprint import pprint

EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v']
EXT_IMG = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'tiff', 'tiff', 'jfif']
EXT_DOCS = ['txt', 'pdf', 'csv', 'xls', 'ods', 'doc', 'docx', 'html', 'odt', 'tax', 'ppt', 'pptx', 'log']
EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTL = ['dmg', 'exe', 'iso']
EXT_PYTHON = ['py', 'ipynb']


BASE_PATH = os.path.expanduser('~')
DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documents', 'Applications', 'Other', 'Python Files']

for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    if file_name[0] != '.':
        file_ext = file_name.split('.')[-1]
        files_mapping[file_ext].append(file_name)

pprint(files_mapping)

# the code below moves all files given a specific file extension to a target
# directory

for f_ext, f_list in files_mapping.items():

    if f_ext in EXT_INSTL:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Applications', file))

    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Music', file))

    elif f_ext in EXT_VIDEO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Movies', file))

    elif f_ext in EXT_IMG:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Pictures', file))

    elif f_ext in EXT_DOCS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Documents', file))

    elif f_ext in EXT_PYTHON:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Python Files', file))

    elif f_ext in EXT_PYTHON:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Other', file))


