function initMap() {
  var Taiwan = { lat: 23.97565, lng: 120.973881944444 };
  // var highway_coor_lat = [24.251491000000001, 24.195640000000001, 23.159483999999999, 23.216488000000002, 23.159483999999999, 23.216488000000002, 24.251491000000001, 24.195640000000001, 23.569887999999999, 24.029285000000002, 24.195640000000001, 24.251491000000001, 24.023800000000001, 23.159483999999999, 23.216488000000002, 23.569887999999999, 24.035654999999998, 23.813020999999999,
  //   23.179205, 24.251491000000001, 24.195640000000001, 23.159483999999999, 23.216488000000002, 23.159483999999999, 23.216488000000002, 24.251491000000001, 24.195640000000001, 23.569887999999999, 24.029285000000002, 24.195640000000001, 24.251491000000001, 24.023800000000001, 23.159483999999999, 23.216488000000002, 23.569887999999999, 24.035654999999998, 23.813020999999999, 23.179205]
  // var highway_coor_lon = [121.16924299999999, 121.30365500000001, 120.75933700000002, 121.01954099999999, 120.75933700000002, 121.01954099999999, 121.16924299999999, 121.30365500000001, 120.89231200000002, 121.17594099999999, 121.30365500000001, 121.16924299999999, 121.18070700000001, 120.75933700000002, 121.01954099999999, 120.89231200000002, 121.185975, 120.850477, 120.78046999999999,
  //   121.16924299999999, 121.30365500000001, 120.75933700000002, 121.01954099999999, 120.75933700000002, 121.01954099999999, 121.16924299999999, 121.30365500000001, 120.89231200000002, 121.17594099999999, 121.30365500000001, 121.16924299999999, 121.18070700000001, 120.75933700000002, 121.01954099999999, 120.89231200000002, 121.185975, 120.850477, 120.78046999999999]
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
    center: Taiwan
  });
  var t = document.getElementById("table1");
  var k = 0;
  var check_name = [];
  var xhr = new XMLHttpRequest();
  xhr.open('GET', './data_hw1.json');
  xhr.onreadystatechange = function() {
    if(xhr.readyState === 4) {
      console.log(JSON.parse(xhr.responseText))
      var data_hw =  JSON.parse(xhr.responseText);
      data_hw.forEach(function(value,index) {
        var lat = value.lat;
        var lon = value.lon;
        var latlng = new google.maps.LatLng(lat,lon);
        var marker = new google.maps.Marker({
          position: latlng,
          map: map
        });
        var contentString = '<div>'+value.location+'</div><div>'+value.lat+'</div><div>' + value.lon + '<div>';
        var infowindow = new google.maps.InfoWindow({
          content: contentString
        });
        marker.addListener('mouseover', function() {
          infowindow.open(map, marker);
        });
        marker.addListener('mouseout', function() {
          infowindow.close();
        });
        if(check_name.includes(value.location) === false){
          if (k === 0){
            t.insertRow();
            for (var i=0;i<4;i++){
              t.rows[k].insertCell(i);
            }
            t.rows[k].cells[0].innerText = 'time';
            t.rows[k].cells[1].innerText = 'location';
            t.rows[k].cells[2].innerText = 'lat';
            t.rows[k].cells[3].innerText = 'lon';
            k++;
          }

          t.insertRow();
          for (var i=0;i<4;i++){
          t.rows[k].insertCell(i);
          }
          t.rows[k].cells[0].innerText = value.time;
          t.rows[k].cells[1].innerText = value.location;
          t.rows[k].cells[2].innerText = value.lat;
          t.rows[k].cells[3].innerText = value.lon;
          k++;
          check_name.push(value.location)
      };
      });
      }
    };
    xhr.send();


  }


// function test(){
//   // var pg = require("pg");
//   // var connectionString = "postgres://postgres:postgres123@localhost:5432/database1";
  
  
//   var myArray = [[1,2,3],[4,5,6],[7,8,9]]; 
//   var t = document.getElementById("table1"); 
//   for(var i=0;i<myArray.length;i++) { 
//      t.insertRow(); 
//      for(var j=0;j<myArray[i].length;j++) { 
//         t.rows[i].insertCell(j); 
//         t.rows[i].cells[j].innerText = myArray[i][j]; 
//      }    
//   } 
// }

