
url = "https://alu-intranet.hbtn.io/status"

req = Request("GET", url)

if __name__ == "__main__":
    """body response.
    """
    response = requests.get(url)
    print("Body response:\t")