import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time
import os

def main():
    tok = os.environ.get('bottoken')
    vk_session = vk_api.VkApi(token=tok)
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            while True:
                time.sleep(6)
                vk.messages.send(
                    peer_id=267526362,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Казино'
                )

if __name__ == '__main__':
    main()
