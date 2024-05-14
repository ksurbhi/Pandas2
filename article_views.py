# Article Views I
import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # df = views[(views['author_id']) == (views['viewer_id'])]
    # df = df.drop_duplicates(subset=['author_id'])
    # df = df[['author_id']].rename(columns= {'author_id':'id'})
    # #DataFrame.sort_values(by, *, axis=0, ascending=True, 
    # #inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
    # return df.sort_values(by='id')
    ####################### OR ####################

    df = views[(views['author_id']) == (views['viewer_id'])]
    df.drop_duplicates(subset = 'author_id', inplace = True)
    df.sort_values(by ='author_id',inplace = True)
    return df[['author_id']].rename(columns = {'author_id':'id'})
    
