# Decos

import logging
from functools import wraps
import inspect


class RenameFilter(logging.Filter):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def filter(self, record):
        record.filename = self.filename
        return True


class Log():
    def __init__(self, logger=None):
        self.logger = logger

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            parent_func_name = inspect.currentframe().f_back.f_code.co_name
            module_name = inspect.currentframe().f_back.f_code.co_filename.split("/")[-1]
            if not self.logger:
                self.logger = logging.getLogger(module_name.split('.')[0])
            self.logger.addFilter(RenameFilter(module_name))
            self.logger.debug(f'Функция {func.__name__} вызвана из функции {parent_func_name} '
                              f'в модуле {module_name} с аргументами:'
                              f'{args}; {kwargs}')
            result = func(*args, **kwargs)
            return result

        return wrapper