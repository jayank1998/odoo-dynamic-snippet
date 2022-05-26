odoo.define('dynamic_snippet.snippet_customer', ['web.ajax'], function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function () {
    var container = document.getElementById("snippet_customer_container");
    if (container) {
        container.innerHTML = "";
        container.innerHTML = "<div class='col text-center'><div class='lds-dual-ring'></div></div>";
        ajax.jsonRpc('/get_jobs','call', {}).then(function(data) {
            console.log(data,'MILE DATA')
            container.innerHTML = "";
            for (var i = 0; i < data.length; i++) {
                container.innerHTML += '<div class="col-md-3">'
                + '<div style="height:15mm;"><h5><center>' + data[i].name + '</center></h5></div>'
                + '<div class="col-4 col-sm-4 col-lg-2"><center>
                                            <img src="/web/image/hr.job/'+data[i].id+'/image_medium" />
                                        </center></div>'
                + '<div><h5>' + data[i].department + '</h5></div>'
                + '<div style="height:4cm; text-overflow: ellipsis;
                                    -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: scroll;
                                    display: -webkit-box;"><p>' + data[i].description + '</p></div>'
                + '</div>';
            }
        });
    }
    });

});
