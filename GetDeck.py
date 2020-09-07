import requests
id = '5e90ecaa2bbd79003fe3a0a1'

URL = f'https://cardslackingoriginality.com/expansions/{id}/get'
resp = requests.get(URL)
deck = resp.json()["expansion"]
print(deck)
name = deck["name"]
whitecards = deck["whiteCards"]
blackcards = deck["blackCards"]

f = open(f"ignore/{name}_white.txt","w+")

for card in whitecards:
    f.write(card+"\n")
f.close

f = open(f"ignore/{name}_black.txt","w+")

for card in blackcards:
    f.write(card+"\n")
f.close
