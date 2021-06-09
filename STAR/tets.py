import inspect


def foo(*test):
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') + 1:-1].split(',')

    names = []
    for i in args:
        if i.find('=') != -1:
            names.append(i.split('=')[1].strip())

        else:
            names.append(i)

    return names


a = foo(1, 1000, 2)