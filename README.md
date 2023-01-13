# LAB - Class 19

## Project: automation

### Author: Eric Mungai Kinuthia

### About

This project utilizes regex to find and collect all email addresses and phone numbers given a document with the two types of contacts. Once emails and phone contacts are found they are stored in two separate documents.

### How to initialize application

`python3.11 automation/automation.py`

### Tests

To runs tests use `pytest -k test_automation.py`

Tests include:

1. Checking whether we can grab information from file system.

2. Checking to see if we can extract phone numbers from text document.

3. Checking to see if we can extract emails from text document.

4. Checking to see if we can write files with extracted emails and phone numbers