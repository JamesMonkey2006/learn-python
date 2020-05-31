def say(who, what='hello'):
    """Say hello to client"""

    print(what, who)
    if what == 'hello':
        print('nice to see you :)')
    elif what == 'goodbye':
        print("I'll miss you")
    else:
        print("That's all")


def get_name():
    """get and return client name"""
    name = input("enter your name")
    return name


name = get_name()
say(name)
say(name, 'goodbye')
say(name, 'you like cookies')
