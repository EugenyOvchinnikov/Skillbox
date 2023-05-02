class MyDict(dict):
    def get(self, key, default=None):
        return super().get(key, 0)


a = MyDict({'a': 1, 'b': 2})

print(a.get('a'))
print(a.get('e'))
