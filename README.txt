This is an implementation of a process used in 'cracking' a 
ciphertext encrypted using a Vigenere cipher.

It utilizes the Index of Coincidences process described here:
http://practicalcryptography.com/cryptanalysis/text-characterisation/index-coincidence/

The ciphertext--in this case, the one given in the assignment--is contained in the 'ciphertext' file.
Running 'python3 main.py' will evaluate the ciphertext, determining the key and the decrypted text.