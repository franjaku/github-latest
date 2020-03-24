import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    url = "https://api.github.com/users/{}/events".format(username)
    time_stamp = requests.get(url).json()[0]['created_at']

    print(time_stamp)
