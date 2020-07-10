# Strong-Password-Generator
Generates safe, strong passwords and saves them locally on your computer.

## Information
This was made to help you improve your security. A lot of people (including celebrities) get hacked every day, and this is becoming a problem.
Ava Rose (a famous TikToker) was recently hacked and I asked myself "how?". Well, this action inspired me and made me take a deeper look at why and how she was hacked. Not only did her Instagram account get hacked, but also her Snapchat.
![](https://i.imgur.com/bHzYpJg.png)<br/><br/>
You might ask yourself, what consequences could this kind of a hack lead to? Well, this made the hacker able to see all her private DM's and also capable of contacting any of her friends using her account, view her private photos, shout himself out (the hacker gained 9K followers in 12h) and more.

## How did Ava Rose get hacked?
As the hacker got access to both her Instagram- and Snapchat account, I'm sure we can all agree on that the hacker either got access to her email and reset the passwords or she was using the same password on both platforms. So how did the hacker get access to her password(s)? Well, there are several ways of hacking a user. I am going to leave a few methods down below — I'm sure there are more methods but here are a few I just thought of and was possibly used to hack Ava Rose.

- Brute Force Attack — automate the process of trying different combinations of passwords. There are "most commonly used passwords" lists online that you could download. The list would most likely look something like this: "qwerty123, 123456789, passw0rd, ...". As these are easy to remember passwords, people tend to use these kind of passwords. But that is of course easy to brute force/guess which makes them bad passwords.
- Social Engineering — simple method to gain trust and collect data. You can for instance send a spoofed email (great example here: https://emkei.cz/) with the name of someone else (it could be a friend of the target) and include a keylogger, R.A.T (Remote Access Trojan) or a fake login page that sends you the account credentials the user inputs.
- Network Monitoring — capture network traffic. You should never use a public Wi-Fi in e.g. airports, cafés or restaurants if you care about your security. However, if you choose to connect to a public Wi-Fi then you should be careful and make sure you don't log in to any website/application or send sensitive information. That is simply because viewing network traffic is accessible by anyone who has the the correct tools and there are several tutorials of this online.
- Password Guessing — you can brute force and make the process quicker but if you have enough information of this person (e.g. date of birth, pets, school and interests) it would possibly only take a few tries. A lot of people tend to use the password form: {Name}{Year of Birth} as it is easy to remember and it's static unlike your age that increases every year. That is exactly why you should use a password generator like [this](https://github.com/zoony1337/Strong-Password-Generator/blob/master/main.py).
- Recovery Codes — brute force recovery codes. This is often used if you know your target has an "unbruteforcable" password. Most websites/applications have a "Forgot password?" option which you can use to enter your recovery code in case of a forgotten password. If the actual password isn't their pet's name for instance, there is a chance the recovery code is.
- Database Dumping — access a database and reveal a detailed record of tables. You can do this on weak websites you are sure the user has registered on, if they use the same password on other websites/applications the chances are high that the hacker gets access to multiple accounts. That is why you should never use the same password on multiple websites. There are a lot of tutorials online on how to do dump databases, but you should also be aware that the passwords would most likely be encrypted. You would have to find the correct format and decrypt the password unless they're using a format like Bcrypt (afaik it's impossible to decrypt).
- Database leaks — dumped databases that have been leaked. You can use something like [this](https://github.com/zoony1337/Email-to-Password) to detect if the email/password has been leaked. If it has, you can try to find the leak and filter your target.
- Physical Action — if you know the target in real life or somehow get access to the person's phone/computer you can view saved passwords.

I hope you learned something new today and I think we should all use password generators as it decreases the risks of being hacked. I'm aware that people can use this for bad and illegal purposes. I am not accountable for anything you get into, this was just a speedrun to demonstrate how hacking accounts can be done.

## What can I do to prevent getting hacked?
- Use different passwords for different websites/applications.
- Enable 2FA (two-factor authentication) if possible.
- Use strong generated passwords (use an [open source](https://github.com/zoony1337/Strong-Password-Generator/blob/master/main.py) one and not some random generator someone sends you).
- Do not trust anyone.
- Think twice when you receive a fishy message.

## Previews
![](https://i.imgur.com/IqkjGVI.png)<br/>
![](https://i.imgur.com/KNst0FA.png)
