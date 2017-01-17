//////////////////////////////////////////////////////////////////////////////
// Copyright 2015-2016 callidomus                          info@callidomus.com
// All Rights Reserved                             https://www.callidomus.com/
//////////////////////////////////////////////////////////////////////////////
cd.widgets.waermepumpe = {

    refresh: function (widgets) {
        //       widgets.each( function() {
        //           var widget = $(this);
        //       });
    },

    update: function (widget, item, val) {

        var items = widget.attr('data-item').split(' ');
        var status = items[0];
        var qvl = items[1];
        var qrl = items[2];
        var aussen = items[3];
        var wpvl = items[4];
        var wprl = items[5];

        svg1 = d3.select(widget[0]).select('svg.waermepumpeDetail');
        svg2 = d3.select(widget[0]).select('svg.waermepumpeDigest');

        if (item == status) {
            svg1.select('text.Status').text(val);
            svg2.select('text.Status').text(val);
            return;
        } else if (item == qvl) {
            svg1.select('text.QVL').text(val.toFixed(1) + '°C');
            svg2.select('text.QVL').text(val.toFixed(1) + '°C');
            return;
        } else if (item == qrl) {
            svg1.select('text.QRL').text(val.toFixed(1) + '°C');
            svg2.select('text.QRL').text(val.toFixed(1) + '°C');
            return;
        } else if (item == aussen) {
            svg1.select('text.Aussentemp').text(val.toFixed(1) + '°C');
            svg2.select('text.Aussentemp').text(val.toFixed(1) + '°C');
            return;
        } else if (item == wpvl) {
            svg1.select('text.WPVL').text(val.toFixed(1) + '°C');
            svg2.select('text.WPVL').text(val.toFixed(1) + '°C');
            return;
        } else if (item == wprl) {
            svg1.select('text.WPRL').text(val.toFixed(1) + '°C');
            svg2.select('text.WPRL').text(val.toFixed(1) + '°C');
            return;
        }

    }
}
