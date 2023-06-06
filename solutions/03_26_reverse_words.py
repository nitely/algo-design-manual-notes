# -*- coding: utf-8 -*-

# in:  My name is Chris
# out: Chris is name My

def reverse2(text):
    return ' '.join(reversed(text.split(' ')))

def reverse(text):
    text = list(text)
    text.reverse()
    i = 0
    while i < len(text):
        j = i
        while j < len(text) and text[j] != ' ':
            j += 1
        k = j
        j -= 1
        while i < j:
            text[i], text[j] = text[j], text[i]
            j -= 1
            i += 1
        i = k + 1
    return ''.join(text)

print(reverse('My name  is Chris'))
