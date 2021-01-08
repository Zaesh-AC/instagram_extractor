#!/usr/bin/python3

import os
import json
import subprocess
import pandas as pd

MEDIA_DIR = 'media/'

def get_dataframe():
    df = pd.DataFrame()
    for filename in os.listdir(MEDIA_DIR):
        with open(f'{MEDIA_DIR+filename}') as f:
            data = json.load(f)
            df = pd.concat([df, pd.DataFrame(data["photos"])])
    df["taken_at"] = pd.to_datetime(df["taken_at"])
    df.drop(labels=["location"], axis=1, inplace=True)
    return df

def get_caption(group):
    return group[0][0]

def get_date(group):
    return group[0][1]

def get_paths(group):
    return group[1]["path"]

if __name__ == '__main__':
    df = get_dataframe()
    for group in df.groupby(["caption", "taken_at"], axis=0):
        caption = get_caption(group)
        taken_at = get_date(group)
        subprocess.run(f'mkdir "output/{taken_at}"', shell=True)
        if caption != '':
            with open(f'output/{taken_at}/caption.txt', 'w') as file:
                file.write(caption)
        for path in get_paths(group):
            subprocess.run(f'cp {path} "output/{taken_at}"', shell=True)