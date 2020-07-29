import urllib.request
import re

### Define URL and Header information for XMLHttpRequest
url = 'https://www.robinhoodnetwork.co.uk/stops/9400ZZNOBLV2'
headers = {
    #GET /stops/400ZZNOBLV2 HTTP/1.1
    'Host': 'www.robinhoodnetwork.co.uk',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': '*/*',
    'Accept-Language': 'en,en-US;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.robinhoodnetwork.co.uk/stops/',
    'Cookie': '__cfduid=d96b8e50dcaecaae970507e463f8e42bc1579964796; passenger-favourites-0=%7B%22device%22%3A%228a31be25f3469b76f0b96641e0f2443e%22%2C%22user%22%3Anull%2C%22lastSync%22%3Anull%2C%22favourites%22%3A%5B%5D%7D; cookie_message_viewed=true; _ga=GA1.3.586894754.1579964800; _gid=GA1.3.438284959.1579964800',
    'TE': 'Trailers',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

req = urllib.request.Request(url, headers=headers)

# Try connection and decompress if successful
try:
    response = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except urllib.error.URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    raw_data = response.read()
    if response.info()['Content-Encoding'] == 'br':
        import brotli
        data = str(brotli.decompress(raw_data))
    elif response.info()['Content-Encoding'] == 'gzip':
        import gzip
        data = str(gzip.decompress(raw_data))
    else:
        data = str(raw_data)

    ### uncomment this line for an example data request    
    #data = open("sample_response.txt", encoding="cp1252").read()

    ### Use regex to find all live trams
    p = re.compile('expected">\s[\w]+[\s]*[\w]*')
    matches = [x.strip('expected"> ') for x in p.findall(data)]
    #print(matches)

    outputs["tram_count"] = str(len(matches))
    if int(outputs["tram_count"]) > 1:
        outputs["tram1"] = matches[0]
        outputs["tram2"] = matches[1]
    elif int(outputs["tram_count"]) == 1:
        outputs["tram1"] = matches[0]

    #print(len(matches))
