var a
$(document).ready(function(){
        $.getJSON('/start',
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
    scrollSettings: {
        allowScrolling: true,
        allowSheetOnDemand: true,
        width: "70%",
        isResponsive: false
    },
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

$(function () {
            $("#defaultListView").ejListView({ showHeader: true, showHeaderBackButton: true, headerTitle: "Check Frequent Item set",height:350, enableGroupList:true });
        });
function cellClick(args) {
    jQuery.addEventLog("Spreadsheet <span class='eventTitle'>cellClick</span> event called");
}

$(function () {
    $('a#test').bind('click', function () {

        $.get("/apriori", function (data, status) {
            debugger;
            var dataItem = []
            var primaryKey = 1
            for (var freqNum in data){
                dataItem.push({"text" : primaryKey.toString(),"primaryKey" : primaryKey.toString()})
                var primaryKeySecond = primaryKey +1;
                for(var itemName in data[freqNum] ){
                    dataItem.push({"text" :itemName,"primaryKey" : primaryKeySecond.toString(), "parentPrimaryKey":primaryKey.toString()});
                    var nameArray = data[freqNum][itemName]
                    for (var element in data[freqNum][itemName][nameArray])

                }
            }


                var dataSourceItem =
                [{ "Texts": "Discover Music", "PrimaryKeys": "1" },
                    { "Texts": "Hot Singles", "PrimaryKeys": "2","ParentPrimaryKeys": "1" },
                    { "Texts": "Rising Artists", "PrimaryKeys": null, "ParentPrimaryKeys": "3" },
                    { "Texts": "Live Music", "ParentPrimaryKeys": "1" },
                    { "Texts": "Best of 2013 So Far", "ParentPrimaryKeys": "1" },
                { "Texts": "Sales and Events", "PrimaryKeys": "2" },
                    { "Texts": "100 Albums - $5 Each", "ParentPrimaryKeys": "2" },
                    { "Texts": "Hip-Hop and R&amp;B Sale", "ParentPrimaryKeys": "2" },
                    { "Texts": "CD Deals", "ParentPrimaryKeys": "2" }];
               var musicFields = {
                "href": "Hrefs",
                "text": "Texts",
                "primaryKey": "PrimaryKeys",
                "parentPrimaryKey": "ParentPrimaryKeys"
                };
                $(function(){
                $("#defaultListView").ejListView({fieldSettings:musicFields,dataSource:dataSourceItem});
                });
                });
        return false;
    });
});