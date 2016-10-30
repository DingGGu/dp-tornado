# -*- coding: utf-8 -*-


import os

from dp_tornado import Bootstrap


kwargs = {
    'application_path': os.path.join(os.path.dirname(os.path.realpath(__file__))),
}

bootstrap = Bootstrap()
bootstrap.run(**kwargs)