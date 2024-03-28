# Pico2024 WRITEUP

### PLACED 166/1329 for 2024 Pico

### Binary Exploitation

- format string 0
    - Once inspecting the source code and netcatting into the instance, you can see that format strings are used
    - In the first input section where you have to input a sandwitch, you can find this format identifier “%114d”, which is for long datatype
    - If you simply enter a large string “A” (30 times), you are given the flag
    
    Flag: [forgot to save, doing later]
    

### Cryptography

- Custom encryption
    - You are given some source code and info with terminal output
    - Quickly looking at the source code, you will see that there are some variables (a, b, etc.)
    - The terminal output gives you the value of a and b
    - Simply putting all operations given to us in the source code will allow us to decrypt it
    - (Code has info pre-entered)
    
    Flag: `picoCTF{custom_d2cr0pt6d_8b41f976}`
    
    ```python
    from random import randint
    import sys
    
    def generator(g, x, p):
        return pow(g, x) % p
    
    def encrypt(plaintext, key):
        cipher = []
        for char in plaintext:
            cipher.append(((ord(char) * key*311)))
        return cipher
    
    def is_prime(p):
        v = 0
        for i in range(2, p + 1):
            if p % i == 0:
                v = v + 1
        if v > 1:
            return False
        else:
            return True
    
    def dynamic_xor_encrypt(plaintext, text_key):
        cipher_text = ""
        key_length = len(text_key)
        for i, char in enumerate(plaintext[::-1]):
            key_char = text_key[i % key_length]
            encrypted_char = chr(ord(char) ^ ord(key_char))
            cipher_text += encrypted_char
        return cipher_text
    
    def test(plain_text, text_key):
        p = 97
        g = 31
        if not is_prime(p) and not is_prime(g):
            print("Enter prime numbers")
            return
        a = 90
        b = 22
        print(f"a = {a}")
        print(f"b = {b}")
        u = generator(g, a, p)
        v = generator(g, b, p)
        key = generator(v, a, p)
        b_key = generator(u, b, p)
        shared_key = None
        if key == b_key:
            shared_key = key
        else:
            print("Invalid key")
            return
        print(shared_key, u, v, key, b_key)
        print(plain_text, text_key)
        semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
        print(semi_cipher)
        cipher = encrypt(semi_cipher, shared_key)
        print(f'cipher is: {cipher}')
        return cipher
    
    def dynamic_xor_decrypt(cipher_text, text_key):
        decrypted_text = ""
        key_length = len(text_key)
        for i, char in enumerate(cipher_text):
            key_char = text_key[i % key_length]
            decrypted_char = chr(ord(char) ^ ord(key_char))
            decrypted_text += decrypted_char
        return decrypted_text
    def decrypt(cipher):
        semi = []
    
        p = 97
        g = 31
        if not is_prime(p) and not is_prime(g):
            print("Enter prime numbers")
            return
    
        # Generate random keys
        a = 94
        b = 21
        print(f"a = {a}")
        print(f"b = {b}")
    
        u = generator(g, a, p)
        v = generator(g, b, p)
        key = generator(v, a, p)
        b_key = generator(u, b, p)
        shared_key = None
        
        if key == b_key:
            shared_key = key
        else:
            print("Invalid key")
            return
        print(shared_key, u, v, key, b_key)
    
        # Decrypt the cipher
        for c in cipher:
            semi.append(chr(int(c // shared_key // 311 )))  # Apply inverse operations
        semi = ''.join(semi)
        print(semi)
    
        # Decrypt the semi-decrypted text using XOR with text key
        decrypted_text = dynamic_xor_decrypt(semi, "trudeau")
        print("Decrypted text:", decrypted_text[::-1])
    
    if __name__ == "__main__":
        message = sys.argv[1]
        decrypt([131553, 993956, 964722, 1359381, 43851, 1169360, 950105, 321574, 1081658, 613914, 0, 1213211, 306957, 73085, 993956, 0, 321574, 1257062, 14617, 906254, 350808, 394659, 87702, 87702, 248489, 87702, 380042, 745467, 467744, 716233, 380042, 102319, 175404, 248489])
    
    ```
    

