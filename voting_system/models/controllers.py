# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):

    @http.route('/voting/user/', auth='public')
    def index(self, **kw):
        return "Hello, world"