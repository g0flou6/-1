calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    info = []
    le = len(string)
    up = string.upper()
    low = string.lower()
    info.append(le), info.append(up), info.append(low)
    return print(tuple(info))

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    for i in list_to_search:
        if string_lower in i.lower():
            return True
    return False

string_info('Crocodile')
string_info('Stratosphere')
print(is_contains('PR', ['privet', 'hello']))
print(is_contains('mega', ['giant', 'great']))
print(calls)


