from odoo import http
from odoo.http import request, route
from odoo.addons.website_sale.controllers.main import WebsiteSale
from datetime import datetime, timedelta


class WebsiteSaleRFQ(WebsiteSale):

    @http.route(['/shop/confirm_order'], type='http', auth="public", website=True, sitemap=False)
    def confirm_order(self, **post):
        order = request.website.sale_get_order()

        if 'rfq_btn' in post:
            if order and order.order_line:
                request.env['approval.request'].sudo().create({
                    'request_owner_id' : request.env.user.id,
                    'category_id': request.env.ref('website_rfq.approval_category_website_items').id,
                    'type_request': post.get('type_request') if 'type_request' in post and post.get('type_request') else '',
                    'date_request': post.get('date_request') if 'date_request' in post and post.get('date_request') else datetime.now(),
                    'dis_request': post.get('dis_request') if 'dis_request' in post and post.get('dis_request') else '',
                    'project_id': post.get('project_id') if 'project_id' in post and post.get('project_id') else False,

                    'name': post.get('dis_request') if 'dis_request' in post and post.get('dis_request') else 'New',
                    'date_start': post.get('date_request') if 'date_request' in post and post.get('date_request') else datetime.now(),
                    'date_end': post.get('date_request') if 'date_request' in post and post.get('date_request') else datetime.now(),

                    'product_line_ids': [(0, 0, {
                        'product_id': line.product_id.id,
                        'quantity': line.product_uom_qty,
                    }) for line in order.order_line]
                })

                # Clear cart
                order.unlink()

        return request.redirect('/shop/cart')

