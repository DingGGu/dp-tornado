# -*- coding: utf-8 -*-


from dp_tornado.engine.controller import Controller as dpController


class FooController(dpController):
    @dpController.route('^test/foo/(.*)/([0-9]+)/(.*)$')  # test/foo/a/1/c -> a/1/c
    def get(self, a, b, c):
        self.finish('%s/%s/%s' % (a, b, c))
