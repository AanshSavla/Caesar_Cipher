
# Task-2

cipher = "Udg bhv xc Tcvaxhw iwtgt pgt iltcin hxm ztnh, xu ndj peean dct puitg pcdiwtg dc tcrgneits bhv pcs dqhtgkt imi dct du iwt igpchudgbts imi xh gtpspqat."
cipher_lower = cipher.lower()
letter_dict = {}

for c in cipher_lower:
    if(c.isalpha()):
        if c in letter_dict:
            letter_dict[c] += 1
        else:
            letter_dict[c] = 1

sorted_dict = dict(sorted(letter_dict.items(),key = lambda item : item[1],reverse = True))
most_occur = list(sorted_dict.keys())[0]
key = ord(most_occur) - ord('e')
print("Key =",key)


decipher = ""
for c in cipher:
    if(c.islower()):
        l = ord(c) - ord("a")
        l = (l - key)%26 + 97
    elif(c.isupper()):
        l = ord(c) - ord('A')
        l = (l - key)%26 + 65
    else:
        l = ord(c)
    decipher += chr(l)
print("Decrypted Text :",decipher)

# Task-3

decipher_lower = decipher.lower()
letter_dict = {}

for c in decipher_lower:
    if(c.isalpha()):
        if c in letter_dict:
            letter_dict[c] += 1
        else:
            letter_dict[c] = 1

sorted_data = sorted(letter_dict.items(),key = lambda item : item[1],reverse = True)


print("Top 3 letter:")

most_occur = []

for (key, value) in sorted_data:
    if len(most_occur) < 3:
        most_occur.append((key, value))
        current_value = value
    elif value == current_value:
        most_occur.append((key, value))
    else:
        break

            
# most_occur = list(sorted_dict.keys())
# for i in range(3):
#    print(most_occur[i])
print(most_occur)





