// var a = [{"value": "foo", "key": [1, 2]}];
$(document).ready(function(){
        $.getJSON('/apriori',
            function (data) {
                //do nothing
                var excelObj = $("#Spreadsheet").data("ejSpreadsheet");
                var array =Object.values(data);
                var settings = { dataSource: array, showHeader: "true", startCell: "A1" };
                excelObj.updateRange(1, settings);
                excelObj.XLResize.fitWidth([...Array(15).keys()].map(x => x++))
            });

        return false;
    });
$("#Spreadsheet").ejSpreadsheet({
    // ...
    // sheets: [{
    //     dataSource: a,
    //     // query: ej.Query().take(50).select(["OrderID", "CustomerID", "EmployeeID", "ShipName", "ShipAddress"]),
    //     // primaryKey: "OrderID"
    // }],
    scrollSettings: {
        allowScrolling: true,
        height: 600,
        width: 1200
    },
    loadComplete: "loadComplete",
    cellClick: function (args) {
        var rowIndex = args.rowIndex;
        var colIndex = args.columnIndex;
        var value = args.value; // if we want to know the clicked cell rowIndex and columnIndex and value
        console.log(rowIndex);
        console.log(colIndex);
        console.log(value)
    },
    showRibbon: false
    // ...
});

function loadComplete() {
    this.XLCFormat.setCFRule({action: "greaterthan", inputs: ["10"], color: "redft", range: "D2:D8"});
}

function cellClick(args) {
    jQuery.addEventLog("Spreadsheet <span class='eventTitle'>cellClick</span> event called");
}

$(function () {
    $('a#test').bind('click', function () {
        $.getJSON('/apriori',
            function (data) {
                //do nothing

                var excelObj = $("#Spreadsheet").data("ejSpreadsheet");
                var array =Object.values(data);
                var settings = { dataSource: array, showHeader: "true", startCell: "A1" };
                excelObj.updateRange(1, settings);
                excelObj.XLResize.fitWidth([...Array(15).keys()].map(x => x++))
            });

        return false;
    });
});