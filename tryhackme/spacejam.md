# NOTE: This was a blog from *vipin.xyz* see [this](https://www.vipin.xyz/blog/archive)

# Space Jam | TryHackMe KOTH

My First (Private) King Of The Hill

Released: 2024-03-31

## Foreword

Hey guys, I wanted to share with everyone how my first KOTH experience went. It was a private session because I wanted to grasp the mechanics of the game. I livestreamed it on YouTube, and you can watch the non-edited version [here](https://www.youtube.com/watch?v=FgowvD_mTcs) (will be updated to the edited version when I edit the livestream). Hope you enjoy!

## NMAP Scan

- A first step for any machine is a NMAP scan. My NMAP command was ```nmap -sS -sV $IP```

```bash
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-30 00:18 EDT
Nmap scan report for 10.10.70.26
Host is up (0.093s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
23/tcp   open  telnet  Linux telnetd
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
3000/tcp open  http    Node.js (Express middleware)
9999/tcp open  http    Golang net/http server
```

- Ignore Port 9999 as it is part of the KOTH infrastructure.

## Enumeration & Dirsearch

- The obvious next step is to conduct a directory scan as there isn't any leads.

![Image showing dirsearch](blog/spacejam/dirsearch.png 'Fig.1')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1</small>
</div>

- Sorry for the bad image quality as this was screenshotted from my livestream, but let's check out some of these directories.

- Most of the directories were unusual and useless like the one below

![Image showing carrot](blog/spacejam/carrot.png 'Fig.2')
<div style={{ textAlign: 'center' }}>
  <small>Fig.2</small>
</div>

- So I switched gears by checking out different ports. 3000 seems to be how we get our shell.

![Image showing port 3000](blog/spacejam/port3000.png 'Fig.3')
<div style={{ textAlign: 'center' }}>
  <small>Fig.3</small>
</div>

## Getting a shell

![Image showing me getting RCE](blog/spacejam/RCE.png 'Fig.4')
<div style={{ textAlign: 'center' }}>
  <small>Fig.4</small>
</div>

- After a couple of tries I found a way to get RCE as seen in Fig.4 above.

- To make running commands easier, let's get a shell. I used [revshells.com's](https://www.revshells.com/) Busybox reverse shell command.

![Image showing me getting a Rev shell](blog/spacejam/revshellcommand.png 'Fig.5')
<div style={{ textAlign: 'center' }}>
  <small>Fig.5</small>
</div>

- And running it gets me a reverse shell 🎉!

![Image showing me getting a pty and running sudo -l](blog/spacejam/ptynsudo.png 'Fig.6')
<div style={{ textAlign: 'center' }}>
  <small>Fig.6</small>
</div>

- As soon as I got a shell, I ran ```python -c'import pty; pty.spawn("/bin/bash")'``` to get a PTY and ```sudo -l``` to see what perms I have. And it seems like I have full root access.

## Flags, King.txt, and Final Thoughts

- I ran ```echo "vipin.b" > king.txt``` to put my name in the king.txt file.

- I also found the user flag in the user folder's and the root flag in */root*

> Aren't we done vipin?

- At this point we need to maintain root access, a good tool would be [this](https://github.com/MatheuZSecurity/Koth-TryHackMe-Tricks), it contains a bunch of tips and tricks you can use to maintain your king access. I wasn't very familiar with some of these tricks so I didn't really try to use them. Maybe my next public KOTH I will.

### MACHINE PWN'ED 😎
