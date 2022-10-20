import hashlib
import hmac

key = "Secret Key"
message = "Lara"
h = hmac.new(key.encode(), message.encode(), hashlib.sha512).hexdigest()

print("HMAC Code for Verification of Msg:",h)
