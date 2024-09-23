import requests
from bs4 import BeautifulSoup

# Sample URLs for testing purposes; replace with real API requests if available
API_URLS = {
    "Facebook": "https://graph.facebook.com/v12.0/search",
    "LinkedIn": "https://api.linkedin.com/v2/me",
    "Twitter": "https://api.twitter.com/2/users/by/username"
}

# Example of API call (Facebook Graph API)
def facebook_search(email):
    access_token = "YOUR_FACEBOOK_ACCESS_TOKEN"
    params = {
        'q': email,
        'type': 'user',
        'access_token': access_token
    }
    response = requests.get(API_URLS["Facebook"], params=params)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data['data']) > 0:
            return {"platform": "Facebook", "link": f"https://facebook.com/{data['data'][0]['id']}"}
    return None

# Example of scraping (LinkedIn, replace with API in production)
def linkedin_search(email):
    search_url = f"https://www.linkedin.com/search/results/people/?keywords={email}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, "html.parser")
    profiles = []
    
    # Simulate extraction (you would replace this with real profile parsing)
    for profile in soup.find_all('a', href=True):
        profiles.append({"platform": "LinkedIn", "link": profile['href']})
    return profiles

def track_online_presence(email):
    profiles = []

    # Facebook Search (API)
    fb_profile = facebook_search(email)
    if fb_profile:
        profiles.append(fb_profile)
    
    # LinkedIn Search (Web Scraping)
    linkedin_profiles = linkedin_search(email)
    profiles.extend(linkedin_profiles)

    # Other APIs or Scraping (Twitter example using API)
    twitter_url = f"{API_URLS['Twitter']}/{email}"
    twitter_response = requests.get(twitter_url, headers={"Authorization": "Bearer YOUR_TWITTER_API_TOKEN"})
    if twitter_response.status_code == 200:
        data = twitter_response.json()
        profiles.append({"platform": "Twitter", "link": f"https://twitter.com/{data['data']['id']}"})
    
    return profiles
