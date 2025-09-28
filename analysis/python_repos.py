import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'ステータスコード：{r.status_code}')

response_dict = r.json()
repo_dicts = response_dict["items"]
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br>{description}'
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'hovertext': labels
}]

# layout = {
#     'title': 'Githubで最も多くのスターがついているPythonプロジェクト',
#     'titlefont': {'size': 28},
#     'xaxis': {
#         'title': 'リポジトリ',
#         'titlefont': {'size': 24}},
#     'yaxis': {
#         'title': 'スターの数',
#         'titlefont': {'size': 24}}
# }

# Pyplot version4以降
layout = {
    'title': {
        'text': 'Githubで最も多くのスターがついているPythonプロジェクト',
        'font': {'size': 28}
    },
    'xaxis': {
        'title': {
            'text': 'リポジトリ',
            'font': {'size': 24}
        }
    },
    'yaxis': {
        'title': {
            'text': 'スターの数',
            'font': {'size': 24}
        }
    }
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='python_repos.html')
