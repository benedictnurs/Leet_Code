class Codec:
    def __init__(self):
        self.hm = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(5))

        while random_string in self.hm:
            random_string = ''.join(random.choice(characters) for _ in range(5))
        self.hm[random_string] = longUrl
        shortUrl = "http://short.url/" + random_string
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        random_string = shortUrl.split('/')[-1]
        return self.hm.get(random_string, "")        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))