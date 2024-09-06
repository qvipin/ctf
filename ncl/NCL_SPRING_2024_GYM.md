# Writeup

---

### Open Source Intelligence

- Lookup (Easy)
    - What type of DNS record holds the DNSSEC public signing key?
        - DNSKEY
    - What type of DNS record is used to map hostnames to IPv6 addresses?
        - AAAA
    - What type of DNS record is used to delegate a DNS zone?
        
        NS
        
- Meta (Easy)
    - Download the image and put it into aperisolve to look at the EXIF data
    - When was the image created? Round down to the nearest minute
        - 2015:05:15 02:14:22
    - What are the dimensions of the image? (ex: 800x600)
        - 1024x768
        
    - What is the make of the camera that took the picture?
        - Apple
    - What is the model of the camera that took the picture?
        - Apple iPhone 5
    - What are the GPS coordinates where the was the picture taken? (Any standard format is acceptable)
        - 39 deg 52' 30.00" N, 20 deg 0' 36.00" E
    
- Threat Intel (Easy)
    - Utilizing Google is Key for this
    - What is the CVE of the original POODLE attack?
        
        CVE-2014-3566
        
    - What version of VSFTPD contained the smiley face backdoor?
        
        vsftpd version 2.3.4
        
    - What was the first 1.0.1 version of OpenSSL that was NOT vulnerable to heartbleed?
        
        OpenSSL 1.0.1g
        
    - What was the original RFC number that described Telnet?
        
        RFC 15
        
    - How large (in bytes) was the SQL Slammer worm?
        
        376 bytes
        
    - Complete the sentence: "Samy is my...”
        
        hero (found this on VICE)
        
- HTTP Headers (Easy)
    - Also still mostly using google and a lot of my pre-known knowledge
    - What HTTP request header is used to denote what URI linked to the resource being requested?
        - Referer
    - What HTTP request header is used to identify the client software that made the HTTP request?
        - User-agent
    - What HTTP request header is used to identify the acceptable content types that can be returned?
        - **Accept request**
    
