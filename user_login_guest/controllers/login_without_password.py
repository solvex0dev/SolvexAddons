
from odoo import http
from odoo.http import Controller, request
import logging
from odoo.exceptions import ValidationError

class LoginController(Controller):

    @http.route(['/web/login_as_guest'], type='json', auth='none', website=True,
                csrf=False, csrf_token=None)
    def login_without_password(self):
        config = request.env['config.login.guest'].sudo().search([],limit=1)
        if config and str(config.database) == request.session.db and config.user_id:
            username=str(config.user_id.login)
            database=str(config.database)
            logging.warning(config.database)
            logging.warning(config.user_id.login)
            request.session.authenticate_without_passwd(database, username)
            return request.redirect('/')
        else :
       
            return {} 

