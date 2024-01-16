window.onload = init;
function init() {
    //Map id from html template

    const mapElement = document.getElementById('mapid');
    //map screen type
    const openStreetMap =  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC',
        maxZoom: 22
    })
    //map screen type 2
    const stadiaLightMap =  L.tileLayer('https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png', {
        maxZoom: 22,
        attribution: 'Map <a href="https://memomaps.de/">memomaps.de</a> <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })

    // creating map element 
    const mymap = L.map(mapElement, {
        center: [22, 80],
        zoom: 3,
        minZoom: 1,
        layers: [ stadiaLightMap ]
    })


    //Overlays
    // const perthBaseMapImage = "../static/myimg.jpg";
    // const perthBaseMapBounds = [[10.231,12.34534],[57.56756,34.45645]]
    // const imagePerthOverlay= L.imageOverlay(perthBaseMapImagey)

    
    //Putting Mark or Point on Map
    var lat = [28.47706612131494, 28.45027944330871, 28.507013881018153, 28.43578917275445, 28.499181734215937,28.362401735238237, 30.12612436422458,27.965296099717275, 27.85850514051748,29.859701442126756]

    var long = [77.50985384085652, 77.48073577880861, 77.4086380004883, 77.50339508056642, 77.468389489533397,75.54199218750001, 77.47558593750001, 79.12353515625001, 76.92626953125001, 76.09130859375001]

    var mark = 0;
    const Marker1 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp1 = Marker1.bindPopup('<b>Jeeva Parking : Alpha 1</b>')

    const Marker2 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp2 = Marker2.bindPopup('<b>Shushme Parking : Noida Sector - 148</b>')

    const Marker3 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp3 = Marker3.bindPopup('<b>Quartz Parking : Noida Sector - 137</b>')

    const Marker4 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp4 = Marker4.bindPopup('<b>Marx Parking : Noida</b>')

    const Marker5 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp5 = Marker5.bindPopup('<b>Moustiqueinz Parking : Alpha 1</b>')

    const Marker6 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp6 = Marker6.bindPopup('<b>Shivam Parking House : Pilani</b>')


    const Marker7 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp7 = Marker7.bindPopup('<b>Narendra Parking Hub : YamunaNagar</b>')

    const Marker8 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp8 = Marker8.bindPopup('<b>Krishn Space : Budau</b>')


    const Marker9 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp9 = Marker9.bindPopup('<b>Vaikunth Parking Sthaan : Neemli</b>')

    const Marker10 = L.marker([lat[mark], long[mark]], {
        title : mark,
        opacity : 1
    }).addTo(mymap)
    mark++;
    //MarkerPopUp
    const markerPopUp10 = Marker10.bindPopup('<b>SwargDhaam Parking : JogeWala</b>')
    
    // MY ICON SYSTEM for your current location

    const myIcon = L.icon({
        iconUrl: '../templates/logo_icon.png', // you can also use DIVICON*
        iconSize: [40, 40],
        iconAnchor: [20, 40],
        popupAnchor: [-3, -76],
    });

    // L.marker([50.505, 30.57], {icon: myIcon}).addTo(map);


    //GeoLocation API
    mymap.locate({setView:true, maxZoom: 14})

    function onLocationnFound(e){
        var radius = e.accuracy.toFixed(2);
        var locationMarker = L.marker(e.latlng, {icon: myIcon}).addTo(mymap).bindPopup("You're here")

        var locationCircle = L.circle(e.latlng, radius).addTo(mymap)
    }
    mymap.on('locationfound', onLocationnFound);

    function onLocationError(e){
        window.alert(e.message);
    }
    mymap.on('locationerror', onLocationError)

    //baselayers to choose ( whether the openstreetmap or stadiaMap )
    const baseLayers = {
        '<b>openStreetMap</b>' : openStreetMap,
        '<b>stadiaLightMap</b>' : stadiaLightMap
    }
    //putting control layers
    const layersControls = L.control.layers(baseLayers,{},{}).addTo(mymap)


    /*
    //POLYLINE
    var latlngs = [
        [28.51, 77.68],
        [28.77, 78.43],
        [29.04, 79.2]
    ];
    var polyline = L.polyline(latlngs, { color : 'red'}).addTo(mymap);
    mymap.fitBounds(polyline.getBounds());
    //POLYLINE DYNAMICALLY -> just by clicking on the screen
    var linesCoordinates = [];
    var drawPolyline = L.polyline([], {color: 'black'}).addTo(mymap);

    mymap.on('click', function(e){
        let latlng = e.latlng;
        linesCoordinates.push(latlng)

        if(linesCoordinates.length > 1){
            drawPolyline.setLatLngs(linesCoordinates);
        }
    })

    */

    //Distance finding using markers
    /*
    var counter = 0;
    var coordinates = []

    mymap.on('click', function(e){
        counter += 1;
        let latlng = e.latlng;
        coordinates.push(latlng);

        let popup = L.popup({
            autoClose : false,
            closeOnClick : false
        }).setContent(String(counter))

        L.marker(latlng).addTo(mymap).bindPopup(popup).openPopup()

        if( counter >= 2){
            let distance = mymap.distance(coordinates[0], coordinates[1])
            console.log(distance)
            coordinates.shift()
        }
    })
    */
    // const distance = (mymap.distance([lat[mark-2], long[mark-2]],[lat[mark-1], long[mark-1]]))/1000 + "KiloMeters"
    // console.log(distance)
    
   
}


/*

*/