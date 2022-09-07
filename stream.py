import json
import pprint
import sseclient

# def with_urllib3(url, headers):
#     """Get a streaming response for the given event feed using urllib3."""
#     import urllib3
#     http = urllib3.PoolManager()
#     return http.request('GET', url, preload_content=False, headers=headers)

def with_requests(url, headers=None):
    """Get a streaming response for the given event feed using requests."""
    import requests
    return requests.get(url, stream=True, headers=headers)


TOKEN = "Tpk_15eaa4b48b1142ff8273d6b8bf63131c"
url = f'https://sandbox-sse.iexapis.com/stable/stocksUS1Second?token={TOKEN}&symbols=spy'
url = f"https://cloud-sse.iexapis.com/stable/stocksUS\?symbols\=spy\&token\={TOKEN}"
# url = f"https://sandbox-sse.iexapis.com/stable/forex\?symbols\=USDCAD\&token\={TOKEN}"
headers = {
    'Accept': 'text/event-stream'
}

wikipedia = "https://stream.wikimedia.org/v2/stream/recentchange"

response = with_requests(url, headers=headers)  # or with_requests(url, headers)
if response.status_code == 200:
    client = sseclient.SSEClient(response)
    print(dir(client))
    for event in client.events():
        print(event.data)
        print('hello')
else:
    print(response.text)