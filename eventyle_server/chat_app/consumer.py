from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text_data
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))


#
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         pass
#
#     async def receive(self, text_data=None):
#         # Проверяем, что text_data не None и не пустая строка
#         if text_data:
#             try:
#
#                 # Отправляем сообщение всем подключенным клиентам
#                 await self.send(text_data=json.dumps({
#                     'message': text_data
#                 }))
#             except json.JSONDecodeError:
#                 # Логирование ошибки, если данные не могут быть разобраны как JSON
#                 print(f"Не удалось разобрать JSON из {text_data}")
#         else:
#             # Логирование, если text_data пуст
#             print("Получено пустое сообщение")


# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
#
#
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         pass
#
#     async def receive(self, text_data=None):
#         # Проверяем, что text_data не None и не пустая строка
#         if text_data:
#             # Пропускаем обработку JSON, если данные не являются JSON
#             print(f"Received text: {text_data}")
#
#             # Отправляем сообщение всем подключенным клиентам
#             # Предполагаем, что мы хотим повторно отправить полученное сообщение всем клиентам
#             await self.send(text_data=text_data)
#         else:
#             # Логирование, если text_data пуст
#             print("Получено пустое сообщение")

import json
from channels.generic.websocket import AsyncWebsocketConsumer

#
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = f'chat_{self.room_name}'
#
#         # Добавляем текущее WebSocket соединение в группу
#         await Group(self.room_group_name).add(self.channel_name)
#
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         # Удаляем соединение из группы при отключении
#         await Group(self.room_group_name).discard(self.channel_name)
#
#     async def receive(self, text_data=None):
#         if text_data:
#             print(f"Received text: {text_data}")
#
#             # Отправляем сообщение всем подключенным клиентам в группе
#             await Group(self.room_group_name).send(text_data)
#         else:
#             print("Получено пустое сообщение")
