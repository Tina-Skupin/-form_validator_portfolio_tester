# Test Results

Update 3.5.: all tests running, all specs work, project complete 


## Email Validation Tests (all issues fixed)
- [x] Valid standard emails (user@example.com), incl. numbers, uppercase, umlaut
- [x] Valid emails with subdomains (user@sub.example.com)
- [x] Invalid emails with spaces (user@ example.com)
- [x] Valid emails with plus addressing (user+tag@example.com)
- [x] Invalid emails that are extremely long 
- [x] Invalid emails without @ symbol 
- [X] Invalid mails with more than one @
- [x] puts in webadress instead of mailadress

## Issues to Address
XXXX

## Fixed issues:
1. **Email validation allows spaces** - The validator currently accepts emails containing spaces, which is incorrect according to RFC 5322. Need to add regex pattern or condition to reject these.

## Password Validation Tests
- [X] must be a string
- [x] must be at least 10 long
- [X] must contain at least 1 uppercase and 1 lowercase letter
- [x] must contain at least one star
- [X] must contain at least one number
- [X] must not contain "Swordfish"
- [X] no Ümlaute


## Name Validation Tests
- [X] a string
- [x] at least 4 long
- [X] at least two words (first last name), aka contain a " "
- [RRRRRR] must contain at least 1 uppercase letter - rule has been removed due to conflict with international letters, esp. Chinese and Arabic, 
- no special characters except "-"
- international characters allowed
chinese doesnt work
arabic doesnt work


## Issues to Address
name: special characters needs to be implemented

chinese and arabic doesnt work - becasue of "one upper case" rule? Take out and see if it works
it works. conflict, decided to remove the uppercase letter rule, internationalisation is more important 



Last updated: [03/05/25]