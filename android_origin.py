import base64

# android sha256_cert_fingerprints
hash = "FA:C6:17:45:DC:09:03:78:6F:B9:ED:E6:2A:96:2B:39:9F:73:48:F0:BB:6F:89:9B:83:32:66:75:91:03:3B:9C"

hash = hash.split(":")
hash = ''.join(hash)
hash = bytes.fromhex(hash)
hash = base64.urlsafe_b64encode(hash)

print("android:apk-key-hash:" + hash.decode())
