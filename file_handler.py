import api_handler as ah
import yaml as ya
import os
import requests as rq


def is_in_yaml(value: str, list: list):
    for i in list:
        if value in i.values():
            return True, i
    return False, i

def cache(mylogin: str):
    try:
        file = open("accounts.yaml", "r+")
        accs = ya.safe_load(file)
        is_he_in, usr = is_in_yaml(mylogin, accs)
        if is_he_in:          
            user_id = usr["id"]
            mytoken = usr["access_token"]
        else:
            user_id, mytoken = ah.get_data()
            dict = {"login": mylogin,"id": user_id, "access_token": mytoken}
            ya.dump([dict], file)
    except FileNotFoundError:
        file = open("accounts.yaml", "w+")
        user_id, mytoken = ah.get_data()
        dict = {"login": mylogin,"id": user_id, "access_token": mytoken}
        ya.dump([dict], file)
    finally:
        file.close()
        return user_id, mytoken

def get_groups():
    file = open("groups.yaml", "rt")
    groups = ya.safe_load(file)
    return groups

def load_pics(urls: list):
    try:
        os.mkdir("pics")
        for i in range(0, len(urls)):
            req = rq.get(urls[i])
            with open("pics/" + str(i) + ".jpg", "wb") as file:
                file.write(req.content)
    except FileExistsError:
        pass