def check_url():
    print("================================")
    print("      CyberShield - URL")
    print("================================")

    url = input("Enter a URL: ")

    score = 0

    # Words that may sometimes appear in suspicious links
    suspicious_words = ["login", "verify", "account"]

    # Check for HTTPS
    if url.startswith("https://"):
        print("The URL uses HTTPS.")
        score += 1
    else:
        print("The URL does not use HTTPS.")

    # Check for a domain
    if "." in url:
        print("The URL contains a domain.")
        score += 1
    else:
        print("The URL may be invalid.")

    # Check for @ symbol
    if "@" in url:
        print("Warning: The URL contains @.")
    else:
        print("The URL does not contain @.")
        score += 1

    # Check for suspicious words
    for word in suspicious_words:
        if word in url.lower():
            print("Warning: The URL contains", word)
            score -= 1

    # Prevent the score from becoming negative
    if score < 0:
        score = 0

    # Give the final result
    if score == 3:
        result = "Looks safer"
    elif score == 2:
        result = "Use caution"
    else:
        result = "Suspicious signs found"

    print("\nURL Analysis")
    print("------------")
    print("Score:", score, "/ 3")
    print("Result:", result)