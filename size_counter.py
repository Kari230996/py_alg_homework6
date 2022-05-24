import sys

def size_counter(data):
    print(f'{type(data)=} {sys.getsizeof(data)=} {data=}')
    size = sys.getsizeof(data)
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            for key, value in data.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(data, str):
            for item in data:
                size += sys.getsizeof(item)
    return size

