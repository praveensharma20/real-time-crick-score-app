from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

headers = {
    'x-rapidapi-key': '56b507f775mshb1a9b6bd744c51ep183a96jsn0dea0ebc36e7',
    'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com'
}

def fetch_cricket_scores():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    response = requests.get(url, headers=headers)
    matches_data = []

    if response.status_code == 200:
        data = response.json()
        type_matches = data.get("typeMatches", [])
        for match_type in type_matches:
            for series in match_type.get("seriesMatches", []):
                wrapper = series.get("seriesAdWrapper", {})
                for match in wrapper.get("matches", []):
                    match_info = match.get("matchInfo", {})
                    team1 = match_info.get("team1", {}).get("teamName", "")
                    team2 = match_info.get("team2", {}).get("teamName", "")
                    desc = match_info.get("matchDesc", "")
                    status = match_info.get("status", "")
                    match_data = {
                        'Description': desc,
                        'Teams': f"{team1} vs {team2}",
                        'Status': status
                    }
                    matches_data.append(match_data)
    return matches_data

def fetch_upcoming_matches():
    url = 'https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming'
    response = requests.get(url, headers=headers)
    upcoming_matches = []

    if response.status_code == 200:
        data = response.json()
        type_matches = data.get('typeMatches', [])
        for match_type in type_matches:
            for series in match_type.get("seriesMatches", []):
                wrapper = series.get("seriesAdWrapper", {})
                for match in wrapper.get("matches", []):
                    match_info = match.get("matchInfo", {})
                    team1 = match_info.get("team1", {}).get("teamName", "")
                    team2 = match_info.get("team2", {}).get("teamName", "")
                    desc = match_info.get("matchDesc", "")
                    status = match_info.get("status", "")
                    match_data = {
                        'Description': desc,
                        'Teams': f"{team1} vs {team2}",
                        'Status': status
                    }
                    upcoming_matches.append(match_data)
    return upcoming_matches

def fetch_live_matches():
    url = 'https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live'
    response = requests.get(url, headers=headers)
    live_matches = []

    if response.status_code == 200:
        data = response.json()
        type_matches = data.get('typeMatches', [])
        for match_type in type_matches:
            for series in match_type.get("seriesMatches", []):
                wrapper = series.get("seriesAdWrapper", {})
                for match in wrapper.get("matches", []):
                    match_info = match.get("matchInfo", {})
                    team1 = match_info.get("team1", {}).get("teamName", "")
                    team2 = match_info.get("team2", {}).get("teamName", "")
                    desc = match_info.get("matchDesc", "")
                    status = match_info.get("status", "")
                    match_data = {
                        'Description': desc,
                        'Teams': f"{team1} vs {team2}",
                        'Status': status
                    }
                    live_matches.append(match_data)
    return live_matches

@app.route('/')
def index():
    cricket_scores = fetch_cricket_scores()
    upcoming_matches = fetch_upcoming_matches()
    live_matches = fetch_live_matches()
    return render_template('index.html', cricket_scores=cricket_scores, upcoming_matches=upcoming_matches, live_matches=live_matches)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
