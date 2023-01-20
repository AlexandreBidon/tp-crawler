from urllib.parse import urlparse

domain = urlparse('http://www.example.test/foo/bar')
print(domain.scheme +"://" + domain.netloc) # --> www.example.test
