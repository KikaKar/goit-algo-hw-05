fh = open('log.txt', mode='r', encoding=None, errors=None, closefd=True, )
all_file = fh.read()
print(all_file)
fh.close()