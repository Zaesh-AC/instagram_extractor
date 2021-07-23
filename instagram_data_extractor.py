#!/usr/bin/python3

import os, json, subprocess, sys
import pandas as pd

MEDIA_DIR = 'media/'


class Extractor():

    def get_dataframe(self):
        df = pd.DataFrame()
        for filename in os.listdir(MEDIA_DIR):
            with open(f'{MEDIA_DIR+filename}') as f:
                data = json.load(f)
                df = pd.concat([df, pd.DataFrame(data["photos"])])
        df["taken_at"] = pd.to_datetime(df["taken_at"])
        df.drop(labels=["location"], axis=1, inplace=True)
        return df

    def get_caption(self, group):
        return group[0][0]

    def get_date(self, group):
        return group[0][1]

    def get_paths(self, group):
        return group[1]["path"]

if __name__ == '__main__':
    if not sys.platform == 'linux':
        raise ('Sorry, this script will not work on your Operating System :( ')
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