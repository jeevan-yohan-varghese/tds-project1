
import requests
import pandas as pd

# Replace 'YOUR_TOKEN_HERE' with your actual personal access token
GITHUB_TOKEN = 'YOUR_TOKEN_HERE'

def get_dublin_users_with_followers(min_followers=50):
    url = "https://api.github.com/search/users"
    dublin_users = []
    page = 1

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }

    while True:
        params = {
            'q': f'location:Dublin followers:>{min_followers}',  
            'page': page,
            'per_page': 100
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 403:
            print("Error: Access forbidden (403). Check your token or permissions.")
            break
        elif response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            break
        
        users = response.json().get('items', [])
        if not users: 
            break
        
        for user in users:
            user_details = requests.get(user['url'], headers=headers).json()
            if 'location' in user_details and 'Dublin' in user_details['location'] and user_details['followers'] > min_followers:
                dublin_users.append(user_details)
        
        page += 1

    return dublin_users

def get_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    repos = []
    page = 1

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }

    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})
        if response.status_code == 403:
            print(f"Error: Access forbidden (403) for user {username}. Check your token or permissions.")
            break
        elif response.status_code != 200:
            print(f"Error fetching repos for {username}: {response.status_code}")
            break
        
        user_repos = response.json()
        if not user_repos:  
            break
        
        repos.extend(user_repos)
        page += 1

    return repos[:500]  

def clean_company_name(company):
    if company:
        return company.strip().lstrip('@').upper()
    return ""

def main():
    users = get_dublin_users_with_followers()
    user_data = []
    repo_data = []

    for user in users:
        user_info = {
            "login": user['login'],
            "name": user.get('name', ""),
            "company": clean_company_name(user.get('company', "")),
            "location": user.get('location', ""),
            "email": user.get('email', ""),
            "hireable": str(user.get('hireable', "")).lower() if user.get('hireable') is not None else "",
            "bio": user.get('bio', ""),
            "public_repos": user['public_repos'],
            "followers": user['followers'],
            "following": user['following'],
            "created_at": user['created_at']
        }
        user_data.append(user_info)

        repos = get_user_repositories(user['login'])
        for repo in repos:
            repo_info = {
                "login": user['login'],
                "full_name": repo['full_name'],
                "created_at": repo['created_at'],
                "stargazers_count": repo['stargazers_count'],
                "watchers_count": repo['watchers_count'],
                "language": repo['language'],
                "has_projects": str(repo.get('has_projects', "")).lower() if repo.get('has_projects') is not None else "",
                "has_wiki": str(repo.get('has_wiki', "")).lower() if repo.get('has_wiki') is not None else "",
                "license_name": repo['license']['key'] if repo.get('license') else ""
            }
            repo_data.append(repo_info)

    users_df = pd.DataFrame(user_data)
    repos_df = pd.DataFrame(repo_data)
    users_df.to_csv('users.csv', index=False)
    repos_df.to_csv('repositories.csv', index=False)

if __name__ == "__main__":
    main()
