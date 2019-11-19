var itemSet_Frequency = [];
var realItemSetFrequency = [];
var isSecond = 0;
var firstIndex;
var graph1Source = [];
var graph1Reference = {};
var queryTotal = [];
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
        debugger;
        var columnList = $('input[name=Columns]').val();
        if(columnList!=="")columnList=columnList.concat(",");
        columnList=columnList.concat(value);
        $('input[name=Columns]').val(columnList);
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
        pointRegionClick: function (args) {
         debugger;
         var requestedValue = graph1Source["Count"][args.data.region.Region.PointIndex].ItemSizeName.split("<br>");
         var RequestedKey =  graph1Source["ItemSizeName"].split("<br>");
         for( var j = 0; j < requestedValue.length; j++){
             if(graph1Reference.hasOwnProperty(RequestedKey[j])){
                if(!graph1Reference[RequestedKey[j]].includes(requestedValue[j]))graph1Reference[RequestedKey[j]].push(requestedValue[j]);
             }
             else{
                 graph1Reference[RequestedKey[j]] = Array(1);
                 graph1Reference[RequestedKey[j]][0] = (requestedValue[j]);
             }
         }
        },
        zooming: {enable: true},
        title: {
	           //Add chart title
               text: 'Frequent Support Item Set'
	        },
         series: [{
           marker: {
             dataLabel: {
                //Enable data label in the chart
                visible: true
             }
           },
          tooltip: {
               visible: true
           },
            selectionSettings: {
             // enable the selection settings
             mode: 'point',
             enable: true
          }
         }],
        primaryXAxis: {
            labelIntersectAction : 'trim',
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
    $( "#target" ).submit(function () {


        debugger;
        var $inputs = $('#target :input');
        var values = {};
        $inputs.each(function() {
            values[this.name] = $(this).val();
        });
        $.post("/apriori", values,  function (data, status) {
            debugger;
            data = JSON.parse(data);
            var dataItem = [];
            var primaryKey = 1;
            for (var freqNum in data){
                dataItem.push({"text" :`${freqNum} item set`,"primaryKey" : primaryKey.toString()});
                var primaryKeySecond = primaryKey +1;
                var freqSize = [];
                for(var itemName in data[freqNum] ){
                    var out = itemName.replace(/[{()}]/g, '').split(/'/).filter(x => x&&x!==", ").join("|");
                    dataItem.push({"text" :out,"primaryKey" : primaryKeySecond.toString(), "parentPrimaryKey":primaryKey.toString()});
                    var freqSizeItem = [];
                    var subFreqSizeItem = [];
                    for (var realItemName in  data[freqNum][itemName]){
                        var primaryKeyThird  = primaryKeySecond + 1;
                        var output = realItemName.replace(/[{()}]/g, '').split(/'/).filter(x => x&&x!==", ").join("|");
                        dataItem.push({"text": output, "parentPrimaryKey": primaryKeySecond.toString()})
                        subFreqSizeItem.push({"ItemSizeName": output.split("|").join("<br>").replace(/[{(')}]/g, ''), "Count":  data[freqNum][itemName][realItemName]})
                    }
                    freqSize.push({"ItemSizeName" : out.split("|").join("<br>").replace(/[{(')}]/g, ''), "Count" : subFreqSizeItem});
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


$(function () {
    $('#test').bind('click', function () {
debugger;
      $.post("/kmeans",  jsonObj,  function (data, status) {
          debugger;


      });
        return false;
    });
});