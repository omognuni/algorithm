def test(**kwargs):
    print(kwargs)

test(a=1,b=2,c=3)
payload = {'a': 1, 'b':2, 'c':3}

test(**payload)
