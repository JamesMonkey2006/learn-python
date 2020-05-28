def say(what='hello'):
    """Say hello to client"""
    who = get_name()
    print(what, who)


def get_name():
    """get and return client name"""
    name = input("enter your name")
    return name


say()
say('goodbye')