- WHOIS (Easy)
    - Using [whois.com](https://www.whois.com/whois/cityinthe.cloud) I found most of the information along with some of my knowledge
    - Who is the registrar of this domain?
        - `dynadot`
    - On what day was this domain first registered?
        
        2016-02-16
        
    - What is this domain's registry domain ID?
        
        `D15CD1AC4DEB54207A5048A69B9FC0558-ARI`
        
    - What is the Top-Level Domain (TLD) of this domain?
        
        `.cloud`
        
    - What organization manages the TLD used by cityinthe.cloud?
        
        Aruba PEC SpA (found with google)
        
- PGP Lookup (Easy)
    - I mostly utilized [keyserver.ubuntu.com](https://keyserver.ubuntu.com/) for this
    - What is the key fingerprint for [security@cpanel.net](mailto:security@cpanel.net)?
        
        `ded38747ceefc789fdc3a6154cf279c5c0424907`
        
    - What email address is associated with the key fingerprint `7A39A56B73D1E097D57435CFCDE2DE1DCB2077F2`?
        
        `hx@liber8tion.cityinthe.cloud`
        
    - On what date does the above key expire (in UTC)?
        
        2050-12-26
        
- SSL (Medium)
    - Clicking on the lock on the top of your URL bar has the information needed
    - Who is the issuer for Cyber Skyline's SSL certificate?
        
        Sectigo
        
    - How many bits long is the SSL key?
        
        2,048 bits
        
    - How many certificates are in the certificate chain?
        
        3
        
- Barcode (Medium)
    - I used [https://online-barcode-reader.inliteresearch.com/](https://online-barcode-reader.inliteresearch.com/) for all the questions
    - What format does the barcode use?
        
        Code39
        
    - What is the flag hidden in the barcode?
        
        `SKY-UZLU-5635`
        

### Cryptography

- Number Bases (Easy)
    - I used [CyberChef](https://gchq.github.io/CyberChef/) for all of them
    - 0x73636f7270696f6e
        
        scorpion (hex)
        
    - c2NyaWJibGU=
        
        scribble (Base64)
        
    - 01110011 01100101 01100011 01110101 01110010 01100101 01101100 01111001
        
        securely (Binary)
        
    - 01100010 01000111 00111001 01110011 01100010 01000111 01101100 01110111 01100010 00110011 01000001 00111101
        
        lollipop (From Binary > Base64 > Plaintext)
        
    
- Shift (Easy)
    - One question in Rot13 and used cyberchef
    - iveghny ynxr
        
        virtual lake
        
- @bash (Easy)
    - One question again and name tells us the cipher (@bash is atbash cipher)
    - hzuvob lyerlfh xzev
        
        safely obvious cave
        
- Beep (Easy)
    - In morse (just use an online morse decoder)
    - - .... . / ... . -.-. .-. . - / --- ..-. / --. . - - .. -. --. / .- .... . .- -.. / .. ... / --. . - - .. -. --. / ... - .- .-. - . -.. / ... -.- -.-- / -.. -.- ...- -... / ----. ---.. .---- -.…
        
        THE SECRET OF GETTING AHEAD IS GETTING STARTED SKY DKVB 9816
        
- Fencing (Medium)
    - Rail Fence Cipher (one has the key 3 and the other 5) decoded with cyberchef
    - Cair eruSA-0org sgaeudrpesr K-II98.ue cn seYQ3
        
        Courage is grace under pressure SKY-AIQI-9380.
        
    - F daS-eefn  n KZ3eheadty.YI8lta oiwy-Q0. r aI2
        
        Feel the fear and do it anyway. SKY-IQIZ-3802. (make sure u dont have a trailing space)
        
    
- French (Medium)
    - The title french makes me think of the vignere cipher. Using cyber chef we decode it.
    - Y ln xkv lubj swlzqvkht, A vmzb pjk bbua we ddgs ILQ-GQYU-8026
        
        I do not fear computers, I fear the lack of them SKY-QIZK-8026
        
- Strings (Easy)
    - Below is the decode command used.
    
    ```bash
    ❯ strings Steg1.jpg | grep 'SKY'
    SKY-TVJI-2063
    ```
    

### Password Cracking

- Rockyou (Easy)
    - I used [hashes.com](http://hashes.com) to decode all of them
    
    ```bash
    2233287f476ba63323e60addca1f6b64:kirkles
    32e5f63b189b78dccf0b97ac41f0d228:joybird1
    6539bbb84fe2de2628fc5e4f2a31f23a:ddmack
    68a96446a5afb4ab69a2d15091771e39:emilybffl
    ec5f0b1826389df8622133014e88afde:ryjd1982
    
    ```
    
- Mask (Medium)
    - Decoded all of them with `hashcat -a 3 -m 0 hashes.txt 'SKY-HQNT-?d?d?d?d'` took 3 seconds to crack all of them (M2 THE BEST)
    
    ```bash
    06f03267f31077d2c4b5c728472070ae:SKY-HQNT-6598
    d866f4b3b34b598375149fb7661113ab:SKY-HQNT-5981
    674291170dffcf620bda2a604a6820ea:SKY-HQNT-7659
    71b816fe0b7b763d889ecc227eab400a:SKY-HQNT-8765
    d9053951a8d1c15254b46ec9fc974a6b:SKY-HQNT-9816
    ```
    
- Pokemon (Medium)
    - I did this NCL Gym challenge before so I still have my custom wordlist. (just search up pokemon wordlist and u can crack them too or use [hashes.com](http://hashes.com) for an easy way out)
    - (sorry no answer forgor to put them and to lazy to get them)
- Windows (Medium)
    - [Hashes.com](http://Hashes.com) and all ntlm so u can use hashcat.
        
        ```bash
        11cb3f697332ae4c4a3b108f3fa6cb6d:p@ssword
        13b29964cc2480b4ef454c59562e675c:P@ssword
        21c4e7c2efe8e8d1c00b70065ed76aa7:ECTOPLASM32
        47f747c5190dc0f0b921aa4a07f06285:footba11
        65711c079dc4cd3cc2265b23734e0dac:footba11
        fbbda33fc12e83fb0c240e84a183686e:1TRUSTNO1
        a7a0f9afd4a78f531a1cf4c42e531bbf:ectoplasm32
        dde9dc6e34e2e6e11ef9e51c6b27ed96:1trustno1
        3928e16f614e2316ca51c336fa5b3011:$xEn@=y
        c82e164316183aa3af3ea6baa642a237:^B7e3D;
        c8405270b10b13ae8a24612bb853567a:yhM^GK7
        f196f77bf8bb15781ba8364c649c5fd4:58?-<C6
        fd134459fe4d3a6db4034c4e52403f16:"=Cxu&L
        
        ```
        
- Law & Order (Hard)
    - [Hashes.com](http://Hashes.com) carried!
    
    ```bash
    1e1612db8bdeebc7e8d56f8f30b39456:philadelphia53:MD5
    08038f679de74982bfb9bac43d46271a:unorthodox12:MD5
    3dd9dd0e352df4433aadf2273e269287:resilience05:MD5
    6475c851b56004eb96ab1404252c3a34:hooked37:MD5
    abe6591e06aafc3cf1b0783b120f685e:manhunt74:MD5
    ```
    
- PDF (Medium) Took way tooo long to crack but the password was keanureeves2008 and the flag inside was SKY-KANU-5902
    - The process to crack is pretty simple just takes a long time pdf2john > remove pdf prefix > run `hashcat -m 10700 -a 0 pdfhash.txt rockyou.txt` > and you should have the flag in 2 hours or smth 
- Kali Linux (Hard) (come back to this
    - hollie is the user w/ the password and using the UNIX EPOCH we can find the date (2021-11-03) and

### Forensics

- Version Control (Easy)
    - `ls -la` after unzipped and `cd` into `.git` which has the information needed
    - To find the employee’s email we can check `/.git/logs/HEAD`
- Docter (Medium)
    - When changing the docx file to a .zip it shows the contents and media inside and inside the `/media` folder we find `image0.png` which has the flag `SKY-RATL-8439`
- File Carving (Medium)
    - Binwalk the image to get 4 pngs and 1 zip out of it and there are 6 files in total in the png and the zip has the flag (SKY-RWCI-4291)

### Enumeration & Exploitation

- Timebomb (Easy)
    - You need to decompile the java program online to answer the questions
    - What programming language is the program written in?
        
        Java
        
    - What exit code does the program exit with when it is not time?
        
        10
        
    - What time (in UTC) does the software go "Boom"?
        
        2022-07-17 13:12
        

### Log Analysis

- SSH (Easy)
    - You really just need to read the logs…
    - What is the hostname of the ssh server that was compromised?
        
        myraptor
        
    - What was the first IP address to attack the server?
        
        169.139.243.218
        
    - What was the second IP address to attack the server?
        
        56.13.188.38
        
    - What was the third IP address to attack the server?
        
        30.167.206.91
        
    - Which user was targeted in the attack?
        
        harvey
        
    - From which IP address was the attacker able to successfully log in?
        
        30.167.206.91
        
    
- VSFTPD (Easy)
    - Once again just read the logs
    

### Scanning & Reconnaissance

- NMAP (Easy)

### Web Application Exploitation

- egov (Easy)
    - Change the admin cookie to true and go to `/admin` to get the flag (varied flag)

# UNFINISHED (Last Updated 3/5/24)
