from cmath import log
import api_handler as ah
import yaml as ya
import os
import requests as rq

def __hash(login: str):
    hs = 0
    i = 1
    for j in login:
        hs += ord(j.encode("utf8"))*(2**i)
    return hs


def __is_in_yaml(value: str, list: list):
    for i in list:
        if value in i.values():
            return True, i
    return False, i

def __cache(mylogin: str):
    try:
        file = open("accounts.yaml", "r+")
        accs = ya.safe_load(file)
        is_he_in, usr = __is_in_yaml(mylogin, accs)
        if is_he_in:          
            user_id = usr["id"]
            mytoken = usr["access_token"]
        else:
            user_id, mytoken = ah.__get_data()
            dict = {"login": mylogin,"id": user_id, "access_token": mytoken}
            ya.dump([dict], file)
    except FileNotFoundError:
        file = open("accounts.yaml", "w+")
        user_id, mytoken = ah.__get_data()
        dict = {"login": mylogin,"id": user_id, "access_token": mytoken}
        ya.dump([dict], file)
    finally:
        file.close()
        return user_id, mytoken

def __get_groups():
    file = open("albums.yaml", "rt")
    groups = ya.safe_load(file)
    return groups

def load_pics(urls: list):
    try:
        os.mkdir("pics")
        of = len(urls)
        for i in range(0, len(urls)):
            print("Done ", i+1, "/", of, end="\r", sep="")
            req = rq.get(urls[i])
            with open("pics/" + str(i) + ".jpg", "wb") as file:
                file.write(req.content)
    except FileExistsError:
        pass

def is_admin(login: str):
    file = open("admins.yaml", "rt")
    admins = ya.safe_load(file)
    file.close()
    return __hash(login) in admins

def add_admin(login: str):
    try:
        if not(is_admin(login)):
            file = open("admins.yaml", "at")
            ya.dump(__hash(login), file)
            file.close()
    except FileNotFoundError:
        file = open("admins.yaml", "at")
        ya.dump([__hash(login)], file)
        file.close()
