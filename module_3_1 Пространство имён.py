calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    length = len(string)
    up = string.upper()
    low = string.lower()
    return (length, up, low)
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list_to_search)
result1_1 = string_info('Poleteli Guravli')
result1_2 = string_info('Улетели журавли :(')
result2_1 = is_contains('Fort', ['Боярд', 'forT', 'Старец Фура'])
result2_2 = is_contains('Парк', ['имени', 'Ленина', 'Ильича'])
print(result1_1)
print(result1_2)
print(result2_1)
print(result2_2)
print(calls)