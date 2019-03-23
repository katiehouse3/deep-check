# Get the full list of followers of a particular user
list_of_followers=[]

current_cursor = tweepy.Cursor(api.followers_ids, screen_name="cocoweixu", count=5000)
current_followers = current_cursor.iterator.next()
list_of_followers.extend(current_followers)
next_cursor_id = current_cursor.iterator.next_cursor

while(next_cursor_id!=0):
	current_cursor = tweepy.Cursor(self.api.followers_ids, screen_name="cocoweixu", count=5000,cursor=next_cursor_id)
	current_followers=current_cursor.iterator.next()
	list_of_followers.extend(current_followers)
	next_cursor_id = current_cursor.iterator.next_cursor
# Get a particular user's timeline (up to 200 of his/her most recent tweets)
status_cursor = tweepy.Cursor(api.user_timeline, screen_name="billybob", count=200,tweet_mode='extended')
status_list = status_cursor.iterator.next()