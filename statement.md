# CyberShield

## 1. Problem Statement

Passwords, websites, and files are used every day by people but not everyone thinks about their vulnerabilities at all. Sometimes, it is quite hard for beginners to understand the potential danger or detect them.

CyberShield is designed to provide a simple way to perform some basic cybersecurity checks using Python.

## 2. Project Scope

This project involves the following three fundamental security tests:

* Checking password strength
* Checking URLs for common warning signs
* Checking whether a file has been modified

The purpose of the project is to learn basics of cybersecurity. It does not provide complete security or guarantee that a password, website, or file is completely safe.

## 3. Target Users

CyberShield is mainly intended for:

* Students learning Python and cybersecurity
* Beginners who want to understand basic security checks
* Users looking for a simple security analysis of their files, passwords, and URLs

## 4. High-Level Features

### Password Security

It checks the length of the password and whether it contains upper case letters, lower case letters, numbers, and special characters.

### URL Safety Checker

It checks the URL for basic signs such as HTTPS, a domain, the `@` symbol, and some suspicious words.

### File Integrity Checker

It uses SHA-256 algorithm for comparing hashes to determine whether the file has been altered since it was first hashed.
