import time
from TwitterAPI import TwitterAPI
consumer_key = 'eiavHcTexJq6Sw1AhMoEeH48P'
consumer_secret = '9XMCHgEtOO1xHG6zsEjuVEFrG5NDJ4way0jAu1acU5nVyXnJmI'
def tweets_by_screen_name(screen_name):
	api = TwitterAPI(consumer_key,consumer_secret,auth_type='oAuth2')
	response= api.request( 'statuses/user_timeline',{'screen_name':screen_name, 'count':20} )
	for item in response.json():
		text= item['text']
		entities= item['entities']
# entities include $symbols, @user_mentions, #hashtags, urls, media
		sym_list = [s['text'] for s in entities['symbols']]
		user_list = [u['screen_name'] for u in entities['user_mentions']]
		hash_list = [h['text'] for h in entities['hashtags']]
		url_list = [u['expanded_url'] for u in entities['urls']]
		if 'media' in entities:
			media_list = [m['media_url'] for m in entities['media']]
		else:
			media_list = []
			print("\n" +  item['text'], "$", sym_list, "@", user_list, hash_list, url_list, media_list)
varname = open("/root/Desktop/TARGET_HANDLES","r")
stlst = []
for line in varname.readlines():
	stlst.append(line.strip())
lst = set(stlst)
varname.close()
print ("\n************* Purpose : Verify Suspicious Handles based on their Conversations ****************")
print ("1.) Review the content within each HANDLE. You may also search for DANGER_TERMS")
print ("2.) If a HANDLE is/will not post(ing) anything dangerous/suspicious then Remove that HANDLE(es) from TARGET_HANDLES ")
print ("3.) Repeat the above steps regularly/several times to minimize TARGET_HANDLES as much as possible.")
for n in lst:
	print("**************" + n)
	time.sleep(10)
	tweets_by_screen_name(n)
