ch1 = input()
if ch1.isalpha():
  if(ch1 == 'a' or ch1 == 'e' or ch1 == 'i' or ch1 == 'o' or ch1 == 'u' or ch1 == 'A'
       or ch1 == 'E' or ch1 == 'I' or ch1 == 'O' or ch1 == 'U'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
