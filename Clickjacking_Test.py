import requests

url = input("Enter website URL: ")

try:
    response = requests.get(url)
    x_frame_options = response.headers.get('X-Frame-Options')
    if x_frame_options is None:
        print("This website is vulnerable to clickjacking.")
        print("To fix this, add the X-Frame-Options header to the server response.")
        print("The header should have one of the following values:")
        print("DENY: Prevents the page from being displayed in a frame.")
        print("SAMEORIGIN: Allows the page to be displayed in a frame on the same origin.")
        print("ALLOW-FROM uri: Allows the page to be displayed in a frame from the specified uri.")
    elif x_frame_options == 'DENY':
        print("This website is not vulnerable to clickjacking.")
    elif x_frame_options == 'SAMEORIGIN':
        print("This website is partially vulnerable to clickjacking.")
        print("To fix this, set the X-Frame-Options header to DENY or ALLOW-FROM uri.")
    else:
        print("This website is partially vulnerable to clickjacking.")
        print("To fix this, set the X-Frame-Options header to DENY or SAMEORIGIN.")
except requests.exceptions.RequestException as e:
    print("Error: ", e)
