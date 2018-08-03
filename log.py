import config


def log(text):
    if config.DEBUG:
        print(text)
