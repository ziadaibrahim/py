users = [{"name": "omar", "pass": "123"}, {"name": "ahmed", "pass": "456"}]

def check(username, password):
    for i in users:
        if i["name"].lower() == username.lower() and i["pass"] == password:
            return True
    return False

