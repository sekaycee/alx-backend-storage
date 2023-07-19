#!/usr/bin/env python3
''' task: Working with Redis '''

class Cache:
    ''' represent an object for storing data in a Redis data storage. '''
    def __init__(self) -> None:
        ''' initialize a Cache instance. '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' store a value in a Redis data storage and returns the key. '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
