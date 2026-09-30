# CyberShield Project Report



## Abstract



CyberShield is a Python program designed for use from the command line which shows three basic cybersecurity checks: an analysis of password strength, indicators of risk in a URL, and verification of file integrity by means of SHA-256. The user chooses a check from a menu and then gives the appropriate input for the analysis; the result is displayed in text form. Although CyberShield is intended as an educational tool, the checks it performs do not take the place of proper security software.



## Introduction



In everyday computing, passwords, web links, and unanticipated file changes are all matters of concern. CyberShield has combined a number of basic checks for these areas into a single interactive program, which has a modular design since the menu is separated from the password, URL, and file-checking functions.



## Objectives



- Check the password using a limited number of complexity rules.



- Spot the warning signs that are present in a URL.



- Check the file’s current SHA-256 digest and compare it to a saved one from before.



- Include a terminal interface that is easy to use for carrying out these checks.



## System Design



CyberShield is a Python application which implements SHA-256 hashing using the hashlib module from the standard library. The file main.py handles the display of the menu and passes the user's choice to the appropriate function in the relevant module:



| Module | Responsibility |



| --- | --- |



The main.py file shows the menu, processes the choices made and exits the programme.



The program `password_checker.py` evaluates a password in relation to five rules concerning characters and length.



The script `url_checker.py` evaluates the selected URL indicators and issues warnings.



| `file_checker.py` | Calculates a file digest. Saves it or checks it against another. |



## Operation



### Password analysis



The password checker gives points according to whether the conditions are satisfied. In order to achieve the highest score of 5, the password had to be at least eight characters long and include an uppercase letter, a lowercase letter, a digit, and a non-alphanumeric character; scores in the range 0 to 2 are regarded as weak, those from 3 to 4 are considered medium and 5 is classified as strong. The program then displays the rules which the given password did not meet.



### URL analysis



The URL checker awards points if the URL includes an `https://` prefix, a period, and does not contain an `@` symbol. It then deducts points each time the words `login`, `verify`, or `account` appear; the score is never allowed to go below zero. Finally, the result is given as “Looks safer” (a score of 3), “Use caution” (a score of 2), or “Suspicious signs found” (a score below 2).



### File-integrity analysis



The file checker reads the selected file in binary mode and computes its SHA-256 digest. The user has the option of saving that digest to the file named original_hash.txt or of checking whether the digest of the file in question matches the one stored in the file. If the digests agree, the report states that the file has not changed; if they do not agree, the programme alerts the user to the fact that the file has been modified.



## Assessment



The program is compact and modular since the source code is easy to read and each responsibility specific to a domain—for example, displaying the menu—is handled by a separate module. It shows how conditional logic, the reading of user input, module imports, reading from and writing to files, and hashing can all be used through Python's built-in features.



The checks are intentionally simplistic, and the program’s fairness and effectiveness can be questioned:



The password strength is estimated by means of heuristic methods only; the score does not represent the real entropy of the password and does not take into account the possibility that the password is known to have been compromised. Furthermore, the program gives no protection for the password that has been entered, for example by allowing it to appear in the shell history.



- Similarly, the URL analysis is heuristic and offers no guarantees; it is not enough merely to check that the URL starts with `https://` and does not include suspicious words in order to claim that the URL is safe.



– The file digest provides integrity checking but not confidentiality or authenticity. Since anyone who has writing permissions for the file `original_hash.txt` can alter its contents, they are able to pass any kind of security checks. Additionally, the file is always compared against the same digest, no matter which file is in question, so `original_hash.txt` can be changed to always hold the digest of some other file.



The program fails to deal with file-open errors in a graceful manner and has only limited input validation; furthermore, the project lacks automated tests, and these are not included among the files examined for this report.



## Recommendations



1. You should not treat the results of these checks as an absolute standard and must clearly indicate in the interface that a 'safer' URL result does not imply that the URL is safe.



2. Enter the password using a secure method (for example, by using Python’s `getpass`) and make sure the password is not stored anywhere.



3. Use the urllib.parse library to parse the URL string and break the URL down into its various components. When constructing a URL, use the same library to convert the components back into a string. It might be a good idea to employ an external reputation service in order to enhance the URL checking procedure.



4. Make sure the file digests are stored in such a way that they are associated with specific files, for example, by including them in a JSON object with the file paths used as keys. When the stored digests are read, check that their integrity is intact and deal with any errors that occur when opening a file or when the content is malformed.



5. Prepare unit tests for all of the scoring rules, for the edge cases involving the calculation of the score, and for the situations in which the file original_hash.txt is empty or contains a无效 digest, as well as for the file integrity check procedure.



## Conclusion



CyberShield serves as an excellent illustration of a straightforward terminal application that shows three aspects of cybersecurity within one program; it is easy to understand and thus helps in education and raising awareness, since a user can add extra checks and develop on the cryptographic logic shown by the file-integrity checker. Nevertheless, when considering the program's use as a security tool, attention should be paid to the limitations of the input validation available, the heuristics used for URL and password analysis, and the fact that the saved digest file is not protected.