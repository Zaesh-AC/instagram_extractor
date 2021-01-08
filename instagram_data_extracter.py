#!/usr/bin/python

import os
import json
import pandas as pd

def get_dataframe():
    f = open('data/media.json')
    f1 = open('data/media (1).json')
    f2 = open('data/media (2).json')
    f3 = open('data/media (3).json')
    f4 = open('data/media (4).json')
    f5 = open('data/media (5).json')
    f6 = open('data/media (6).json')
    data = json.load(f)
    data1 = json.load(f1)
    data2 = json.load(f2)
    data3 = json.load(f3)
    data4 = json.load(f4)
    data5 = json.load(f5)
    data6 = json.load(f6)
    df = pd.DataFrame(data['photos'])
    df = pd.concat([df,
               pd.DataFrame(data1['photos']),
              pd.DataFrame(data2['photos']),
              pd.DataFrame(data3['photos']),
              pd.DataFrame(data4['photos']),
              pd.DataFrame(data5['photos']),
              pd.DataFrame(data6['photos']),
               ])
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
        os.system(f'mkdir "output/{taken_at}"')
        if caption != '':
            with open(f'output/{taken_at}/caption.txt', 'w') as file:
                file.write(caption)
        for path in get_paths(group):
            os.system(f'cp {path} "output/{taken_at}"')
