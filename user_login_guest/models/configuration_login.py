# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from math import ceil
import logging as log

class ConfigLogin(models.Model):
    _name = 'config.login.guest'
    _rec_name='database'

    user_id = fields.Many2one(
        'res.users',
        string='User',
        domain=lambda x: x.compute_domain_users()  
        )
    database= fields.Char(
       
        string='Database',
        default=lambda self: self.env.cr.dbname,   
        ondelete="cascade" 
        )
    
    def action_disable(self):
        self.user_id=False
    
    def compute_domain_users(self):
        list_ids=[]
        users=self.env['res.users'].sudo().search([])
        for user in users :
            if user.has_group('base.group_user') :
                list_ids.append(user.id)
        return f"[('id','in',{list_ids})]"