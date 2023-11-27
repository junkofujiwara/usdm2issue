"""GitHub utility functions"""
import json
import requests
from util.issue import Issue

class GithubUtil:
    '''GitHub utility functions'''

    def __init__(self, token, endpoint, owner, repo):
        '''init'''
        self.token = token
        self.endpoint = endpoint
        self.owner = owner
        self.repo = repo
        self.headers = {"Authorization" : f"token {self.token}"}
        self.issueurl = f"{self.endpoint}/repos/{self.owner}/{self.repo}/issues"

    def format_issue(self, issue):
        '''Format the issue to be posted to github.'''
        issue = {'title': issue.title,
                'body': issue.body,
                'labels': issue.labels}
        return issue

    def post_github_issue(self, issues):
        '''Create an issue on GitHub using the given parameters.'''
        for issue in issues:
            title = issue['title']
            response = requests.post(self.issueurl, json.dumps(issue), headers=self.headers)
            if response.status_code == 201:
                print (f'Successfully created Issue {title}')
            else:
                print (f'Could not create Issue {title}')
                print (f'Response:{response.content}')

    def is_github_issue_exist(self, title, labels):
        '''Check if the issue exists on GitHub using the given parameters.'''
        url = f'{self.issueurl}?state=all&labels={labels}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            content = json.loads(response.content)
            if content and 'id' in content[0]:
                print (f'Found Issue {title}')
                return True
            else:
                print (f'Could not find Issue {title}')
        else:
            print (f'Could not find Issue {title} (error)')
        return False