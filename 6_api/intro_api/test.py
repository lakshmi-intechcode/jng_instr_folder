import requests

# spell = requests.get("http://spell-buddy.herokuapp.com/api/spells?name=magic%20missile").json()

# print(spell)

response = requests.get("http://www.omdbapi.com/?s=kill%20bill").json()

print(response)