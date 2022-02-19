from config import *
from startup.development import  development
from startup.production import production
from startup.test import test
from startup.stage import stage
from startup.init import init
from startup.defualt import default
from startup.sandbox import sandbox


def start():
    if startup_mode == 'development':
        development(config[startup_mode])

    elif startup_mode == 'production':
        production(config[startup_mode])

    elif startup_mode == 'test':
        test(config[startup_mode])

    elif startup_mode == 'stage':
        stage(config[startup_mode])

    elif startup_mode == 'init':
        init(config[startup_mode])

    elif startup_mode == 'sandbox':
        sandbox(config[startup_mode])

    else:
        default()


if __name__ == '__main__':
    start()
