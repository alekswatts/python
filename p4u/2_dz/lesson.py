website = "google.com"

if (website == "google.com") and (len(website) > 8):
    website = website.upper()
    print(website)
    if "COM" in website:
        print("COM COM COM")
        if "O" in website:
            print("FUCK")
elif website == "facebook.com":
    website = "AAAA"
    print(website)
else:
    print("No found")

count = 100 if "GOO" in website else 0
print(count)