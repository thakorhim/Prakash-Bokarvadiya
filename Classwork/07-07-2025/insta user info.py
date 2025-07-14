
#{"message":"Please wait a few minutes before you try again.","require_login":true,"igweb_rollout":true,"status":"fail"}
# This script retrieves and displays Instagram user profile information using the Instaloader library.
import instaloader
#user login
L = instaloader.Instaloader()
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
try:
    L.login(username, password)
    print("Login successful.")
    profile = instaloader.Profile.from_username(L.context, username)
    print("Username:", profile.username)
    print("Full Name:", profile.full_name)
    print("Bio:", profile.biography)
    print("Followers:", profile.followers)
    print("Following:", profile.followees)
    print("Posts:", profile.mediacount)
    print("Post downloads:", [post.download() for post in profile.get_posts()])
    instaloader.Instaloader().download_profile(username, profile_pic_only=True)
    print("Profile picture downloaded.")

except instaloader.exceptions.BadCredentialsException:
    print("Invalid username or password.")
    exit()



# Get profile information