### General Skills

- Time Machine
    
    ```bash
    ❯ cd drop-in
    ❯ ls
    message.txt
    ❯ ls -a
    .           ..          .git        message.txt
    ❯ cd .git
    ❯ ls
    COMMIT_EDITMSG config         index          objects
    HEAD           description    info           refs
    branches       hooks          logs
    ❯ cd logs
    ❯ ls
    HEAD refs
    ❯ cat HEAD
    0000000000000000000000000000000000000000 b92bdd8ec87a21ba45e77bd9bed3e4893faafd0f picoCTF <ops@picoctf.com> 1710018629 +0000	commit (initial): picoCTF{t1m3m@ch1n3_5cde9075}
    ╭─    ~/Downloads/drop-in/.git/logs    master                        ✔
    ╰─
    ```
    
    Flag: `picoCTF{t1m3m@ch1n3_5cde9075}`
    
- Commitment Issues
    - You will see a text file that could contain the flag but just says “TOP SECRET’. Open the `/.git/logs/refs/heads/master` file and you will see a commit history. You want to bring back the commit with the message “create flag”.
    - Run `git log --grep="create flag”`to bring the commit back. Now open that same text file from the beginning in the parent directory titled “message.txt” and you will see the flag.
    - Flag: `picoCTF{s@n1t1z3_7246792d}`
- Blame Game
    - Download the zip file, extract it, and open `/.git/logs/refs/heads/master` in the extracted folder where you can see all commits that were made. You should see the flag in plan text at the top.
    
    Flag: `picoCTF{@sk_th3_1nt3rn_e9957ce1}`
    
- Collaborative Development
    - Download the zip file and extract it. In the newly created folder, open the terminal and list all Git branches with `git branch -vvv`. Here you will see that there are four branches:
    
    ```
      feature/part-1 f65544e add part 1
      feature/part-2 d3563a2 add part 2
      feature/part-3 5c00b43 add part 3
    * main           54c7842 init flag printer
    ```
    
    - We want to view the versions of “flag.py” from the folder in all three branches that start with “feature”. To do this, run `git show feature/part-1:flag.py` , and the same command for part 2 and 3 too. Each of these will output code that will have print statements containing segments of a string. When concatenated together, they reveal the full flag.
    
    Flag: `picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_7ffa0077}`
    
