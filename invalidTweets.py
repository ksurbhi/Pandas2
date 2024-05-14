# invalid tweets
import pandas as pd
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    is_valid = tweets['content'].str.len() >15
    # print(type(tweets['content']))
    # print(is_valid)
    df= tweets[is_valid]
    return df[['tweet_id']]
