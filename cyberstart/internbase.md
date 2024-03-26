# Intern Base

### Level 1

- L1C1 Hello World
    - Try selecting the entire page.
    
    Flag: [1337hax@myaboutpage.com](mailto:1337hax@myaboutpage.com)
    
- L1C2 Mixed Up Messages
    - Reverse the text in the post and you will find the flag.
    
    Flag: time4hackattack
    
- L1C3 Social Engineering
    - Briefing
        
        Permission has been granted to try and log into the Chirp social media account of a hacker who goes by the name of **D4YDR3AM**. Luckily for us, they've been clumsy with their personal information. We know their dog's name is **Barkley** and they were born in **1993**. Can you use what we know about them to **guess their password** and get us into their account?
        
        **Tip:** Get the flag by guessing the correct password to log into the account.
        
    - We know that the hackers dog’s name is Barkley and his birth year is 1993 So lets enter the password “Barkley1993”
    
    Flag: Varies
    
- L1C4 Lazy Locked Login
    - Inspect the *Enter* button and change the value from *disabled* to *enabled* and you will get the flag.
    
    Flag: Varies
    

### Level 2

- L2C1 The Rocketeer
    - go to the console and type `launchRocket()` and the flag will appear
    
    Flag: Varies
    
- L2C2 First Contact
    - Click on a planet and enter each of the coords in the url until the flag appears
    
    Flag:Varies
    
- L2C3 Galactic Greetings
    - First, Click the analysis signal button. This will give you a code and after that enter it into a site like [this](https://www.dcode.fr/ascii-code)
    - After decoding the Binary code you will get *“What is twelve minus eight plus one?” .* The answer is 5 and after that decode the answer back into Binary (which is “00000101”) and reply to the Signal
    
    Flag: Varies
    
- L2C4 Rover Rodeo
    - Easy Challenge use the commands *`rover.move()`, `rover.turn('left')`, `rover.turn('right')` and `rover.drill(*)` to get to the flag and for more info use *`rover.info()`*
    
    Flag: Varies
    

### Level 3

- L3C1 Hextraordinary
    - To solve add 0xB105F00D & 0xAAA8400A
    
    Flag: 0x1badb007
    
- L3C2 Maths at Light Speed
    
    Hint: Try watching the source code as you are spinning a new set of numbers. What changes when the spin is happening and then gets removed when the calculator gets locked?
    
    - To solve change the action to `/flashfast/answer`
    - Flag: Varies
- L3C3 Off Balance
    
    Flag: postD4ta_w1zard
    
- L3C4 Final Countdown
    - Using Javascript run `npm install undici` for the packages and below is the code used to solve
    - Javascript Code
        
        ```jsx
        const {fetch} = require("undici");
        
        async function solve() {
            var res = []
            for (var i = 1; i < 6; i++) {
                res.push(await fetch(`https://roambarcelona.com/clock-pt${i}?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D`));
            }
            var str = ""
            for (var i of res) {
                var x = await i.text();
                str += x;
            }
            var answer = await fetch(`https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string=${str}`)
            var answerTxt = await answer.text();
            console.log(answerTxt)
        }
        
        solve().then()
        ```
        
    
    Flag: wh1te_Ro$e