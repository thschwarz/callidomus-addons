//////////////////////////////////////////////////////////////////////////////
// Copyright 2015-2016 callidomus                          info@callidomus.com
// All Rights Reserved                             https://www.callidomus.com/
//////////////////////////////////////////////////////////////////////////////
cd.widgets.heizung = {

    refresh: function (widgets) {
        //       widgets.each( function() {
        //           var widget = $(this);
        //       });
    },

    update: function (widget, item, val) {

        var items = widget.attr('data-item').split(' ');
        var status = items[0];
        var fbh = items[1];
        var aussen = items[2];
        var innen = items[3];
        var h2o = items[4];

        svg1 = d3.select(widget[0]).select('svg.heizungDetail');
        svg2 = d3.select(widget[0]).select('svg.heizungDigest');

        if (item == status) {
            svg1.select('text.Status').text(val);
            svg2.select('text.Status').text(val);
            return;
        } else if (item == fbh) {
            svg1.select('text.Fussbodenheizung').text(val.toFixed(1) + '°C');
            svg2.select('text.Fussbodenheizung').text(val.toFixed(1) + '°C');
            return;
        } else if (item == aussen) {
            svg1.select('text.Aussentemperatur').text(val.toFixed(1) + '°C');
            svg2.select('text.Aussentemperatur').text(val.toFixed(1) + '°C');
            return;
        } else if (item == innen) {
            svg1.select('text.Innentemp').text(val.toFixed(1) + '°C');
            svg2.select('text.Innentemp').text(val.toFixed(1) + '°C');
            return;
        } else if (item == h2o) {
            svg1.select('text.Warmwasser').text(val.toFixed(1) + '°C');
            svg2.select('text.Warmwasser').text(val.toFixed(1) + '°C');
            return;
        }

    }
}
