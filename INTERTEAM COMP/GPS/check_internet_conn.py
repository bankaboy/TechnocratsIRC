import requests

def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        print("true")
        return True
    except requests.ConnectionError:
        print("false")
    return False

check_internet()
