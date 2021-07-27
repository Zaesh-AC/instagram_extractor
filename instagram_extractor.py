from json.decoder import JSONDecodeError
import os, json
import pandas as pd

from json.decoder import JSONDecodeError


class Extractor():

    def get_dataframe(self, file):
        df = pd.DataFrame()
        with open(file) as f:
            try:
                data = json.load(f)
                df = pd.concat([df, pd.DataFrame(data["photos"])])
            except JSONDecodeError:
                raise ValueError('JSON decode error')
        df["taken_at"] = pd.to_datetime(df["taken_at"])
        df.drop(labels=["location"], axis=1, inplace=True)
        return df

    def get_caption(self, group):
        return group[0][0]

    def get_date(self, group):
        return group[0][1]

    def get_paths(self, group):
        return group[1]["path"]