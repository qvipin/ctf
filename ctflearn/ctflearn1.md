# NOTE: This was a blog from *vipin.xyz* see [this](https://www.vipin.xyz/blog/archive)

# CTFLearn Writeup Pt. 1

How I solved each challenge!

Released: 2024-02-2

# Author's note

This part of the write-up, along with the others, will contain most of the solutions for the CTFlearn CTF Challenges. Some of the first ones were skipped because I had already completed them and didn't feel like making a solution for them. Most of the solutions in this part is the cryptography/misc/forensics challenges. Hope you enjoy!

## Vignere Cipher

- I used [dcode.fr's Vigenere Decoder](https://www.dcode.fr/vigenere-cipher) as seen in Fig.1 below.

![Image showing how to decode the cipher with dcode.fr](blog/ctflearn1pics/vignere1.png 'Fig.1')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1</small>
</div>

Flag: ```flag{CiphersAreAwesome}```

## Reverse Polarity

- I used CyberChef and decoded the text from binary. CyberChef recipe [here](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)&input=MDEwMDAwMTEwMTAxMDEwMDAxMDAwMTEwMDExMTEwMTEwMTAwMDAxMDAxMTAxMDAxMDExMTAxMDAwMTAxMTExMTAxMDAwMTEwMDExMDExMDAwMTEwMTAwMTAxMTEwMDAwMDExMTAwMDAwMTEwMTAwMTAxMTAxMTEwMDExMTExMDE).

Flag: ```CTF{Bit_Flippin}```

## Wikipedia

- Interesting challenge, on wikipedia you can search for a user through their IP address and see their contributions and you can see they contributed to an article called *"flag"*.

![Image showing where the flag is on the article](blog/ctflearn1pics/wikipedia1.png 'Fig.2')
<div style={{ textAlign: 'center' }}>
  <small>Fig.2</small>
</div>

- And as seen above, we have the flag!

Flag: ```cNi76bV2IVERlh97hP```

## Hextroadinary

