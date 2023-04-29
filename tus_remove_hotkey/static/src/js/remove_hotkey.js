$(document).keydown(function(event){
    if(odoo.session_info && odoo.session_info.is_access_key && event.altKey){
        var elementWithAccessKey = [];
        elementWithAccessKey = document.documentElement.querySelectorAll('[accesskey]');
        _.each(elementWithAccessKey, function (elem) {elem.removeAttribute('accesskey');});

        var ariaElementWithAccessKey = [];
        ariaElementWithAccessKey = document.documentElement.querySelectorAll('[aria-keyshortcuts]');
        _.each(ariaElementWithAccessKey, function (elem) {elem.removeAttribute('aria-keyshortcuts');});

        var tattElementWithAccessKey = [];
        tattElementWithAccessKey = document.documentElement.querySelectorAll('[t-att-accesskey]');
        _.each(ariaElementWithAccessKey, function (elem) {elem.removeAttribute('t-att-accesskey');});

        var elementWithAccessKeyTooltip = [];
        elementWithAccessKeyTooltip = $(document).find('.o_web_accesskey_overlay');
        if (elementWithAccessKeyTooltip.length) {elementWithAccessKeyTooltip.remove();}
    }
});