- endianness
    - Launch your personal instance and connect to it using the nc command given. It will give you a string. You have to convert this into little endian format. If you download the source code of this program from the challenge description, you can copy some C code into your own program. It is suggested to use an online C compiler to save time.
    
    Code to copy:
    
    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <stdbool.h>
    #include <ctype.h>
    #include <time.h>
    
    char *find_little_endian(const char *word)
    {
        size_t word_len = strlen(word);
        char *little_endian = (char *)malloc((2 * word_len + 1) * sizeof(char));
    
        for (size_t i = word_len; i-- > 0;)
        {
            snprintf(&little_endian[(word_len - 1 - i) * 2], 3, "%02X", (unsigned char)word[i]);
        }
    
        little_endian[2 * word_len] = '\0';
        return little_endian;
    }
    
    char *find_big_endian(const char *word)
    {
        size_t length = strlen(word);
        char *big_endian = (char *)malloc((2 * length + 1) * sizeof(char));
    
        for (size_t i = 0; i < length; i++)
        {
            snprintf(&big_endian[i * 2], 3, "%02X", (unsigned char)word[i]);
        }
    
        big_endian[2 * length] = '\0';
        return big_endian;
    }
    ```
    
    - Below this segment of code, you have to insert more code where you use the functions defined above on the string given to you by the program. In my case the word was “cbdpn” but yours will be different. I wrote the code below.
    
    ```c
    int main() {
        
        char word[] = "cbdpn";
        
        printf("Little Endian: %s\n", find_little_endian(&word));
        printf("Big Endian: %s\n", find_big_endian(&word));
    
        return 0;
    }
    ```
    
    - Remember to change the “word” variable to your word instead of “cbdpn”. This should give you the little and big endian representations of your word and you will enter them in accordingly. After putting in both in the correct spots, you will receive the flag.
    
    Flag: `picoCTF{3ndi4n_sw4p_su33ess_817b7cfe}`
    
- Binary Search
    
    SSH in using the command provided and enter the password. Once you are in, it says you have to guess a number between 1 and 1000 and you only have 10 attempts. Your first guess should be “500”. If it says that the number is higher, try something above 500, else try a number below it. Keep narrowing down the number like this using higher or lower numbers. Once you guess it correctly, it will inform you and give you the flag. 
    
    `picoCTF{g00d_gu355_3af33d18}`
    
- binhexa
    - Surprisingly easy
    - Simply follow all commands (& is and, * is multiply, et.c)
    - Gives you the flag
    
    Flag:`picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_6ab1ad84`
    

### Web Exploitation

- No SQL Injection
    - You are given a web project repo. Upon inspection you can find that it uses mongoose
    - You find a default user schema with an email
    - After further inspection you find the login endpoint does not “sanitize” their login request and can be exploited
    - If you enter the following {”ne”:null} in the place of the password, you can trick the DB into giving you the users token
    - After exploitation it and looking at the requests you will notice a user object with a token, that once decoded from base 64 gives you the flag
    
    Flag: `picoCTF{jBhD2y7XoNzPv_1YxS9Ew5qL0uI6pasql_injection_e31ef324}`
    
- Unminify
    - Open up dev browser tools and head to the “Sources” tab
    - If you look in one of the p tags, you will see it has a class attribute. That’s the flag.
    
    Flag: `picoCTF{pr3tty_c0d3_ed938a7e}`
    
- IntroToBurp
    - You are given a website that allows you register for something and you have to enter an otp
    - After registering, open burpsuite and turn on intercept on burpsuite and catch the request while entering the OTP
    - Move into repeater and mess with the cookie arguments
    - I pasted the session cookie into the OTP argument and it gave me the flag
    
    Flag:`picoCTF{#0TP_Bypvss_SuCc3$S_e1eb16ed}`
    

### Forensics

- Verify
    
    ```bash
    ctf-player@pico-chall$ find files -type f -exec sha256sum {} + | grep '5848768e56185707f76c1d74f34f4e03fb0573ecc1ca7b11238007226654bcda'
    5848768e56185707f76c1d74f34f4e03fb0573ecc1ca7b11238007226654bcda  files/8eee7195
    ctf-player@pico-chall$ ./decrypt.sh files/8eee7195
    picoCTF{trust_but_verify_8eee7195}
    ```
    
    Flag: `picoCTF{trust_but_verify_8eee7195}`
    
- CanYouSee
    - Under **ExifTool,** look at the **AttributionURL** which ****gives us `cGljb0NURntNRTc0RDQ3QV9ISUREM05fNGRhYmRkY2J9Cg==` and decoding it from base64 gives us the flag.
    
    Flag: `picoCTF{ME74D47A_HIDD3N_4dabddcb}`
    
- Secret of the Polyglot
    - Opened the file as a pdf, which shows the 2nd part of the flag. The `file` command says that its a png file, and opening it gives us the 1st part of the flag.
    
    Flag: `picoCTF{f1u3n7_1n_pn9_&_pdf_249d05c0}`
    
- Scan Surprise
    - Scan given qr code to get the flag
    
    Flag: `picoCTF{p33k_@_b00_b5ce2572}`
    
- Mob psycho
    - Extract the file with 7zip
    - Searching the folder for flag gives you the text
    - Opening the file, you are given something encoded with hexadecimal
    - Decoding this gives you the flag
    
    Flag: `picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_85dbd215}`