- Using a XOR calculator like [xor.pw](https://xor.pw/) we can input both values in to get the flag.

![Image showing me using xor.pw to get the flag](blog/ctflearn1pics/xorchall1.png 'Fig.3')
<div style={{ textAlign: 'center' }}>
  <small>Fig.3</small>
</div>

- Make sure that you add a ```0x``` in front of the output or the flag will be incorrect.

Flag: ```Oxc0ded```

## Accumulator

- **Foreword:** This challenge was rated easy and was only worth 10 points, even though it was a buffer overflow challenge. It can seem difficult to beginners, however this is a fairly easy challenge **if** you know what you are doing.

- The challenge is a simple buffer overflow challenge. Below is how I solved it.

```bash
❯ nc rivit.dev 10009
acc = 0
Enter a number: 1111
acc = 1111
Enter a number: 11111111111
You can't enter the negative number!
acc = 1111
Enter a number: 111111111
acc = 111112222
Enter a number: 1111111111
acc = 1222223333
Enter a number: 11111111111111
acc = 1252939692
Enter a number: 1111111111111111
You can't enter the negative number!
acc = 1252939692
Enter a number: 11111111111
You can't enter the negative number!
acc = 1252939692
Enter a number: 11111111111111
acc = 1283656051
Enter a number: 11111111111111111
acc = 1935244090
Enter a number: 11111111111111111111
You can't enter the negative number!
acc = 1935244090
Enter a number: 11111111111111111
You win! acc = -1708135167
CTFlearn{n3x7_7yp3_0f_0v3rf0w}
❯
```

Flag: ```CTFlearn{n3x7_7yp3_0f_0v3rf0w}```

## Time Traveller

- To find the email, we can use a tool called "The Wayback Machine" and look for a snapshot on December 31 1996. 
- If you are having trouble getting to the page, click [here](https://web.archive.org/web/19961231235847/http://www.nasa.gov/) for the link.

Flag: ```CTFlearn{today@nasa.gov}```

## WOW.... So Meta

- Using [Aperisolve's](https://www.aperisolve.com/) EXIF tool, we can see the metadata of the image (Fig.4).

![Image showing where the flag is in the exif section](blog/ctflearn1pics/exifchall1.png 'Fig.4')
<div style={{ textAlign: 'center' }}>
  <small>Fig.4</small>
</div>

- As shown above in *Figure 4*, the flag is found under ***XMP Microsoft***

Flag: ```flag{EEe_x_I_FFf}```

## BruXOR

- The best tool for XOR bruteforcing (in most cases) is the Cyberchef's XOR Bruteforce. Cyberchef Recipe link [here](https://gchq.github.io/CyberChef/#recipe=XOR_Brute_Force(1,100,0,'Standard',false,true,false,'flag')&input=cXt2cGxuJ2JIX3Zhckh1ZWJjcnF4ZXRySE9YRWo).

Flag: ```flag{y0u_Have_bruteforce_XOR}```

## Modern Gaius Julius Caesar

- Most cipher identifiers cannot identify it, except dcode.fr's cipher identifer. There I saw *Keyboard Shift Cipher* and the challenge description mentioned the word *"keyboard'*. 
- Attempting to decode from Keyboard Shift Cipher gives us the flag.

![Image showing the keyboard shift cipher in use](blog/ctflearn1pics/keyshift1.png 'Fig.5')
<div style={{ textAlign: 'center' }}>
  <small>Fig.5</small>
</div>

- Remember that even if you get `CTFlearn{Cyb3rCae54r}`, ensure that you add an underscore or the flag will be incorrect.

Flag: ```CTFlearn{Cyb3r_Cae54r}```

## Snowboard

- A simple image forensics challenge where a *Base64* encoded string can be found in the strings, and decoding it gives us the flag. 

![Image showing where the flag is in the strings section](blog/ctflearn1pics/snowboard1.png 'Fig.6')
<div style={{ textAlign: 'center' }}>
  <small>Fig.6</small>
</div>

- Beware of the fake flag, it didn't stump me but it did for other people.

Flag: ```CTFlearn{SkiBanff}```

## PikesPeak

- This is another strings challenge, but we are faced with an issue as seen in Fig. 7.

![Image showing the flags in the strings section](blog/ctflearn1pics/peaks1chall.png 'Fig.7')
<div style={{ textAlign: 'center' }}>
  <small>Fig.7</small>
</div>

- With all these flags it can seem difficult to find which is the correct one, but the way to figure out the right one is by making sure it follows the CTFlearn flag format. To find the correct formatting we can look at the flag box's example flag.

Flag: ```CTFlearn{Gandalf}```

## My Blog

- A simple, fun challenge. If you are having trouble, try looking at the bolded words in the description (**Application** & __Memory__)

- To solve this I instantly went to the Application tab in inspect element, however nothing seemed to appear on the main landing page in *Local Storage*, however when I went to the blog page and looked in *Local Storage*, I found the flag.

![Image showing the flags the application section in inspect element](blog/ctflearn1pics/myblogchall1.png 'Fig.8')
<div style={{ textAlign: 'center' }}>
  <small>Fig.8</small>
</div>

- Make sure to replace flag with CTFlearn as it says in the description.

Flag: ```CTFlearn{n7f_l0c4l_570r463_15n7_53cur3_570r463}```

## My Friend John

- **WAIT!** *john* is a foe not a friend (when it comes to ZIP Cracking), instead use *fcrackzip* for a simpler experience. 

- Download the zip and install *fcrackzip*. 

```bash

❯ sudo fcrackzip -u -D -p /Users/vipin/tech/CTFs/rockyou.txt -u use-rockyou.zip


PASSWORD FOUND!!!!: pw == kdbs0429

``` 

- Just when we thought it was over... We are presented with another ZIP plus a wordlist in _use-rockyou.zip_. Let's crack this one!

```bash

❯ sudo fcrackzip -u -D -p /Users/vipin/Downloads/customlist.txt -u /Users/vipin/Downloads/customlist.zip


PASSWORD FOUND!!!!: pw == 1N73rD3N0M1N4710N41

```
- Bruh, there is another one inside of it 🙄.

```bash

❯ sudo fcrackzip -u -D -p /Users/vipin/Downloads/rockyou.txt -u /Users/vipin/Downloads/brute-force-pin.zip
sh: -c: line 0: unexpected EOF while looking for matching ``'
sh: -c: line 1: syntax error: unexpected end of file
^C^C

PASSWORD FOUND!!!!: pw == 991337

```

- And finally we see the beloved *flag.txt* after cracking app those ZIP's 😮‍💨.

Flag: ```CTFlearn{s0_n0W_y0uv3_M3t_J0hN}```

# Final Note

This is only the first part of all the CTFlearn writeup's. Next CTFlearn writeup will cover more REV & Binary challenges, so be on the lookout 👀.