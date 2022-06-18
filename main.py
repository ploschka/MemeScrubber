import file_handler as fh
import api_handler as ah

def main():
    mylogin = input("Login: ")

    vk = ah.get_vk_api(mylogin)

    photos, urls = ah.get_photos(vk)

    fh.load_pics(urls)

    for i in range(0, len(photos)):
        curr_photo = photos[i]
        if not(curr_photo['likes']['user_likes']):
            while True:
                inp = input(str(i) + " Like or Skip?\n")
                if inp == "Like":
                    vk.likes.add(type = "photo", owner_id = curr_photo['owner_id'], item_id = curr_photo['id'])
                    break
                elif inp == "Skip":
                    break

if __name__ == "__main__":
    main()