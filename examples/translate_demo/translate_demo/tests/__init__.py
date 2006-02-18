import os, sys
import pkg_resources

pkg_resources.require('Paste')
pkg_resources.require('PasteScript')

from paste.deploy import loadapp
import paste.fixture
from unittest import TestCase

here_dir = os.path.dirname(__file__)
conf_dir = os.path.dirname(os.path.dirname(here_dir))
controller_dir = os.path.join(os.path.dirname(here_dir), 'controllers')

sys.path.insert(0, here_dir)

from translate_demo.config.routing import *
from pylons.myghtyroutes import RoutesResolver
from routes import request_config, url_for

class TestController(TestCase):
    def __init__(self, *args):
        wsgiapp = loadapp('config:development.ini', relative_to=conf_dir)
        self.app = paste.fixture.TestApp(wsgiapp)
        TestCase.__init__(self, *args)

__all__ = ['url_for', 'TestController']
