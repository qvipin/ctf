## Writeup

### Open Source Intelligence

#### Lookup (Easy)
- **What type of DNS record holds the DNSSEC public signing key?**
  - **Answer:** DNSKEY
- **What type of DNS record is used to map hostnames to IPv6 addresses?**
  - **Answer:** AAAA
- **What type of DNS record is used to delegate a DNS zone?**
  - **Answer:** NS

#### Meta (Easy)
- **Download the image and put it into aperisolve to look at the EXIF data**
  - **When was the image created?** (Round down to the nearest minute)
    - **Answer:** 2015:05:15 02:14:22
  - **What are the dimensions of the image?** (ex: 800x600)
    - **Answer:** 1024x768
  - **What is the make of the camera that took the picture?**
    - **Answer:** Apple
  - **What is the model of the camera that took the picture?**
    - **Answer:** Apple iPhone 5
  - **What is the exposure time for the picture? (ex: 1/200)**
    - **Answer:** 1/640
  - **What are the GPS coordinates where the picture was taken?** (Any standard format is acceptable)
    - **Answer:** 39 deg 52' 30.00" N, 20 deg 0' 36.00" E

#### Threat Intel (Easy)
- **What is the CVE of the original POODLE attack?**
  - **Answer:** CVE-2014-3566
- **What version of VSFTPD contained the smiley face backdoor?**
  - **Answer:** vsftpd version 2.3.4
- **What was the first 1.0.1 version of OpenSSL that was NOT vulnerable to heartbleed?**
  - **Answer:** OpenSSL 1.0.1g
- **What was the original RFC number that described Telnet?**
  - **Answer:** RFC 15
- **How large (in bytes) was the SQL Slammer worm?**
  - **Answer:** 376 bytes
- **Complete the sentence: "Samy is my..."**
  - **Answer:** hero (found this on VICE)

#### HTTP Headers (Easy)
- **What HTTP request header is used to denote what URI linked to the resource being requested?**
  - **Answer:** Referer
- **What HTTP request header is used to identify the client software that made the HTTP request?**
  - **Answer:** User-agent
- **What HTTP request header is used to identify the acceptable content types that can be returned?**
  - **Answer:** Accept

#### WHOIS (Easy)
- **Who is the registrar of this domain?**
  - **Answer:** dynadot
- **On what day was this domain first registered?**
  - **Answer:** 2016-02-16
- **What is this domain's registry domain ID?**
  - **Answer:** D15CD1AC4DEB54207A5048A69B9FC0558-ARI
- **What is the Top-Level Domain (TLD) of this domain?**
  - **Answer:** .cloud
- **What organization manages the TLD used by cityinthe.cloud?**
  - **Answer:** Aruba PEC SpA (found with google)

#### PGP Lookup (Easy)
- **What is the key fingerprint for [security@cpanel.net](mailto:security@cpanel.net)?**
  - **Answer:** ded38747ceefc789fdc3a6154cf279c5c0424907
- **What email address is associated with the key fingerprint `7A39A56B73D1E097D57435CFCDE2DE1DCB2077F2`?**
  - **Answer:** hx@liber8tion.cityinthe.cloud
- **On what date does the above key expire (in UTC)?**
  - **Answer:** 2050-12-26

#### SSL (Medium)
- **Who is the issuer for Cyber Skyline's SSL certificate?**
  - **Answer:** Sectigo
- **How many bits long is the SSL key?**
  - **Answer:** 2,048 bits
- **How many certificates are in the certificate chain?**
  - **Answer:** 3

#### Barcode (Medium)
- **What format does the barcode use?**
  - **Answer:** Code39
- **What is the flag hidden in the barcode?**
  - **Answer:** SKY-UZLU-5635

---

### Cryptography

#### Number Bases (Easy)
- **Hex:** 0x73636f7270696f6e → **Answer:** scorpion
- **Base64:** c2NyaWJibGU= → **Answer:** scribble
- **Binary:** 01110011 01100101 01100011 01110101 01110010 01100101 01101100 01111001 → **Answer:** securely
- **Binary > Base64 > Plaintext:** 01100010 01000111 00111001 01110011 01100010 01000111 01101100 01110111 01100010 00110011 01000001 00111101 → **Answer:** lollipop

#### Shift (Easy)
- **ROT13:** iveghny ynxr → **Answer:** virtual lake

#### @bash (Easy)
- **Atbash:** hzuvob lyerlfh xzev → **Answer:** safely obvious cave

