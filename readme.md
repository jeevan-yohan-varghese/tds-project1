# GitHub User & Repository Analysis for Dublin

- This project uses the GitHub API to gather data on users located in Dublin with over 50 followers, capturing their profiles and repository details.
- A surprising finding is that only a few top developers dominate the follower count, while the majority have a modest following.
- Recommendation: Developers looking to increase visibility should focus on quality repositories and engagement in projects/wikis, as these features are often associated with higher follower counts.

## Project Overview

This project aims to analyze the GitHub profiles and repositories of developers in Dublin to gain insights into common characteristics and trends. We gathered data using the GitHub API and saved it in `users.csv` and `repositories.csv`. The project contains two main notebooks:

1. **questions.ipynb**: Contains responses to specific questions about Dublin-based GitHub users, focusing on follower count, programming languages, hiring tendencies, and more.
2. **analysis.ipynb**: Contains additional Exploratory Data Analysis (EDA) of the data, covering trends in company affiliations, repository activity, and correlations between user and repository features.

## Data Collection

The data was collected using the GitHub API with a Python script that:
1. Searches for GitHub users in Dublin with over 50 followers.
2. Retrieves profile details such as username, company, location, and more.
3. Fetches up to 500 most recent repositories for each user, including details like programming language, stars, watchers, and license.

## Key Findings

- **Top Languages and Licenses**: The most popular programming languages are highlighted, with a few prominent licenses indicating common open-source preferences.
- **Followers & Repository Stars**: Users with higher follower counts tend to have more starred repositories, suggesting that engagement correlates with popularity.
- **Hireable Status and Email Sharing**: Developers open to hiring share emails more often, which could increase opportunities for connections.
- **Weekday vs. Weekend Repository Creation**: Analysis shows certain developers are more active in creating repositories on weekends, which may hint at project commitment beyond regular hours.

## Additional Exploratory Data Analysis (EDA)

The `analysis.ipynb` notebook further explores:
- **Company Affiliations**: Visualizations of the top companies associated with GitHub users in Dublin.
- **Popular Programming Languages**: Analyzes the prevalence of different programming languages among Dublin-based repositories.
- **License Distribution**: Highlights the common licenses used, reflecting developers' openness to open-source contributions.
- **Followers and Public Repositories**: Examines the correlation between user follower counts and the number of public repositories.

## Questions Addressed

The `questions.ipynb` notebook contains responses to specific questions about Dublin's GitHub users, including:
1. Top users by followers, companies, and activity trends.
2. Popular licenses and languages used in repositories.
3. Analysis of user engagement factors like bio length, leader strength, and more.
4. Correlations between hiring openness, email sharing, and visibility on the platform.

## Recommendations for Developers

To maximize visibility and engagement, Dublin-based developers could consider:
- Increasing activity in collaborative projects and enabling wikis on repositories.
- Sharing contact information, such as email, if they are open to hiring.
- Regularly updating repositories and engaging with community languages, as popularity in programming language communities positively correlates with follower count.

## How to run

Run this once to scrape data using GitHub api.  

```
python main.py
```

This may take a while to get the whole data.  The data will be saved to *repositories.csv* and *users.csv*

Once data is saved, run all blocks in analysis.ipynb and questions.ipynb to see analysis of collected data