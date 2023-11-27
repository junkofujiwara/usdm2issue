""" read excel and post to github issue """
import pandas as pd
import settings
from util.githubutil import GithubUtil
from util.issue import Issue
from util.requirements import Requirements

def main():
    """main"""

    # GitHub init
    githubutil = GithubUtil(settings.GH_TOKEN, settings.GH_ENDPOINT, settings.GH_OWNER, settings.GH_REPO)

    # Read xlsx file
    file = pd.ExcelFile(settings.FILE_NAME)
    issues = []
    for sheet in file.sheet_names:
        labels = settings.ISSUE_LABELS.copy()
        labels.append(sheet)
        if settings.SKIP_IF_EXIST:
            if githubutil.is_github_issue_exist(sheet, labels):
                continue
        dataframe = file.parse(sheet, names=settings.FILE_COLUMN)
        dataframe.fillna("", inplace=True)
        requirements = Requirements(sheet, dataframe)
        markdown = requirements.format_markdown()
        issue = githubutil.format_issue(Issue(title=sheet, body=markdown, labels=labels))
        issues.append(issue)
    
    # Create GitHub issues
    githubutil.post_github_issue(issues) 

if __name__ == "__main__":
    main()
