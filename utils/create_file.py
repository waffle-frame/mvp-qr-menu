import os
from settings.configurations import MEDIA_DIR

def create_folders(place_name: str):
    parent_dir = MEDIA_DIR + place_name

    try:
        os.mkdir(parent_dir)
    except Exception as e:
        print(e)

    try:
        os.mkdir(parent_dir + '/food')
    except Exception as e:
        print(e)

    try:
        os.mkdir(parent_dir + '/banners')
    except Exception as e:
        print(e)

    return
