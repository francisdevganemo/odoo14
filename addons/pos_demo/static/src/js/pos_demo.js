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
            component: PosDiscountButton,
            condition: function(){
                return true;
            },
    });
    Registries.Component.add(PosDiscountButton);
    return PosDiscountButton;
})