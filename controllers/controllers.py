# -*- coding: utf-8 -*-
# from odoo import http


# class CustomModule(http.Controller):
#     @http.route('/custom_module/custom_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_module/custom_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_module.listing', {
#             'root': '/custom_module/custom_module',
#             'objects': http.request.env['custom_module.custom_module'].search([]),
#         })

#     @http.route('/custom_module/custom_module/objects/<model("custom_module.custom_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_module.object', {
#             'object': obj
#         })

