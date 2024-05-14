from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from . import serializers


def get_all_event_swagger_docs():
    return swagger_auto_schema(
        methods=['get'],
        operation_summary="Возвращает список всех мероприятий",
        operation_description="Данный эндпоинт возвращает список всех мероприятий хранящихся в БД",
        responses={200: "OK"},
    )


def get_user_event_swagger_docs():
    return swagger_auto_schema(
        methods=['get'],
        operation_summary="Возвращает список всех мероприятий пользователя",
        operation_description="Данный эндпоинт возвращает список всех мероприятий в которых участвует пользователь "
                              "хранящиеся в БД",
        responses={200: "OK"},
    )


def post_new_event_swagger_docs():
    return swagger_auto_schema(
        methods=['POST'],
        operation_summary="Создает новое мероприятие",
        operation_description="Данный эндпоинт создает новый обект мероприятия в БД",
        responses={200: "OK"},
        request_body=serializers.EventSerializer
    )


def post_new_user_to_event_swagger_docs():
    return swagger_auto_schema(
        methods=['post'],
        operation_summary="Добавляет пользователя к мероприятию",
        operation_description="Данный эндпоинт добавляет пользователя/пользователей в качестве участника мероприятия",
        responses={200: "OK"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'event_id': openapi.Schema(type=openapi.TYPE_STRING),
                'user_ids': openapi.Schema(type=openapi.TYPE_ARRAY,
                                           items=openapi.Schema(type=openapi.TYPE_STRING)),
            }
        )
    )


def get_all_info_swagger_docs():
    return swagger_auto_schema(
        methods=['get'],
        operation_summary="Возвращает список всей информации",
        operation_description="Данный эндпоинт возвращает список всей информации о всех мероприятиях хранящихся в БД",
        responses={200: "OK"},
    )


def get_event_info_swagger_docs():
    return swagger_auto_schema(
        methods=['get'],
        operation_summary="Возвращает список информации о мероприятии",
        operation_description="Данный эндпоинт возвращает список всей информации о конкретном мероприятии",
        responses={200: "OK"},
        manual_parameters=[
            openapi.Parameter(
                name='event_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='ID мероприятия',
                required=True
            ),
        ]
    )


def post_new_event_info_swagger_docs():
    return swagger_auto_schema(
        methods=['POST'],
        operation_summary="Создает новую информацию о мероприятии",
        operation_description="Данный эндпоинт добавляет новый объект информации о мероприятии в БД",
        responses={200: "OK"},
        request_body=serializers.EventInfoSerializer
    )


def get_event_image_swagger_docs():
    return swagger_auto_schema(
        methods=['get'],
        operation_summary="Возвращает изображение мероприятия",
        operation_description="Данный эндпоинт возвращает изображение конкретного мероприятия",
        responses={200: "OK"},
        manual_parameters=[
            openapi.Parameter(
                name='event_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='ID мероприятия',
                required=True
            ),
        ]
    )


def post_new_event_image_swagger_docs():
    return swagger_auto_schema(
        methods=['post'],
        operation_summary="Добавляет новое изображение мероприятия",
        operation_description="Данный эндпоинт создает новое изображение для определенного мероприятия в БД",
        responses={200: "OK"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'image_id': openapi.Schema(type=openapi.TYPE_STRING),
                'image': openapi.Schema(type=openapi.TYPE_STRING),

            }
        )
    )
