immutable_tuple = (4, 5, 6)
immutable_tuple[0] = 404
x = 100
y = 200
x, y = y, x
# пустой кортеж
empty_tuple = ()
 
# кортеж из 4-х элементов разных типов
four_el_tuple = (36.6, 'Normal', None, False)
 
# пример tuple, что содержит вложенные элементы
nested_elem_tuple = (('one', 'two'), ['three', 'four'], {'five': 'six'}, (('seven', 'eight'), ('nine', 'ten')))
print(nested_elem_tuple)
def get_status(service_name):
    return None, f"service {service_name} is OK!"

print(type(get_status('nginx')))
tuple_creation = tuple('any iterable object')

print(tuple_creation)
is_tuple = ('a',)
is_tuple_too = 'b',
not_a_tuple = 'c'
 
print(type(is_tuple))
print(type(is_tuple_too))
print(type(not_a_tuple))
# Mike - [0], Leo - [1], Don - [2], Raph - [3]
turtles = ('Mike', 'Leo', 'Don', 'Raph')
# Mike - [-4], Leo - [-3], Don - [-2], Raph - [-1]
 
print(turtles[1])
print(turtles[-2])
print(turtles[2] == turtles[-2])
