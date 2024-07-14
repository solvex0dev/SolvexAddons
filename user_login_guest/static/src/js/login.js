/** @odoo-module */
import publicWidget from "@web/legacy/js/public/public_widget";
import {login} from "@web/legacy/js/public/signin";
import { _t } from "@web/core/l10n/translation";
import { jsonrpc } from "@web/core/network/rpc_service";

 publicWidget.registry.login.include({
     events: Object.assign({}, publicWidget.Widget.prototype.events, {
            'click #login_click': '_onLoginClick',
            
        }),
        
       async _onLoginClick(ev) {
       
            jsonrpc('/web/login_as_guest',{
            'login_without_password':""}
            ).then((e) => {
                window.location.href = '/';
         
            
        });
       
         
        }

    })



