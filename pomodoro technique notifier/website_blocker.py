import time
from datetime import (datetime, timedelta)


hostsFilePath = r"C:\Windows\System32\drivers\etc\hosts"
redirect_IP = "127.0.0.1"
website_list = ["www.facebook.com", "web.facebook.com",
                "www.instagram.com", "www.youtube.com"]


def web_blocker(end_time):
    time_now = datetime.now()
    end_time = time_now + timedelta(seconds=end_time)
    while True:
        if datetime.now() < end_time:
            with open(hostsFilePath, "r+") as file:
                content = file.read()
                for website in website_list:
                    if website not in content:
                        file.write(redirect_IP + " " + website + "\n")
        else:
            with open(hostsFilePath, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
            break
        time.sleep(5)
