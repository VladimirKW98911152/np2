# from django import template
#
# register = template.Library()
#
#
# cens = [
#     'как',
#     'автомобилей',
#     'законодательстве',
#     'Питера',
#     'Процессуальный',
#     'Процессуальное',
#     'социологических',
#     'высокие',
#     'менеджменте'
# ]
#
# @register.filter()
# def censor(value):
#     if not isinstance(value, str):
#         raise ValueError('Нельзя цензурировать не строку')
#
#         for word in cens:
#             value = value.replace(word[1:], '*' * (len(word) - 1))
#
#         return value