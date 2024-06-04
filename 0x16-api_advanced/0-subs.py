#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests

def number_of_subscribers(subreddit):
  """Queries the Reddit API to get the number of subscribers for a subreddit.

  Args:
      subreddit: The name of the subreddit to query.

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """

  # Replace 'CLIENT_ID' and 'CLIENT_SECRET' with your actual Reddit app credentials
  url = f"https://api.reddit.com/r/{subreddit}/about.json?limit=1"
  headers = {"Authorization": f"bearer {get_bearer_token()}", "User-Agent": "your_app_name"}

  response = requests.get(url, headers=headers)

  # Check for successful response status code
  if response.status_code == 200:
    data = response.json()
    # Check if data contains 'data' key and 'subscribers' key within 'data'
    if 'data' in data and 'subscribers' in data['data']:
      return data['data']['subscribers']
    else:
      # Subreddit may not exist or data format may have changed
      return 0
  else:
    # API request failed
    return 0

def get_bearer_token():
  """ Placeholder function to illustrate obtaining a bearer token
  This function is not implemented here and should be replaced with your 
  logic for obtaining an OAuth bearer token for Reddit API access.

  Returns:
      A bearer token string for Reddit API access.
  """
  # Replace this with your logic to get a bearer token
  # You can use the praw library to simplify Reddit API authentication
  raise NotImplementedError("Replace this with your logic to get a bearer token")

if __name__ == "__main__":
  # Example usage
  subreddit_name = input("Enter subreddit name: ")
  number_of_subscribers = number_of_subscribers(subreddit_name)
  print(f"Subscribers for r/{subreddit_name}: {number_of_subscribers}")
