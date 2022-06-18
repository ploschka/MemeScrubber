import api_handler as ah
import os
import time

def like_count(photo):
    return photo['likes']['count']

def space_count(a: int, b: str):
    return (a - len(b))*" "

def main():
    mylogin = input("Login: ")
    print()

    vk = ah.get_vk_api(mylogin)

    while True:
        os.system("clear")
        photos, urls = ah.get_photos(vk)
        s_photos = sorted(photos, key = like_count, reverse = True)
        up_photos = []
        i = 1
        of = len(s_photos)
        for pht in s_photos:
            user = vk.users.get(user_ids = pht['user_id'])[0]
            up_photos.append({"num": str(i), "owner": user['first_name'] + " " + user['last_name'], "id": str(pht['id']), "likes": str(like_count(pht))})
            print("Done", i, "from", of, end="\r")
            i += 1
        os.system("clear")
        print("Place  ", "Owner name              ", "ID        ", "Likes", sep="||", end="||\n")
        for ph in up_photos:
            print(ph['num'] + space_count(7, ph['num']), ph['owner'] + space_count(24, ph['owner']), ph["id"] + space_count(10, ph['id']), ph['likes'] + space_count(5, ph['likes']), sep="||", end="||\n")
        time.sleep(10)


if __name__ == "__main__":
    main()