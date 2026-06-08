import hashlib
import requests

class BreachChecker:
    def __init__(self, password):
        self.password = password

    def get_password_hash(self):
        # Convert password to SHA-1 hash and make it uppercase
        sha1_hash = hashlib.sha1(self.password.encode("utf-8")).hexdigest().upper()
        return sha1_hash

    def check_breach(self):
        sha1_hash = self.get_password_hash()

        #Split hash — first 5 chars go to API, rest stays local
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]

        #Send only the first 5 characters to the API
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url)

        if response.status_code != 200:
            return None, "⚠️  Could not reach the breach database. Check your internet."

        #API returns a list of hash suffixes and how many times they appeared
        hashes = response.text.splitlines()

        for line in hashes:
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count), f"🚨 DANGER! This password has been seen in {count} data breaches!"

        return 0, "✅ Good news! This password has never appeared in a known data breach."