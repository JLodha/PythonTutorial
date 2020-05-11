monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March"
}

print(monthConversions.get("Jan"))
print(monthConversions["Feb"])
print(monthConversions.get("This value does not exist"))
print(monthConversions.get("This value again does not exist","This is the way you could modify that output message on invalid key"))
