#!/use/bin/python
for i in range(ord('a'), ord('z') + 1):
    if i != ord('q') and i != ord('e'):
        print(f"{i:c}", end='')
