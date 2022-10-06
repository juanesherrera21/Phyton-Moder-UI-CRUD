import cryptocode

str_encoded = cryptocode.encrypt("https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios","qwerty")

## And then to decode it:
str_decoded = cryptocode.decrypt(str_encoded, "qwerty")
