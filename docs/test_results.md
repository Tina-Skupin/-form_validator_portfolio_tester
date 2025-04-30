# Test Results

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
- [] must be at least 10 long
- [] must contain at least 1 uppercase and 1 lowercase letter
- [] must contain at least one star
- [] must contain at least one number
- [] must not contain "Swordfish"
- [] no Ümlaute
- [] 




Last updated: [25/04/25]