import urllib.request, json, base64
token = input("Token: ").strip()
choice = input("1=Bravery 2=Brilliance 3=Balance 4=Leave: ").strip()
if choice not in "1234":
    exit("Invalid")
house_id = int(choice) if choice in "123" else None
method = "DELETE" if house_id is None else "POST"
url = "https://discord.com/api/v9/hypesquad/online"
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://discord.com",
    "Referer": "https://discord.com/channels/@me",
    "X-Super-Properties": base64.b64encode(json.dumps({
        "os": "Windows",
        "browser": "Chrome",
        "client_build_number": 280133
    }).encode()).decode()
}
body = json.dumps({"house_id": house_id}).encode() if method == "POST" else None
req = urllib.request.Request(url, data=body, headers=headers, method=method)
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        print("Success" if r.status == 204 else f"Status {r.status}")
except Exception as e:
    print("Error:", e)
