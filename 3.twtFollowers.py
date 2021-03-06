import time
from TwitterAPI import TwitterAPI
consumer_key = 'eiavHcTexJq6Sw1AhMoEeH48P'
consumer_secret = '9XMCHgEtOO1xHG6zsEjuVEFrG5NDJ4way0jAu1acU5nVyXnJmI'
def list_followers_by_screen_name(screen_name):
	counter= 0
def show_user_list( response ):
	counter = 0
	for u in response['users']:
		print("HANDLE: " + u['screen_name'] + "	||nm: " + u['name'] + "||following: " + str(u['friends_count']) + "	||followers: " + str(u['followers_count']))
		counter += 1
api = TwitterAPI(consumer_key,consumer_secret,auth_type='oAuth2')
varname = open("/root/Desktop/TARGET_HANDLES","r")
stlst = []
for line in varname.readlines():
	stlst.append(line.strip())
lst = set(stlst)
varname.close()
print ("\n*************** Purpose : Followers Analysis, Deeper Mining for more Suspicious Handles ***************")
print ("0.) Make sure you have sufficiently minimized TARGET_HANDLES")
print ("1.) You will have to manually analyze and Copy-paste Anti-National followers Handles in (One)1 Anti-National Handle/Line format in TARGET_HANDLES file")
print ("2.) You may also optimize SEARCH_TERMS based on your experience")
print ("3.) You may save results for future analysis/checks")
for n in lst:
	cursor = -1
	print ("********************" + n)
	r = 1
	time.sleep(120)
	while cursor != 0:
		time.sleep(30)
		response= api.request( 'followers/list',{'screen_name':n, 'cursor':cursor} ) ##enter twitter username only
		assert response.status_code == 200, "Request failed:{text}\n{headers}".format_map(vars(response))
		if r < 16: 
			body= response.json()
			show_user_list(body)
			cursor= body['next_cursor']
			r = r + 1
		else:
			break
##print( "Total {counter}".format_map(vars) )
