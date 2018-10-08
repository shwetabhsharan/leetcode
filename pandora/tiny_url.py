import uuid

class TinyURL(object):

    url_data = dict()


    def encode(self, url):
        tiny_url = "www.tinyurl.com/{}/".format(str(uuid.uuid4())[:6])
        TinyURL.url_data[tiny_url] = url
        return tiny_url

    def decode(self, tiny_url):
        if tiny_url in TinyURL.url_data:
            return TinyURL.url_data[tiny_url]

obj = TinyURL()
tiny_url = obj.encode("www.google.com")
print obj.decode(tiny_url)