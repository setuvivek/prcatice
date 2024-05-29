/** @odoo-module **/

import { WebsiteSale } from "@website_sale/js/website_sale";
import { jsonrpc } from "@web/core/network/rpc_service";

WebsiteSale.include({

    init: function () {
            const def = this._super(...arguments);
            $('.product_id').change(function() {
                jsonrpc('/productgetqty', {
                'data':$(this).val(),
               }).then(function (result){
                        console.log(result)
                        $(".stock_loc").html(result.stock_loc)
                        $(".stock_val").html(result.qty)
                });
            })
        },

})


