import file_handler as fh
import api_handler as ah

def main():
    mylogin = input("Login: ")
    print()

    vk = ah.get_vk_api(mylogin)

    photos, urls = ah.get_photos(vk)

    fh.load_pics(urls)

    for i in range(0, len(photos)):
        curr_photo = photos[i]
        user = vk.users.get(user_ids = curr_photo['user_id'])[0]
        print("Author:", user['first_name'], user['last_name'], "Likes =", curr_photo['likes']['count'], end = ". ")
        if (curr_photo['likes']['user_likes']):
            print("You've already leaved a like", end = "")
        print()
        while True:
            inp = input(str(i) + " Like or skip?\n")
            if inp == "Like" or "like" or "L" or "l":
                vk.likes.add(type = "photo", owner_id = curr_photo['owner_id'], item_id = curr_photo['id'])
                break
            elif inp == "Skip" or "skip" or "S" or "s":
                break

if __name__ == "__main__":
    main()