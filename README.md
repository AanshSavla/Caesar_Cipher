## Caesar Cipher Encryption and Decryption
The Caesar Cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the “shift” or “key”. The Caesar Cipher technique is one of the earliest and simplest methods of encryption techniques.

Following is the output on running caesar.py file

Encryption:
![image](https://github.com/user-attachments/assets/e6db1e17-c03b-4966-8440-039f6bbb15f2)

Decryption:
![image](https://github.com/user-attachments/assets/b676bbf5-aad1-42dd-95b2-048a93ae78ce)

Blog Link on Caesar Cipher:
https://medium.com/@aanshsavla2453/caesar-cipher-a-classical-cryptography-technique-c393cadc8da2

## Brute Force on Caesar Cipher
Nothing can stop a cryptanalyst from guessing one key, decrypting the ciphertext with that key, looking at the output, and if it is not the correct key then moving on to the next key. The technique of trying every possible decryption key is called a brute-force attack.
It is trivial since an immediate problem with caesar cipher is that the method is fixed and there are only 26 possible keys. Thus, anyone learning how Caesar encrypted his messages would be able to decrypt effortlessly. Thus we can hack the Caesar cipher by using a cryptanalytic technique called “brute-force”.

Following is the output on running brute_force.py file

![image](https://github.com/user-attachments/assets/ec203539-05c1-4204-947f-1a36c7ad3523)

![image](https://github.com/user-attachments/assets/76c4a894-0ff2-4156-a6e7-c720699da2e4)

![image](https://github.com/user-attachments/assets/5bde2854-41e8-48c3-9d49-5caa867971ee)

From all the possible 26 decryptions we can check manually which decryption gives a meaningful text. But if we want to make computer to know the meaningful message then we declare a constant variable which consists of repeated English Words. It can be as follows : {‘the’,’a’,’an’,’am’,’it’,’he’,’she’,’or’,’and’,….}.
If some of these words match with any of the decryptions then that gives the final decrypted text.

Blog Link on Caesar Cipher:
https://medium.com/@aanshsavla2453/brute-force-attack-on-caesar-cipher-in-python-5972cdcff5b6

## Key Breaking using Frequency Analysis

Below diagram shows frequency of 26 letters in an English text paragraph.
<img width="741" alt="image" src="https://github.com/user-attachments/assets/8bef9a56-d6d3-4ae2-b27b-c554dd06401c">

Hence if we assume this to be true for the above case then the above message can also be decrypted by subtracting the maximum occuring letter in the encrypted text with letter 'e' to find the final key.

Following is the output on running break.py

<img width="1325" alt="image" src="https://github.com/user-attachments/assets/a031c4a3-2cc7-4e8e-9f73-144f39287e61">

Here we directly get the key and decrypted text.








