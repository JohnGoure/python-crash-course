usernames = ["jgoure", "johngoure", "admin",
             "destinydeleon80", "jgoure30", "ghazi30"]

new_users = ["berrybear", "stargazedpirate",
             "trailblazermater", "bunchamunch",
             "jgoure"]

for new_user in new_users:
    if new_user.lower() in usernames:
        print("Please enter a new username.")
    else:
        print("The username is available.")
