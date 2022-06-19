import vk_api as va
import file_handler as fh
import webbrowser as wb

def __captcha_handler(captcha):

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

def get_vk_api(login: str):
    app_id = 8196809

    user_id, mytoken = fh.__cache(login)

    vk_session = va.VkApi(login = '+79953098236', token = mytoken, app_id = app_id, captcha_handler=__captcha_handler)
    return vk_session.get_api()

def __get_data():
    app_id = 8196809
    redirect_uri = 'https://oauth.vk.com/blank.html'
    display = 'page'
    myscope = 73732
    response_type = 'token'
    URL = 'https://oauth.vk.com/authorize?' + 'client_id=' + str(app_id) + "&" + 'redirect_uri=' + str(redirect_uri) + "&" + 'display=' + str(display) + "&" + 'scope=' + str(myscope) + "&" + 'response_type=' + str(response_type)
    
    wb.open(URL)
    params = input("URL: \n").split('#')[1].split('&')
    print()
    user_id = int(params[2].split("=")[1])
    mytoken = str(params[0].split("=")[1])

    return user_id, mytoken
    
def get_photos(vk):
    photos = []
    urls = []
    groups = fh.__get_groups()
    group_count = len(groups)
    tmp_index = 0
    for i in range(0, group_count):
        tmp_photos = vk.photos.get(owner_id = groups[i]['owner'], album_id = groups[i]['album'], count = 0)
        this_count = tmp_photos['count']
        photos.extend(vk.photos.get(owner_id = groups[i]['owner'], album_id = groups[i]['album'], count = this_count, extended=1)['items'])
        for j in range(0, this_count):
            urls.append(photos[tmp_index + j]['sizes'][len(photos[tmp_index + j]['sizes'])-1]['url'])
        tmp_index += this_count
    return photos, urls