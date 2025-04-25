# Test Results

## Email Validation Tests
- [x] Valid standard emails (user@example.com), incl. numbers, uppercase, umlaut
- [x] Valid emails with subdomains (user@sub.example.com)
- [x] Invalid emails with spaces (user@ example.com)
- [x] Valid emails with plus addressing (user+tag@example.com)
- [] Invalid emails that are extremely long
- [ ] Invalid emails without @ symbol - ISSUE: Not implemented yet
- [ ] Invalid mails with more than one @ - issue: not implemented yet

## Issues to Address
2. ** mails without @ ** 


## Fixed issues:
1. **Email validation allows spaces** - The validator currently accepts emails containing spaces, which is incorrect according to RFC 5322. Need to add regex pattern or condition to reject these.


Last updated: [25/04/25]