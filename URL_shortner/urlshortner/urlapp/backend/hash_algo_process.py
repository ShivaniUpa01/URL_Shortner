import hashlib


def url_shortner_url_hash_algo(url, length=6):
    sha256_hash = hashlib.sha256(url.encode()).hexdigest()
    short_url = sha256_hash[:length]  # Use the first 6 characters of the hash as the short URL
    return short_url
