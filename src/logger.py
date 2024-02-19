def log(message):
    print(message)


def log_inline(message):
    print(message, end="")


def file_log(message, file="log.txt"):
    with open(file, "a") as f:
        f.write(f"{message}" + "\n")


def clear_line(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)
