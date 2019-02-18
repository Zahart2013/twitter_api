import urllib.request, urllib.error
import twurl
import json
import ssl


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


def downloader(acct, twitter):

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print('')
    url = twurl.augment(twitter,
                        {'screen_name': acct})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    with open("data.json", "w") as json_file:
        json.dump(json.loads(data), json_file)
    return acct


if __name__ == '__main__':
    username = input("Enter Twitter username: ")
    downloader(username, TWITTER_URL)
