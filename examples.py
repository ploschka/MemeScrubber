import file_handler as fh
import api_handler as ah

def main():
    login = "88005553535"
    vk = ah.get_vk_api(login) #Получение объекта VK API, позволяет обращаться к методам
        #API как к методам класса
    photos, urls = ah.get_photos(vk) #Получение списков мемов из альбомов и
        # ссылок на них
    fh.load_pics(urls) #Скачивание всех мемов из альбомов по списку URL
    fh.is_admin(login) #Проверка, является ли пользователь с данным логином админом
    fh.add_admin(login) #Добавление пользователя с указанным логином в список админов

    