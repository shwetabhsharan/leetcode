import uuid

class Codec:

    def __init__(self):
        self.mapping = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        tinyurl = "www.tinyurl.com/{}/".format(str(uuid.uuid4())[:6])
        self.mapping[tinyurl] = longUrl
        return tinyurl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.mapping[shortUrl]

# Your Codec object will be instantiated and called as such:
codec = Codec()
short = codec.encode("www.google.com")
print short
longU = codec.decode(short)
print longU