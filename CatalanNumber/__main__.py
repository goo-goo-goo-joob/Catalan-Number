import argparse
import multiprocessing
import os
import sys

import gunicorn.app.base
from configargparse import ArgumentParser
from setproctitle import setproctitle
from typing import Callable


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CatalanProject.settings')


def number_of_workers():
    return multiprocessing.cpu_count() * 2 + 1

def clear_environ(rule: Callable):
    for name in filter(rule, tuple(os.environ)):
        os.environ.pop(name)


ENV_VAR_PREFIX = 'GUNICORN_'

parser = ArgumentParser(
    auto_env_var_prefix=ENV_VAR_PREFIX, allow_abbrev=False,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
group = parser.add_argument_group('Gunicorn Options')
group.add_argument('--socket', type=str, help='Unix socket server would listen on')
group.add_argument('--workers', type=int, default=number_of_workers(), help='Number of workers')
group.add_argument('--access-logfile', type=str, default='-', help='log file')
group.add_argument('--timeout', type=int, default=60, help='Process timeout')
group.add_argument('--settings-root', type=str, help='Settings file directory')


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def main():
    args = parser.parse_args()
    clear_environ(lambda x: x.startswith(ENV_VAR_PREFIX))
    setproctitle('gunicorn')
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.abspath(args.settings_root))

    from CatalanNumber.CatalanProject.wsgi import application
    options = {
        'bind': args.socket,
        'workers': args.workers,
        'access-logfile': args.access_logfile,
        'timeout': args.timeout,
    }
    StandaloneApplication(application, options).run()


if __name__ == '__main__':
    main()