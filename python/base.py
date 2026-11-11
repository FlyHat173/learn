import base64
text = 'lady gaga love bruno mars '
encoded = base64.b64encode(text.encode("utf-8"))
print(encoded.decode("utf-8"))
