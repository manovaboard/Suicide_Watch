SELECT author, id, created_utc, title, selftext FROM [fh-bigquery:reddit_posts.2016_11]
WHERE 1=1
AND lower(subreddit) = 'suicidewatch';