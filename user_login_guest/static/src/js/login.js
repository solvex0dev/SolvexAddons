/** @odoo-module **/
    import rpc from 'web.rpc';
    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');
    publicWidget.registry.UserGuestLogin = publicWidget.Widget.extend({
    selector: '.login_as_guest',
        events: {
            'click #login_click': '_onLoginClick',
        },
       async _onLoginClick(ev) {
        try{
            ajax.jsonRpc('/web/login_as_guest', 'call', {'login_without_password': ""}).then((e)=>{window.location.href = '/';}) 
        }
        catch(Exeption){
            console.log("")
        }

        }
    })
