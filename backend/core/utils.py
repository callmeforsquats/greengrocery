def iter_file(path):
    with open(path,'rb') as f:
        yield from f