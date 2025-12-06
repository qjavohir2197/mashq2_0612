#1-misol
kirish = input('Ozingizni tanishtiring:')

words = kirish.split()
secret = ""

for w in words:
    secret += w[0]

print(secret)

#2-misol
royhat = [2, 3, 4, 5, 6, 7, 8]
new = []

for i in range(len(royhat)):
    new.append(royhat[i] * i)

print(new)

#3-misol
words = ['dasturlash', 'kitob', 'shunday', 'komputer', 'ilm', 'maktab']

new1 = ''
new2 = ''

for i in words:
    if len(i) > len(new1):
        new2 = new1
        new1 = i
    elif len(i) > len(new2):
        new2 = i

print('1-chi eng uzun so\'z:', new1)
print('2-chi eng uzun so\'z:', new2)
