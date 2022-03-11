# -*- coding: utf-8 -*-
# from odoo import http


# class SaleQuotation(http.Controller):
#     @http.route('/sale_quotation/sale_quotation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_quotation/sale_quotation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_quotation.listing', {
#             'root': '/sale_quotation/sale_quotation',
#             'objects': http.request.env['sale_quotation.sale_quotation'].search([]),
#         })

#     @http.route('/sale_quotation/sale_quotation/objects/<model("sale_quotation.sale_quotation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_quotation.object', {
#             'object': obj
#         })
