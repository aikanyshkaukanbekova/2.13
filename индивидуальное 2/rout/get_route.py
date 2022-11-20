#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_route(routes):
    """
    Запросить данные о маршруте
    """
    start = input("Название начального пункта маршрута? ")
    finish = input("Название конечного пункта маршрута? ")
    number = int(input("Номер маршрута? "))

    route = {
        'start': start,
        'finish': finish,
        'number': number,
    }
    routes.append(route)
    if len(routes) > 1:
        routes.sort(key=lambda item: item.get('number', ''))
