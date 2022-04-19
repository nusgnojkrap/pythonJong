def start(filename, n):
    exec(open(filename).read())

    for i in range(0, int(n)):


start("./s1027.py", 10000)