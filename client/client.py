import urllib.request

fp = urllib.request.urlopen("http://localhost:8080/")

encoded_content = fp.read()
decoded_content = encoded_content.decode("utf-8")

print(decoded_content)

fp.close()
