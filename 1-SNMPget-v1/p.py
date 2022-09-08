import mmap

with open('localhost.txt') as f:
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if s.find(b'Windows') != -1:
        print('Windows True')
    if s.find(b'Linux') != -1:
        print('Linux True')
    if s.find(b'Mac') != -1:
        print('Mac True')

