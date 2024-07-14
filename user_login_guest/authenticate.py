
from odoo.http import OpenERPSession
from odoo.http import request


def authenticate_without_passwd(self, db, login=None):
    """Authenticate the current user with the details in QR code.
    If successful, store the authentication parameters in the
    current session and request, unless multi-factor-authentication
    is activated. In that case, that last part will be done by
    :ref:`finalize`."""
    uid = request.env['res.users'].search([('login', '=', login)]).id
    self.pre_uid = uid
    self.rotate = True
    self.db = db
    self.login = login
    request.disable_db = False
    user = request.env(user=uid)['res.users'].browse(uid)
    if not user._mfa_url():
        self.finalize()
    return uid
OpenERPSession.authenticate_without_passwd = authenticate_without_passwd
