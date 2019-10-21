var itemSet_Frequency = []
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
            $("#defaultListView").ejListView({
                showHeader: true,
                showHeaderBackButton: true,
                headerTitle: "Check Frequent Item set",
                height:400,
                enableGroupList:true,

            });
        });
function cellClick(args) {
    jQuery.addEventLog("Spreadsheet <span class='eventTitle'>cellClick</span> event called");
}
$(function () {
    $("#container1").ejChart({
        title: {
	           //Add chart title
               text: 'Frequent Support Item Set'
	        },
         series: [{
           marker: {
             dataLabel: {
                //Enable data label in the chart
                visible: true
           } }
         }],
        primaryXAxis: {
                font : {
                        fontFamily : 'Segoe UI',
                        size : '10px',
                },
            }
    });
    $("#container2").ejChart({
        title: {
	           //Add chart title
               text: 'Frequent Support Item Set'
	        },
         series: [{
           marker: {
             dataLabel: {
                //Enable data label in the chart
                visible: true
           } }
         }],
        primaryXAxis: {
                font : {
                        fontFamily : 'Segoe UI',
                        size : '10px',
                },
            }
    });
});

//update to listview with aporir
$(function () {
    $('a#test').bind('click', function () {

        $.get("/apriori", function (data, status) {
            var dataItem = []
            var primaryKey = 1
            for (var freqNum in data){
                dataItem.push({"text" :`${freqNum} item set`,"primaryKey" : primaryKey.toString()})
                var primaryKeySecond = primaryKey +1;
                var freqSize = [];
                for(var itemName in data[freqNum] ){
                    dataItem.push({"text" :itemName,"primaryKey" : primaryKeySecond.toString(), "parentPrimaryKey":primaryKey.toString()});
                    freqSize.push({"ItemSizeName" : itemName.replace(/,/g,"<br>").replace(/[{(')}]/g, ''), "Count" : data[freqNum][itemName].length});
                    for (var i = 0; i < data[freqNum][itemName].length; i++){
                        dataItem.push({"text": data[freqNum][itemName][i], "parentPrimaryKey": primaryKeySecond.toString()})
                    }
                    primaryKeySecond ++;
                }
                itemSet_Frequency.push(freqSize);
                primaryKey = primaryKeySecond;
            }

            $(function(){
                $("#defaultListView").ejListView({dataSource:dataItem});
            });


            });
        return false;
    });
});