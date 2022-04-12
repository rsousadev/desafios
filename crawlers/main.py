from sty import ef, fg

from scraping.get_reddit_infos import RedditData

if __name__ == "__main__":
    # execute only if run as the entry point into the program
    while True:
        print(
            f"\n {fg.li_green} {ef.bold} To stop execution, type exit in the field below. {fg.rs}"
        )
        sub = str(
            input("\n Enter the subreddit names separated by semicolons: ")
        ).lower()
        if sub == "exit":
            break
        scraping = RedditData("terminal", sub)
        data = scraping.extract_data()
        if data == "":
            print("\n" + "There is no value, please try again." + "\n")
        print(data)
