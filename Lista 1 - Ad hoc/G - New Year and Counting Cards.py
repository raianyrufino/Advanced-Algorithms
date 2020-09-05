string = raw_input()

vowels_and_odd = ['1', '3', '5', '7', '9', 'a', 'e', 'i', 'o', 'u']

print len(filter(lambda valor: valor in vowels_and_odd, string))
