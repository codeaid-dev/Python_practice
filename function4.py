def ask(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'yeah'):
            return True
        if ok in ('n', 'no', 'none'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

if ask('Do you really want to quit?'):
    print('Normal END')
else:
    print('Lets Do It Again!!')