#### Beep (Easy)
- **Morse Code:** 
    - - .... . / ... . -.-. .-. . - / --- ..-. / --. . - - .. -. --. / .- .... . .- -.. / .. ... / --. . - - .. -. --. / ... - .- .-. - . -.. / ... -.- -.-- / -.. -.- ...- -... / ----. ---.. .---- -.…
  - **Answer:** THE SECRET OF GETTING AHEAD IS GETTING STARTED SKY DKVB 9816

#### Fencing (Medium)
- **Rail Fence Cipher (key 3 and 5):**
  - **Decoded Message:** 
    - Courage is grace under pressure SKY-AIQI-9380.
    - Feel the fear and do it anyway. SKY-IQIZ-3802.

#### French (Medium)
- **Vigenère Cipher:**
  - **Decoded Message:** I do not fear computers, I fear the lack of them SKY-QIZK-8026

#### Strings (Easy)
- **Command used:**
  ```bash
  strings Steg1.jpg | grep 'SKY'
  ```
- **Found Flag:** SKY-TVJI-2063

####  RSA (Hard)

`factor()` in sage to get primes

- **P** = 13
- **q** = 83 

Flag is `SKY-KRYG-5530`

Solution:

```python
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

ct = [996, 894, 379, 631, 894, 82, 379, 852, 631, 677, 677, 194, 893]
e = 43
p = 13
q = 83
n = 1079
assert p*q == n # jus to check if p & q are right

phi = (p-1)*(q-1)
d = pow(e, -1, phi)
msg = [pow(c, d, n) for c in ct]
print(''.join(chr(m) for m in msg))
```

---

### Password Cracking

#### Rockyou (Easy)
- **Decoded Passwords from Hashes:**
  ```bash
  2233287f476ba63323e60addca1f6b64:kirkles
  32e5f63b189b78dccf0b97ac41f0d228:joybird1
  6539bbb84fe2de2628fc5e4f2a31f23a:ddmack
  68a96446a5afb4ab69a2d15091771e39:emilybffl
  ec5f0b1826389df8622133014e88afde:ryjd1982
  ```

#### Mask (Medium)
- **Cracked with Hashcat:**
  ```bash
  hashcat -a 3 -m 0 hashes.txt 'SKY-HQNT-?d?d?d?d'
  ```
- **Decoded Passwords:**
  ```bash
  06f03267f31077d2c4b5c728472070ae:SKY-HQNT-6598
  d866f4b3b34b598375149fb7661113ab:SKY-HQNT-5981
  674291170dffcf620bda2a604a6820ea:SKY-HQNT-7659
  71b816fe0b7b763d889ecc227eab400a:SKY-HQNT-8765
  d9053951a8d1c15254b46ec9fc974a6b:SKY-HQNT-9816
  ```

#### Pokemon (Medium)
- **Custom wordlist used; no answers provided.**

#### Windows (Medium)
- **Cracked NTLM Hashes with Ophcrack and Hashes.com:**
  ```bash
  # hashes.com
  11cb3f697332ae4c4a3b108f3fa6cb6d:p@ssword
  13b29964cc2480b4ef454c59562e675c:P@ssword
  21c4e7c2efe8e8d1c00b70065ed76aa7:ECTOPLASM32
  47f747c5190dc0f0b921aa4a07f06285:footba11
  65711c079dc4cd3cc2265b23734e0dac:footba11
  fbbda33fc12e83fb0c240e84a183686e:1TRUSTNO1
  a7a0f9afd4a78f531a1cf4c42e531bbf:ectoplasm32


  5473357ae764607c6b78e1cf7d68c4ba:password1
  60e086abe1f3790310a8855d8c8000e6:P@ssword
  ```

---

```plaintext
# oph crack
::E85B4B634711A266AAD3B435B51404EE:FD134459FE4D3A6DB4034C4E52403F16:"=CXU&L::"=Cxu&L
::BA756FB317B622DBAAD3B435B51404EE:C8405270B10B13AE8A24612BB853567A:YHM^GK7::yhM^GK7
::199C926FA387EAB7AAD3B435B51404EE:F196F77BF8BB15781BA8364C649C5FD4:58?-<C6::58?-<C6
::FE4AACAAAD7D986AAAD3B435B51404EE:3928E16F614E2316CA51C336FA5B3011:$XEN@=Y::$xEn@=y
::3613F7EC15407F56AAD3B435B51404EE:C82E164316183AA3AF3EA6BAA642A237:^B7E3D;::^B7e3D;
```

