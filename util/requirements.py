"""requirements"""
from util.requirement import Requirement
import settings

class Requirements:
    """requirements"""

    def __init__(self, feature, dataframe):
        """init"""
        self.feature = feature
        self.list = []
        for index, row in dataframe.iterrows():
            key = ""
            value = ""
            if row[settings.FILE_COLUMN[0]] == settings.TERM_REQUIREMENT:
                level = 1
                loop = 0
            if row[settings.FILE_COLUMN[1]] == settings.TERM_REQUIREMENT:
                level = 2
                loop = 0
            if row[settings.FILE_COLUMN[1]] == settings.TERM_SUB:
                level = 3
                loop = 0
            if level == 1:
                key = row[settings.FILE_COLUMN[1]]
                value = row[settings.FILE_COLUMN[2]]
            if level in (2, 3):
                key = row[settings.FILE_COLUMN[2]]
                value = row[settings.FILE_COLUMN[3]]
            self.list.append(Requirement(level=level, index=loop, key=key, value=value,
                                    parameter=row[settings.FILE_COLUMN[4]],
                                    relationreq=row[settings.FILE_COLUMN[5]]))
            loop += 1

    def get_list(self):
        """get list"""
        return self.list

    def format_markdown(self):
        """format markdown"""
        header_icon = settings.MD_HEADER_ICON
        icon = settings.MD_ITEM_ICON
        markdown = f"# {self.feature}\n"
        for requirement in self.list:
            if requirement.get_index() == 0:
                if requirement.get_level() == 1:
                    markdown += f"## {header_icon} {requirement.get_key()}\n"
                if requirement.get_level() == 2:
                    markdown += f"### {header_icon} {requirement.get_key()}\n"
                if requirement.get_level() == 3:
                    markdown += f"#### {header_icon} {requirement.get_key()}\n"
            else:
                markdown += f"{icon} **{requirement.get_key()}**\n"
            markdown += f"{requirement.get_value()}\n"
            if requirement.get_parameter() != "":
                markdown += f"\n{icon} **{settings.FILE_COLUMN[4]}**\n{requirement.get_parameter()}\n"
            if requirement.get_relationreq() != "":
                markdown += f"\n{icon} **{settings.FILE_COLUMN[5]}**\n{requirement.get_relationreq()}\n"
            markdown += "\n"
        return markdown
