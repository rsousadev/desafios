from textwrap import wrap


class bcolors:
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    BOLD = "\033[1m"
    WARNING = "\033[93m"


class FormatText:
    def __init__(self):
        self.words = str(input(f"{bcolors.OKGREEN}Enter a text: "))

    def break_line(self):
        print(f"{bcolors.BOLD}-" * 40)
        formated_text = []

        for line in wrap(self.words, width=40):
            formated_text.append(line)
        self.set_otions(formated_text)

    def set_otions(self, formated_text: list) -> None:
        format_option = input(
            f"{bcolors.BOLD}Want to justify the text? [Y/n] "
        ).lower()
        if format_option == "y":
            self.format_text(formated_text)
        else:
            for line in formated_text:
                print(f"{bcolors.WARNING}" + line)

    def format_text(self, formated_text: list) -> None:
        for line in formated_text:
            count = 0
            lines = line.split(" ")
            while len(line) < 40:
                if count >= len(lines):
                    count = 0
                if count != len(lines) - 1:
                    lines[count] += " "
                    line = " ".join(lines)
                count += 1

            print(f"{bcolors.OKBLUE}" + line)


if __name__ == "__main__":
    # execute only if run as the entry point into the program
    format_text = FormatText()
    format_text.break_line()
