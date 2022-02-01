from collections import abc


class LaureateModel:
    def __init__(self, mapping):
        self.__data = mapping

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            # this will return methods as `.items()` and `.keys()`
            return getattr(self.__data, name)
        else:
            return LaureateModel.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        # deal with nested dictionaries
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        # deal with lists
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        # regulr values such as: str, int
        else:
            return obj