### Law & Order (Hard)
- **Hashes.com Results:**
    ```plaintext
    1e1612db8bdeebc7e8d56f8f30b39456:philadelphia53:MD5
    08038f679de74982bfb9bac43d46271a:unorthodox12:MD5
    3dd9dd0e352df4433aadf2273e269287:resilience05:MD5
    6475c851b56004eb96ab1404252c3a34:hooked37:MD5
    abe6591e06aafc3cf1b0783b120f685e:manhunt74:MD5
    ```

### PDF (Medium)
- Cracking the password took a considerable amount of time. The password was **keanureeves2008**, and the extracted flag was **SKY-KANU-5902**. 
- **Cracking Process:**
    1. Use `pdf2john` to extract the hash.
    2. Remove the PDF prefix.
    3. Run:
    ```bash
    hashcat -m 10700 -a 0 pdfhash.txt rockyou.txt
    ```
    4. The flag was obtained after approximately 2 hours.

### Kali Linux (Hard)
- The user **hollie** had a password cracked using the UNIX EPOCH, which revealed the date **2021-11-03**. The salt is `/WzixhAsn8sdXhCquYzh01` and the hash digest is `KZlio78LilItobsx/17ecFf1e2SbsduhP1sZEWuHrL4`. The cracking was performed by adding the shadow line with the password and executing the following command:
```bash
┌──(hollie㉿kali)-[~]
└─$ john hash.txt --format=crypt
Using default input encoding: UTF-8
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Cost 1 (algorithm [1:descrypt 2:md5crypt 3:sunmd5 4:bcrypt 5:sha256crypt 6:sha512crypt]) is 0 for all loaded hashes
Cost 2 (algorithm specific iterations) is 1 for all loaded hashes
Will run 4 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:04 32.60% 1/3 (ETA: 22:01:07) 0g/s 161.5p/s 161.5c/s 161.5C/s h0llie..q99999
hollie03         (hollie)     
1g 0:00:00:08 DONE 1/3 (2024-10-10 22:01) 0.1194g/s 160.5p/s 160.5c/s 160.5C/s hollie9999917..Hollie9999911
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

### Forensics

#### Version Control (Easy)
- Run `ls -la` after unzipping and `cd` into `.git` to find relevant information. To locate the employee’s email, check `/.git/logs/HEAD`.

- **What is the email address of the employee who was compromised?**
  - `gpeterson@mpd.hacknet.cityinthe.cloud`
- **Each employee is assigned a flag. What is the flag that was compromised?**
  - `SKY-LRHX-4910`
- **Greg thinks that he may have had additional account credentials that were compromised. What's the name of the service provider for that other compromised account?**
  - `Facebook`
- **What was the password on that compromised account?**
  - `waffles85`



#### Doctor (Medium)
- By changing the `.docx` file extension to `.zip`, the contents can be accessed. Inside the `/media` folder, `image0.png` contains the flag **SKY-RATL-8439**.

### Magic Bytes (Medium)
- **What is the original file type?**
  - `png`
- **What is the flag?**
  - `SKY-DSFG-5792`


#### File Carving (Medium)
- Using **Binwalk** on the image (PNG) resulted in 4 PNG files and 1 ZIP. The flag can be found within the ZIP, which contains a total of 6 files. The flag is **SKY-RWCI-4291**.

#### PDF (Easy)
- **What is the name of the program that exported this PDF file?**
  - `Adobe Photoshop CC 2019`
- **What PDF version is this file?**
  - `1.7`
- **What software was used to redact the file and insert a watermark?**
  - `PDFTRON`
- **What is the flag?**
  - `SKY-PDRD-2390`

#### The Book (Hard)
- **Operating System:** Windows (determined using `file memdump.mem`)
- **Computer Name:** DESKTOP-OT97GG3 (found using `vol -f memdump.mem windows.registry.printkey --offset 0xc00154a3e000 --key "ControlSet001\\Control\\"`)
- **Logged In User:** liber8hacker (obtained from the hashdump or files using `vol -f memdump.mem windows.hashdump.Hashdump`)
- **Real Name of "Cloud":** gloria hampton (retrieved by downloading `black_book.db` using `vol -f memdump.mem windows.dumpfile --virtaddr 0xe0003e836f20`)
- **File Path:** \Users\liber8hacker\Desktop\black_book.db (identified as significant due to its association with the user's real name)
- **User's Password:** avatar2 (cracked from hash dump using `vol -f memdump.mem windows.hashdump.Hashdump`)

### Enumeration & Exploitation

#### Python 1 (Easy)
- **What is an input to this program that will result in a correct validation?**
  - `fSeeeeeeel`
  
#### Binary 1 (Medium)
Patch the binary at this line

```nasm
004008e4  837dfc01           cmp     dword [rbp-0x4 {var_c}], 0x0
```

to

```nasm
004008e4  837dfc01           cmp     dword [rbp-0x4 {var_c}], 0x1
```

Which will ensure no matter what password you put, it will always evaluate your tid to a flag

flag: `NCL-EZOF-4024`


#### Timebomb (Easy)
- Decompiling the Java program yields the following answers:
    - **Programming Language:** Java
    - **Exit Code when Not Time:** 10
    - **UTC Time for "Boom":** 2022-07-17 13:12

### Log Analysis

#### SSH (Easy)
- Analyzing the logs reveals:
    - **Hostname of SSH Server:** myraptor
    - **First IP Address to Attack:** 169.139.243.218
    - **Second IP Address to Attack:** 56.13.188.38
    - **Third IP Address to Attack:** 30.167.206.91
    - **Targeted User:** harvey
    - **Successful Login IP Address:** 30.167.206.91

# Nginx (Medium)

- **How many different IP addresses reached the server?**  
  - `47`
- **How many requests yielded a 200 status?**  
  - `19`
- **How many requests yielded a 400 status?**  
  - `38`
- **What IP address rang at the doorbell?**  
  - `186.64.69.141`
- **What version of the Googlebot visited the website?**  
  - `Googlebot/2.1.`
- **Which IP address attempted to exploit the shellshock vulnerability?**  
  - `61.161.130.241`
- **What was the most popular version of Firefox used for browsing the website?**  
  - `31.0`
- **What is the most common HTTP method used?**  
  - `GET`
- **What is the second most common HTTP method used?**  
  - `CONNECT`
- **How many requests were for `\x04\x01\x00P\xC6\xCE\x0Eu0\x00`?**  
  - `6`

#### History (Medium)
- **What did the user search for on Craigslist?**  
  - `bitcoin`
- **What was the current price of Bitcoin when the user was browsing?**  
  - `239.5`
- **What Bitcoin exchange did the user log in to?**  
  - `Coinbase`
- **What is the email that was used to log into the exchange?**  
  - `b1gbird@gmail.com`
- **What was the ID of the Bitcoin transaction that the user looked at?**  
  - `5274cfba585a4b5681527a37f95c76340428916bb7480cef6c545f0a28dcd2d7`
- **What was the total BTC of all the inputs of the Bitcoin transaction?**  
  - `0.22616302`
- **Which Bitcoin address received the majority of the Bitcoin in the transaction?**  
  - `18z6bTFjxkXCmhfp8YBetR2wgmoVjXGJZz`

#### Squid (Hard)
- **In what year was this log saved?**  
  - `2010`
- **How many milliseconds did the fastest request take?**  
  - `5`
- **How many milliseconds did the longest request take?**  
  - `41762`
- **How many different IP addresses did the proxy service in this log?**  
  - `4`
- **How many GET requests were made?**  
  - `35`
- **How many POST requests were made?**  
  - `78`
- **What company created the antivirus used on the host at 192.168.0.224?**  
  - `Symantec`
- **What URL is used to download an antivirus update?**  
  - `http://liveupdate.symantecliveupdate.com/streaming/norton$202009$20streaming$20virus$20definitions_1.0_symalllanguages_livetri.zip`

#### Payments (Hard) (100 points)  
**Cyber Command**  
*A payment transaction log was compromised in a data breach. Help us determine what information was stolen.*

- **How many transactions are contained in the log?**  
  - `192`
- **What is the transaction ID of the largest purchase made in the log?**  
  - `Answer...`
- **Which state made the greatest number of purchases?**  
  - `MA`

#### VSFTPD (Easy)
- Similar to the SSH section, the logs provide necessary information.

#### Custom File Format 
See customfileformat.py, this is the script that answers all the questions.


### Web Application Exploitation

#### Egov (Easy)
- Modify the admin cookie to `true` and navigate to `/admin` to obtain the flag (which may vary).

#### Never Winter Bank (Easy)
- The first question involves accessing `robots.txt` to find a relevant path.
- The second question requires inputting `0100` into the transfer box to retrieve the flag.

# UNFINISHED (Last Updated 03/20/25)
