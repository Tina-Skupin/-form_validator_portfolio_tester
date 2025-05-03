# Form Validator Testing Portfolio

A Python project demonstrating thorough testing techniques for form validation.

## Project Overview

This project showcases my approach to testing form validation logic, with a focus on:
- Comprehensive test coverage
- Edge case handling
- Test documentation
- Clean code practices

## Structure

form-validator/
│
├── src/
│   ├── __init__.py
│   └── validator.py        # Main validation logic
│
├── tests/
│   ├── __init__.py
│   └── test_validator.py   # Unit tests
│
├── docs/
│   ├── test_plan.md        # testing strategy
│   └── edge_cases.md       # Documentation of edge cases
│
├── README.md               # Project overview
└── requirements.txt        # Dependencies




## Features Demonstrated
Unit testing with Python's unittest framework
Test-driven development approach
Edge case handling
Input validation for:
Email (format validation)
Passwords (strength, character requirements, security)
Names (international character support, format validation)

## running the project
enter your testdata in "validator.py" lines 4-6
run the code from "src" with "python validator.py"
or, if that doesn't work, try "python3 validator.py"

## running the tests
from the root of the project, run "python -m unittest discover -v"

## lessons and future improvement
rules that feel valid can inhibit a diferent rule
future idea: automate the input so that info gets piped in automatically
testing still rules

### contact
Tina Skupin
https://www.linkedin.com/in/tina-skupin-70b94a53/




