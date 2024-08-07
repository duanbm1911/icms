(function () {
    function n(a, c) {
        if (a.exportEnabled) {
            var b = document.createElement("div"), d = document.createTextNode("Save as CSV"); b.setAttribute("style", "padding: 12px 8px; background-color: " + a.toolbar.itemBackgroundColor + "; color: " + a.toolbar.fontColor); b.appendChild(d); b.addEventListener("mouseover", function () { b.setAttribute("style", "padding: 12px 8px; background-color: " + a.toolbar.itemBackgroundColorOnHover + "; color: " + a.toolbar.fontColorOnHover) }); b.addEventListener("mouseout", function () {
                b.setAttribute("style",
                    "padding: 12px 8px; background-color: " + a.toolbar.itemBackgroundColor + "; color: " + a.toolbar.fontColor)
            }); b.addEventListener("click", function () { var f = (c || "chart-data") + ".csv"; var e = "" + p({ data: a.options.data }); if (null != e) { f = f || "chart-data.csv"; e.match(/^data:text\/csv/i) || (e = "data:text/csv;charset=utf-8," + e); e = encodeURI(e); var g = document.createElement("a"); g.setAttribute("href", e); g.setAttribute("download", f); document.body.appendChild(g); g.click(); document.body.removeChild(g) } }); a._toolBar.lastChild.appendChild(b)
        }
    }
    function q(a) { for (var c = [], b = [], d = 0; d < a.length; d++)for (var f = 0; f < a[d].dataPoints.length; f++)c.push(k(a[d].dataPoints[f])); c.forEach(function (e) { var g = b.filter(function (l, m) { return l.x == e.x }); if (g.length) g = b.indexOf(g[0]), b[g].y = b[g].y.concat(e.y); else { if ("string" == typeof e.y || "number" == typeof e.y) e.y = [e.y]; b.push(e) } }); for (d = 0; d < b.length; d++) { for (f = 0; f < b[d].y.length; f++)b[d]["y" + f] = b[d].y[f]; delete b[d].y } return b } function p(a) {
        var c = "", b; var d = a.data || null; if (null == d || !d.length) return null; var f =
            a.columnDelimiter || ","; var e = a.lineDelimiter || "\n"; a = q(d); var g = Object.keys(a[0]); c = ""; c += g.join(f); c += e; a.forEach(function (l) { b = 0; g.forEach(function (m) { 0 < b && (c += f); c += l[m]; b++ }); c += e }); return c
    } function k(a) {
        if (null === a || "object" !== typeof a) return a; if (a instanceof Date) return new Date(a.getTime()); Array.isArray || (Array.isArray = function (d) { return "[object Array]" === Object.prototype.toString.call(d) }); if (Array.isArray(a)) { for (var c = [], b = 0; b < a.length; b++)c.push(k(a[b])); return c } c = new a.constructor;
        for (b in a) a.hasOwnProperty(b) && (c[b] = k(a[b])); return c
    } var h = window.CanvasJS || h ? window.CanvasJS : null; null == h && (h = require("@canvasjs/charts")); if (h) { h.Chart.prototype.exportAsCSV = function (a) { n(this, a) }; var r = h.Chart.prototype.render; h.Chart.prototype.render = function (a) { var c = r.apply(this, arguments); this.exportAsCSV(); return c } }
})();