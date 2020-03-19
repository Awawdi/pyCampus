underscore = "_"
str1 = "Aa___________&1"


def check_username(username):
    alphanum = True
    underscore_in_username = underscore in username
    MESSAGE = ""

    for i in username:
        if i != underscore and not i.isalnum():
            alphanum = False
            break

    if not underscore_in_username:
        MESSAGE = "No underscore found in username,"
    if not alphanum:
        MESSAGE += "username contains an illegal character ''%s'' at index %s" % (i, username.index(i))

    return alphanum and underscore_in_username, MESSAGE


print(check_username(str1))

