import urllib.request
# date = 20180331
# perfect_game = 'perfect_game'

url = 'https://www.draftkings.com/contest/exportfullstandingscsv/54847274'  
# urllib.request.urlopen(url)


 
# url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
 

...

response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary

# date = 20180331
# perfect_game_url_1 = 'https://www.draftkings.com/contest/exportfullstandingscsv/54847274'






# open('dk_mlb_%s_%d_raw.csv' % (perfect_game, date), 'wb').write(r.content)

# def is_downloadable(url):
#     """
#     Does the url contain a downloadable resource
#     """
#     h = requests.head(url, allow_redirects=True)
#     header = h.headers
#     content_type = header.get('content-type')
#     if 'text' in content_type.lower():
#         return False
#     if 'html' in content_type.lower():
#         return False
#     return True

# print(is_downloadable('https://www.draftkings.com/contest/exportfullstandingscsv/54847274'))






# def get_filename_from_cd(cd):
#     """
#     Get filename from content-disposition
#     """
#     if not cd:
#         return None
#     fname = re.findall('filename=(.+)', cd)
#     if len(fname) == 0:
#         return None
#     return fname[0]


# url = 'http://google.com/favicon.ico'
# r = requests.get(perfect_game_url_1, allow_redirects=True)
# filename = get_filename_from_cd(r.headers.get('content-disposition'))
# open('dk_mlb_%s_%d_raw.csv' % (perfect_game, date), 'wb').write(r.content)

# urlretrieve(perfect_game_url_1, "dk_mlb_%s_%d_raw.csv" % (perfect_game, date))

