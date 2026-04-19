str_list = ['abc', 'ab', 'aba', 'hello', 'madam', 'hi', 'level']
count = 0
for s in str_list:
    if len(s) >= 3 and s[0] == s[-1]:
        count += 1
        print(f' "{s}" qualifies')

print(f'Count of qualifying strings: {count}')