#!/usr/bin/python3

import subprocess
from instagram_extractor import Extractor

if __name__ == '__main__':
    extractor = Extractor()
    df = extractor.get_dataframe()
    for group in df.groupby(["caption", "taken_at"], axis=0):
        caption = extractor.get_caption(group)
        taken_at = extractor.get_date(group)
        subprocess.run(f'mkdir "output/{taken_at}"', shell=True)
        if caption != '':
            with open(f'output/{taken_at}/caption.txt', 'w') as file:
                file.write(caption)
        for path in extractor.get_paths(group):
            subprocess.run(f'cp {path} "output/{taken_at}"', shell=True)