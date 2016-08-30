import time
from twitter import *
##from TwitterAPI import TwitterAPI
consumer_key = 'eiavHcTexJq6Sw1AhMoEeH48P'
consumer_secret = '9XMCHgEtOO1xHG6zsEjuVEFrG5NDJ4way0jAu1acU5nVyXnJmI'
Access_Token = '740857079267659776-zC3go6UbtXSZRDr4sVbkDOELXrYgQ4j'
Access_Secret = 'dxfioz6l7DM829XfJzJLaUUyjuaZ9V2au6hOrUVQwhcmN'
##api = TwitterAPI(consumer_key,consumer_secret,auth_type='oAuth2')
oauth = OAuth(Access_Token, Access_Secret, consumer_key, consumer_secret)
twitter = Twitter(auth=oauth)
flood = []
lst = []
print ("\n*************** Purpose : Search Suspicious Handles based on search terms ***************")
print ("1.) Make Sure You Have (a well researched) 'SEARCH_TERMS' text file in Desktop in (One)1 Search-Term/line format")
print ("2.) Create a Text File (if not already created) named as 'TARGET_HANDLES' text file in Desktop")
print ("3.) You will have to manually analyze and Copy-paste Anti-National Handles in (One)1 Anti-National Handle/Line format in that file")
stlst = []
var_name = open("/root/Desktop/SEARCH_TERMS","r")
for line in var_name.readlines():
	stlst.append(line.strip())
lst = set(stlst)
var_name.close()
for n in lst:
	print (">>>>>>>>>>>>> Search Term : " + n + "\n")
	time.sleep(10)
	r = n + ' near:India'
	print (r)
	results = twitter.users.search(q = r,count = 200) ##|| &near=me  || set geolocation or geolocalization
##twitter.search.tweets(q='#salman')
	countr = 1
	for user in results:
#		print (user["screen_name"])
		print ( user["screen_name"])# + "	||nm: " + user["name"] + " ||loc : " + user["location"] + " ||Following : " + str(user["friends_count"]) + "	||Followers : " + str(user["followers_count"]))
		if countr > 19:
			print ("\n************************************************************** For More Handles Search on Website / Visit Weblink : ")
			flood.append(n)
		countr = countr + 1
## Although Twitter Arranges (Qualitatively & Quantitatively) Popular groups by itself
print ("For Following Search Terms, Use Twitter (Advanced) Search; Enter 'SEARCH_TERM near:India' to get Handles within India")
print (flood)
