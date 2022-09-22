import requests
import os
import sys
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
# bearer_token = os.environ.get("BEARER_TOKEN")
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAB3mgwEAAAAA8iEo30AoQlm5lTfr6KYws4r6rUw%3DK6nyxFy4z2td694icVksgZdDKs0qJrwClu59BQuD9cXjSMWIQy'

def bearer_oauth_user(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def bearer_oauth_tweet(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def create_url_user(usernames):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    # usernames = "usernames=TwitterDev,TwitterAPI"
    user_fields = "user.fields=description,created_at"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def connect_to_endpoint_user(url):
    response = requests.request("GET", url, auth=bearer_oauth_user,)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def getUserID(usernames):
    url = create_url_user(usernames)
    json_response = connect_to_endpoint_user(url)
    return [x['id'] for x in json_response['data']]


def create_url_tweets(user_ids):
    # Replace with user ID below
    # user_id = 2244994945
    return ["https://api.twitter.com/2/users/{}/tweets".format(x) for x in user_ids]


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}


def connect_to_endpoint_tweet(url, params):
    response = requests.request("GET", url, auth=bearer_oauth_tweet, params=params)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def main(usernames="elonmusk"):
    usernames = "usernames=" + usernames
    user_ids = getUserID(usernames)
    urls = create_url_tweets(user_ids)
    params = get_params()
    json_responses = [connect_to_endpoint_tweet(url, params) for url in urls]
    
    # This prints the most recent tweet
    latestTweets = [x['data'][0]['text'] for x in json_responses]
    for tweet in latestTweets:
        print(tweet)


if __name__ == "__main__":
    # print(sys.argv)
    if len(sys.argv) == 1:
        main()
    else:
        main(sys.argv[1])
