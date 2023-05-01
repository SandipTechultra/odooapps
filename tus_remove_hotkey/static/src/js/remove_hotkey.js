odoo.define('tus_remove_hotkey.remove_hotkey', function (require) {
"use strict";

    var session = require('web.session');
    $(document).keydown(function(event){
        if(session && session.is_access_key && event.altKey){
            var elementWithAccessKey = [];
            elementWithAccessKey = document.documentElement.querySelectorAll('[accesskey]');
            _.each(elementWithAccessKey, function (elem) {elem.removeAttribute('accesskey');});

            var elementWithHotKey = [];
            elementWithHotKey = document.documentElement.querySelectorAll('[data-hotkey]');
            _.each(elementWithHotKey, function (elem) {elem.removeAttribute('data-hotkey');});

            var tattElementWithAccessKey = [];
            tattElementWithAccessKey = document.documentElement.querySelectorAll('[t-att-accesskey]');
            _.each(tattElementWithAccessKey, function (elem) {elem.removeAttribute('t-att-accesskey');});

            var elementWithAccessKeyTooltip = [];
            elementWithAccessKeyTooltip = $(document).find('.o_web_accesskey_overlay');
            if (elementWithAccessKeyTooltip.length) {elementWithAccessKeyTooltip.remove();}
        }
    });
});