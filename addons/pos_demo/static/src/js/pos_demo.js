// esto sirve para mandar un mensaje a la consola del navegador
console.log('Point of Sale JavaScript loaded');
// esto define la personalizacion del odoo y variables constantes para el boton
odoo.define('pos_demo.custom',function(require){
    "use strict";
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');

//  Esto define el porcentaje de descuento que se aplicara en el set_discount(x)
    class PosDiscountButton extends PosComponent{
        async onClick(){
            const order = this.env.pos.get_order();
            if (order.selected_orderline){
                order.selected_orderline.set_discount(5);
            }
        }
    }

//  Para añadir el controlador al boton ademas de establecer la condicion
    PosDiscountButton.template = 'PosDiscountButton';
    ProductScreen.addControlButton({
        component: PosDiscountButton,
            condition: function(){
                return true;
            },
    });
    Registries.Component.add(PosDiscountButton);
    return PosDiscountButton;


// añadir un boton de ultimas 5 ventas
    class PosLastOrderButton extends PosComponent{
        async onClick() {
            var self = this;
            const order = this.env.pos.get_order();
            if (order.attributes.client) {
                var domain = [['partner_id', '=', order.attributes.client.id]];
                this.rpc({
                    model: 'pos.order', method: 'search_read',
                    args: [domain, ['name', 'amount_total']],
                    kwargs: { limit: 5 },
                    }).then(function (orders) {
                        if (orders.length > 0) {
                        var order_list = _.map(orders, function(o) {
                        return { 'label': _.str.sprintf("%s - TOTAL: %s", o.name, o.amount_total) };
                        });
                        self.showPopup('SelectionPopup', { title: 'Last 5 orders', list:order_list });
                        } else {
                            self.showPopup('ErrorPopup', { body: 'No previous orders found' });
                        }
                    });
            } else {
                self.showPopup('ErrorPopup', { body: 'Please select the customer' });
        }
    }
}

PosLastOrderButton.template = 'PosLastOrderButton';
ProductScreen.addControlButton({
    component: PosLastOrderButton,
    condition: function () {
    return true;
    },
});
Registries.Component.add(PosLastOrderButton);
return PosLastOrderButton;
}
);




