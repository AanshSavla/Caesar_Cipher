cipher = "Udg bhv xc Tcvaxhw iwtgt pgt iltcin hxm ztnh, xu ndj peean dct puitg pcdiwtg dc tcrgneits bhv pcs dqhtgkt imi dct du iwt igpchudgbts imi xh gtpspqat."
word_dict = ["is","are","am","an","Be","That","He","She","It"]
max_point = 0
final_text = ""
give_point = {}
for key in range(1,27):
    ans = ""

# Decryption
    for c in cipher:
        if(c.islower()):
            l = ord(c) - ord("a") # Assigns number to small case character c. ASCII of 'a' is 97
            l = (l - key)%26 + 97 # decrypts small case letters.
        elif(c.isupper()):
            l = ord(c) - ord('A') # Assigns number to upper case character c. ASCII of 'A' is 65
            l = (l - key)%26 + 65 # decrypts upper case letters
        else:
            l = ord(c) # For other characters
        ans += chr(l) # Convert ASCII to character again.
    print("key =",key)
    print("Decrypted Text:",ans)
    word_array = ans.split() # Splits decrypted text into words and creates a word array.
    #print(word_array)
    for word in word_array:
        if(word in word_dict): # If any word in decrypted text is present in pre_defined word_dict then add 
                               # point to that text.
            # Code for incrementing point to each decrypted text.
            if(key in give_point):
                give_point[key] += 1
                if(max_point < give_point[key]):
                    max_point = give_point[key]
                    final_key = key
                    final_text = ans

            else:
                give_point[key] = 1

print("\nDecryption:")        
print("Final key :", final_key)
print("Decrypted message :")
print(final_text)
        
