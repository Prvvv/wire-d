# wire-fcked
## A UK based Location & Provider phone number identifier and crawler tool
> This tool was made for a red-team cyber security proof of concept (POC) back in late 2021. To demonstrate how easy it is for attackers to seek out and obtain public mobile numbers and their relevant information, for further information or queries contact me at: ***prv@anche.no***


![](https://i.ibb.co/t8L8jrX/banner.png)

### Overview

"***wire-fcked***" is a provider & location based number identifer designed to output high amounts of valid and contactable UK based phone numbers specific to an area or mobile provider chosen.

It is designed for operational security and research purposes to provide high amounts of valid UK based phone numbers.


![](https://i.ibb.co/YX0wD4X/sc1.png)

### How does it work?

The tool works by numerically matching up 9 - 11 digit numbers in a specific format using a custom algorithm and then attempting to gather information on the numbers as if it was a valid UK phone number, once a valid peice of information on that number has been found during the lookup process, this means the mobile number is valid- and will now attempt to gather more information about the now found phone number specific to the users request (whether it be location or provider) using open source number lookups and databases, and then outputing them in mass to the user.

### How effective is it?

Well, it all depends on the specific term of search a user wishes to make.

But given a large or common provider is chosen by the user, such as ***EE*** or ***O2 Mobile*** then it can generate up to a couple thousand valid phone numbers a minute.

If a user has chosen to find numbers based of a more specific term (such as a location or less common cell provider) then it may only generate from 10 to 100 per minute (it really depends)

![](https://i.ibb.co/DKpZrJS/sc2.png)







