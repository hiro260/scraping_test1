import os

a = 'aaaa/eeee/ffff'
b = 'bbbb/gggg/'
c = 'cccc/kkkkk'

path = os.path.join(a, b, c)

print(path)


final_path = os.path.normpath(os.path.join(a, b, c))
print(final_path)

quit()
a1 = 'aaaa\eeee\ffff'
a2 = r'aaaa\eeee\ffff'

print(a1)
print(a2)