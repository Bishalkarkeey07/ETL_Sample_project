import requests
from requests_oauthlib import OAuth1Session
import os
import json
import time
import pandas as pd
from queue import Queue
import threading
from concurrent.futures import ThreadPoolExecutor

os.environ['consumer_key'] = 'GzHWsQKxBeZIBHuijooGwx9t8'
os.environ['consumer_secret_key'] = 'TSGTXYND8UoO12LcYIMQbfzqVyrFR7rE4auyyQfKoqoTXLpBLM'

class Twitter_Proj:
    
    def __init__(self):
        self.consumer_key = os.environ.get('consumer_key')
        self.consumer_secret_key = os.environ.get('consumer_secret_key')
        self.fields = "created_at,description,entities,id,location,name,public_metrics,url,username,verified,withheld"
        self.params = {"user.fields":self.fields}
    
    def request_token(self):
        request_token_url = "https://api.twitter.com/oauth/request_token"
        oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret_key)

        try:
            fetch_response = oauth.fetch_request_token(request_token_url)
            self.resource_owner_key = fetch_response.get("oauth_token")
            self.resource_owner_secret = fetch_response.get("oauth_token_secret")
            print("Got OAuth token: %s" % self.resource_owner_key)
        except ValueError:
            print("There may have been an issue with the consumer_key or consumer_secret you entered.")
        
        return self.resource_owner_key, self.resource_owner_secret
    
    def get_authorization(self):
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret_key,
                              resource_owner_key=self.resource_owner_key, resource_owner_secret=self.resource_owner_secret)
        authorization_url = oauth.authorization_url(base_authorization_url)
        print("Please go here and authorize: %s" % authorization_url)
        verifier = input("Paste the PIN here: ")
        
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret_key,
                              resource_owner_key=self.resource_owner_key, resource_owner_secret=self.resource_owner_secret,
                              verifier=verifier)
        
        try:
            oauth_tokens = oauth.fetch_access_token(access_token_url)
            access_token = oauth_tokens.get('oauth_token')
            access_token_secret = oauth_tokens.get('oauth_token_secret')
            print("Got access token: %s" % access_token)
        except ValueError:
            print("There may have been an issue with the verifier or access token URL.")
        
        self.oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret_key,
                                   resource_owner_key=access_token, resource_owner_secret=access_token_secret)
        
    def make_request(self, url):
        response = self.oauth.get(url, params=self.params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Request failed with status code %d" % response.status_code)
            return None
    
    def producer(self, url):
        while True:
            response = self.make_request(url)
            self.queue.put(response) 
            time.sleep(1)
            
    def consumer(self):
        while True:
            response = self.queue.get()  # Dequeue the response
            print(response)
            time.sleep(1)
            self.queue.task_done()
            
    def start(self, url, num_producers=2, num_consumers=2):
        with ThreadPoolExecutor(max_workers=num_producers + num_consumers) as executor:
            for i in range(num_producers):
                executor.submit(self.producer, url)
            for j in range(num_consumers):
                executor.submit(self.consumer)    
    
    def change_to_dataframe(self, data):
        if data:
            return pd.DataFrame(data)
        else:
            return None
        

twitter_proj = Twitter_Proj()
twitter_proj.request_token()
twitter_proj.get_authorization()


url = "https://api.twitter.com/2/users/me"
twitter_proj.start(url, num_producers=2, num_consumers=2)

response = twitter_proj.make_request(url)



if response.get('data'):
    data_dict = response['data']
    for key, value in data_dict.items():
        if key == 'public_metrics':
            print('public_metrics:')
            for sub_key, sub_value in value.items():
                print(f'    {sub_key}: {sub_value}')
        else:
            print(f'{key}: {value}')



if 'public_metrics' in response:
    public_metrics = response.pop('public_metrics')
    for key, value in public_metrics.items():
        response[key] = value

df = pd.DataFrame([response])  # Convert the dictionary to a dataframe
if df is not None:
    print(df.to_string(index=False))


df.head()
metrics = df.public_metrics[['followers_count', 'following_count', 'tweet_count', 'listed_count']]
metrics

metrics.to_csv('public_metrics.csv', index=False)
df.to_csv('twitter_data.csv', index=False)