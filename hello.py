

def say_hello(name=None):
    if name:
        print('Hello GIT, ' + name)
    else:
        print('Hello GIT')


if __name__ == '__main__':
    say_hello(name='Konstantin')
    say_hello()
