import requests
import datetime
import base64

clientID = '04d998b5a376482ab69316599ff9940c'
clientSecret = None
popularityRatings = {'Incredibles': None, 
			'Toy Story': None,
			'A Bugs Life': None,
			'Toy Story 2': None,
			'Monster Inc': None,
			'Finding Nemo': None,
			'Cars': None,
			'Ratatouille': None,
			'WALL-E': None,
			'Up': None}

pixarMovieIDs = {'Incredibles':'5Gqln6CvkfVOlDq1ne1usV', 
			'Toy Story':'47OFnLtLVi5WrPYNXAwFGh',
			'A Bugs Life':'5MYKGPG7eGeLCwk9vteT87',
			'Toy Story 2':'0MCE2KRV2L5NJYMyQNPKHY',
			'Monster Inc':'7hguux6E8wOGlNsKnZB6Sz',
			'Finding Nemo':'2kJpuz9FOqX5riMjGwihhY',
			'Cars':'3Xiz5kq12VOzTw9Kun7m0f',
			'Ratatouille':'7Dr08Oi3zxdCzmFulSXSs2',
			'WALL-E':'2LhcAFdMWcB49mHSxYrqJT',
			'Up':'5yN2LiMaA7nEXT35GW4hNu'}

class SpotifyAuthorization(object):
	accessToken = None
	accessTokenExpires = datetime.datetime.now()
	accessTokenDidExpire = True
	clientID = None
	clientSecret = None
	tokenUrl = "https://accounts.spotify.com/api/token"


	def __init__(self, clientID, clientSecret, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.clientID = clientID
		self.clientSecret = clientSecret

	def getClientCredentials(self):
		clientID = self.clientID
		clientSecret = self.clientSecret
		clientCreds = f"{clientID}:{clientSecret}"
		clientCredsB64 = base64.b64encode(clientCreds.encode())
		return clientCredsB64.decode()

	def getTokenHeader(self):
		clientCredsB64 = self.getClientCredentials()
		return{
			"Authorization": f"Basic {clientCredsB64}"
		}

	def getTokenData(self):
		return{
			"grant_type": "client_credentials"
		}

	def extractAccessToken(self):
		tokenUrl = self.tokenUrl
		tokenData = self.getTokenData()
		tokenHeaders = self.getTokenHeader()
		r = requests.post(tokenUrl, data = tokenData, headers = tokenHeaders)
		print(r.status_code)
		tokenResponseData = r.json()
		return tokenResponseData['access_token']

client = SpotifyAuthorization(clientID, clientSecret)
accessToken = client.extractAccessToken()

def getResourceHeader(Token):
	return{
		"Authorization":f"Bearer {Token}"
	}

def getAlbumPopularity(Token):
	headers = getResourceHeader(Token)
	url = "https://api.spotify.com/v1/albums/5Gqln6CvkfVOlDq1ne1usV"
	r = requests.get(url, headers=headers)
	if r.status_code not in range(200, 299):
		return{}
	print(r.json()) 



