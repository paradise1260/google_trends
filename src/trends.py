import argparse
import os
import pandas as pd
from pytrends.request import TrendReq


def download_trend(keyword="bitcoin", geo="CA", timeframe="today 5-y", dir="data"):
    """
    Downloads the trend data of the specified keywrod from Google trends and
    saves it into a csv file called trend.csv in the specified directory

    Parameters
    ----------
    keyword : str
        The keyword for searching on Google trends

    geo : str
        The country code for searching on Google trends

    timeframe: str
        The time period for searcing on Google trends

    dir: str
        The directory where to save the csv file

    Returns
    -------
    None
    """
    pytrends = TrendReq()
    pytrends.build_payload([keyword], geo=geo, timeframe=timeframe)
    trend = pytrends.interest_over_time()[keyword]

    trend = pd.DataFrame(trend)
    if not os.path.exists(dir):
        os.makedirs(dir)
    path = os.path.join(dir, "trend.csv")
    trend.to_csv(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--keyword",
        type=str,
        help="The keyword for searching on Google trends",
        default="bitcoin",
    )
    parser.add_argument(
        "--geo",
        type=str,
        help="The country code for searching on Google trends",
        default="CA",
    )
    parser.add_argument(
        "--timeframe",
        type=str,
        help="The time period for searcing on Google trends",
        default="today 5-y",
    )
    parser.add_argument(
        "--dir",
        type=str,
        help="The directory where to save the csv file",
        default="data",
    )

    args = parser.parse_args()
    download_trend(args.keyword, args.geo, args.timeframe, dir=args.dir)
