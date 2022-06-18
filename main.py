import vk_api as va
import webbrowser as wb
import requests as rq
import json
import os

def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device

def main():

    client_id = 8196809
    redirect_uri = 'https://oauth.vk.com/blank.html'
    display = 'page'
    myscope = 65540
    response_type = 'token'

    wb.open('https://oauth.vk.com/authorize?' + 'client_id=' + str(client_id) + "&" + 'redirect_uri=' + str(redirect_uri) + "&" + 'display=' + str(display) + "&" + 'scope=' + str(myscope) + "&" + 'response_type=' + str(response_type))

    params = input().split('#')[1].split('&')
    user_id = int(params[2].split("=")[1])
    mytoken = str(params[0].split("=")[1])
    #mytoken = "vk1.a.61ktaWJ6aDpVuJSprMlxNvLl024p58CyuRIxGbW9xSaDRLaIJdVfLdgWxYnks-oIQMstpgPkMFd9nUm8Zb-IqTUGHjuXpve-IMfxb6MkG246rj3OTQO7KfnND_BtdQdN2LlJo06UORaIrx3RzMX4ObqTqXvEXclJgwauck3XZIgmNA5O_5bYWivofTFheRBY"

    print(mytoken)

    
    print("Hello, World!")
    vk_session = va.VkApi(login = '+79953098236', token = mytoken, auth_handler = auth_handler, captcha_handler = captcha_handler, app_id = client_id)
    #vk_session.auth(token_only=True)
    vk = vk_session.get_api()

    photos = vk.photos.get(owner_id = -197700721, album_id = 284717200, count = 0)

    photos = vk.photos.get(owner_id = -197700721, album_id = 284717200, count = photos['count'])

    try:
        os.mkdir("pics")
    except:
        print(end="")

    print(photos['count'])
    
    for i in range(0, photos['count']):
        print(i)
        r = rq.get(photos['items'][i]['sizes'][len(photos['items'][i]['sizes'])-1]['url'])
        with open("pics/" + str(i) + '.jpg', 'wb') as f:
            f.write(r.content)
    print(photos['items'][0]['user_id'])
    

if __name__ == "__main__":
    main()