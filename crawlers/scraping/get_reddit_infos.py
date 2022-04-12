from typing import Union

import requests
from beautifultable import BeautifulTable
from sty import ef, fg


class RedditData:
    def __init__(self, option: str, sub: str):
        self.__base_url = "https://old.reddit.com/r/"
        self.__sub = sub.split(";")
        self.__option = option
        if option == "telegram":
            self.data = []
        else:
            self.data = BeautifulTable(maxwidth=150)
            self.data.set_style(BeautifulTable.STYLE_BOX_DOUBLED)

    def extract_data(self) -> list:
        for sub in self.__sub:
            if sub == "":
                self.data = ""
                continue
            data = self.get_reddit_data(sub)
            try:
                data = data["data"]["children"]
            except (KeyError, TypeError):
                print("\n" + fg.li_red + ef.bold + data + "\n")
                continue
            if self.__option == "telegram":
                self.format_infos_telegram(data, sub)
            else:
                self.format_infos_terminal(data, sub)
        return self.data

    def get_reddit_data(self, sub: str) -> Union[list, str]:
        url = self.__base_url + sub + "/top/.json"
        response = requests.get(
            url, headers={"User-agent": "IDWall Test Agent"}
        )
        if response.status_code == 200:
            data = response.json()
        else:
            data = f"Please check your internet connection or subreddit: {sub} availability"
        return data

    def format_infos_telegram(self, response: list, sub: str) -> None:
        for posts in response:
            if self.check_ups(posts["data"]["ups"]):
                data = self.format_values(posts, sub)
                data["title"] = self.format_title(data["title"])
                self.data.append(data)

    def format_infos_terminal(self, response: list, sub: str) -> None:
        table = self.data
        table = self.set_header_table(table)
        for posts in response:
            table = self.create_table(posts, table, sub)
        table = self.data

    def create_table(
        self, posts: dict, table: BeautifulTable, sub: str
    ) -> BeautifulTable:
        if self.check_ups(posts["data"]["ups"]):
            data = self.format_values(posts, sub)
            data["title"] = self.format_title(data["title"])
            table.rows.append(
                [
                    fg.da_magenta + data["sub"],
                    f"{ef.rs + fg.li_cyan + ef.bold + data['title']}",
                    f"{ef.rs + fg.green + data['ups']}",
                    f"{ef.rs + fg.da_cyan + ef.underl + data['link']}",
                    f"{ef.rs + fg.cyan + ef.underl + data['thread_url']}",
                ]
            )
        return table

    @staticmethod
    def format_values(posts: dict, sub: str) -> dict:
        data = {}
        data["title"] = posts["data"]["title"]
        data["ups"] = str(posts["data"]["ups"])
        data["link"] = str(
            "https://old.reddit.com/" + posts["data"]["permalink"]
        )
        data["thread_url"] = posts["data"]["url"]
        data["sub"] = sub
        return data

    @staticmethod
    def check_ups(ups: int) -> bool:
        check_up = False
        if ups > 5000:
            check_up = True
        return check_up

    @staticmethod
    def format_title(title: str) -> str:
        if len(title) > 40:
            title = title[:40] + "..."
        return title

    @staticmethod
    def set_header_table(table: BeautifulTable) -> BeautifulTable:
        table.header = [
            "Subreddit.",
            "Title",
            "Ups",
            "Thread Comment Link",
            "Thread Link",
        ]
        return table
