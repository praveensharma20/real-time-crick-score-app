import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
headers= {
    'x-rapidapi-key': '56b507f775mshb1a9b6bd744c51ep183a96jsn0dea0ebc36e7',
    'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com'
  }

response = requests.get(url, headers=headers)
print(response.json())