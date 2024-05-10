from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from . import serializers


def get_user_profile_info_swagger_docs():
    return swagger_auto_schema(
        methods=['get'],
        operation_summary="Возвращает информацию о пользователе",
        operation_description="Данный эндпоинт возвращает информацию о авторизированном пользователе",
        responses={200: "OK"},
    )


def get_user_profile_image_swagger_docs():
    return swagger_auto_schema(
        methods=['get'],
        operation_summary="Возвращает аватарку пользователя",
        operation_description="Данный эндпоинт возвращает изображение являющееся аватаркой пользователя",
        responses={200: "OK"},
        manual_parameters=[
            openapi.Parameter(
                name='user_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='id пользователя',
                required=True
            ),
        ]
    )


def get_searching_user_profile_swagger_docs():
    return swagger_auto_schema(
        methods=['get'],
        operation_summary="Возвращает список пользователей",
        operation_description="Данный эндпоинт возвращает список всех пользователей удовлетворяющих условию поиска",
        responses={200: "OK"},
        manual_parameters=[
            openapi.Parameter(
                name='searchQuery',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Запрос поиска',
                required=True
            ),
        ]
    )
