import configuration
import requests

# функция для создания заказа с заданным телом
def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

# Запрос на получение информации о заказе по его трек-номеру
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track))
