"""GitHub Issue class"""
class Issue:
    """Issue class"""

    def __init__(self, title, body, labels=[]):
        """init"""
        self.title = title
        self.body = body
        self.labels = labels
