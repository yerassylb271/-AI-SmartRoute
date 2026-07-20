// ===============================
// AI SmartRoute
// ===============================


// MAP

const map = L.map("map").setView(
    [43.238949, 76.889709],
    13
);


L.tileLayer(
    "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        maxZoom:19,
        attribution:"&copy; OpenStreetMap"
    }
).addTo(map);



// VARIABLES

let startMarker = null;

let destinationMarker = null;

let routeLayer = null;

let clickCount = 0;

let currentRoutes = [];




// MAP CLICK

map.on("click", function(e){


    const lat =
    e.latlng.lat.toFixed(6);


    const lon =
    e.latlng.lng.toFixed(6);



    if(clickCount === 0){


        if(startMarker)
            map.removeLayer(startMarker);



        startMarker =
        L.marker(e.latlng)
        .addTo(map);



        document
        .getElementById("start")
        .value =
        lat + "," + lon;



        clickCount = 1;


    }

    else{


        if(destinationMarker)
            map.removeLayer(destinationMarker);



        destinationMarker =
        L.marker(e.latlng)
        .addTo(map);



        document
        .getElementById("destination")
        .value =
        lat + "," + lon;



        clickCount = 0;


    }


});







// BUILD ROUTE


async function buildRoute(){


    const start =
    document.getElementById("start")
    .value.trim();



    const destination =
    document.getElementById("destination")
    .value.trim();



    if(!start || !destination){

        alert(
            "Enter start and destination"
        );

        return;

    }



    const response =
    await fetch(
        "/build-route",
        {

        method:"POST",

        headers:{
            "Content-Type":
            "application/json"
        },


        body:JSON.stringify({

            start:start,

            destination:destination

        })


        }
    );



    const data =
    await response.json();



    if(!data.success){

        alert(data.error);

        return;

    }



    currentRoutes =
    data.routes;



    showWeather(
        data.weather
    );


    showAI(
        data.ai
    );


    showRoutes(
        data.routes
    );


    drawRoute(
        data.routes[0]
    );


}








// DRAW ROUTE


function drawRoute(route){


    if(!route)
        return;



    if(routeLayer)

        map.removeLayer(
            routeLayer
        );



    if(
        !route.geometry ||
        !route.geometry.coordinates
    )
        return;



    const coordinates =
    route.geometry.coordinates.map(
        point => [

            point[1],

            point[0]

        ]
    );



    routeLayer =
    L.polyline(

        coordinates,

        {

        color:"#2563eb",

        weight:6

        }

    )
    .addTo(map);



    map.fitBounds(
        routeLayer.getBounds()
    );


}








// WEATHER


function showWeather(weather){

    document
    .getElementById("weather")
    .innerHTML = `

    <p>
    Temperature: <b>${weather.temperature} °C</b>
    </p>

    <p>
    Condition: ${weather.condition}
    </p>

    <p>
    Wind: ${weather.wind} m/s
    </p>

    `;

}








// AI


function showAI(ai){


    let text = ai;



    if(typeof ai === "object"){

        text =
        ai.message ||
        JSON.stringify(ai);

    }



    document
    .getElementById("ai")
    .innerHTML =
    text.replace(
        /\n/g,
        "<br>"
    );


}








// ROUTE CARDS WITH HIGHLIGHT


function showRoutes(routes){


    let html = "";



    routes.forEach(
    (route,index)=>{


        let classes =
        "route-card";



        let badge = "";


// AI RECOMMENDED

if(route.recommended){

    classes += " ai-recommended";

    badge += `

    <div class="ai-badge">
        – AI Recommends
    </div>

    `;

}



// ECO FRIENDLY

if(route.eco){

    classes += " eco-recommended";

    badge += `

    <div class="eco-badge">

        <img src="/static/images/eco-badge.png">

    </div>

    `;

}
        // AI GLOW

        if(route.recommended){


            classes +=
            " ai-recommended";


            badge = `

            <div class="ai-badge">
            ðŸ¤– AI Recommends
            </div>

            `;


        }



        // ECO GLOW

        if(route.eco){


            classes +=
            " eco-recommended";


            badge = `

            <div class="eco-badge">
            <img src="/static/images/eco-badge.png">
            </div>

            `;


        }




        html += `


        <div class="${classes}"

        onclick="selectRoute(${index})">


        ${badge}



        <h3>
        ${route.tag || ""}
        </h3>


        <p>
TIME: ${route.time} min
</p>

<p>
DISTANCE: ${route.distance} km
</p>

<p>
PRICE: ${route.price} KZT
</p>

<p>
CO2: ${route.co2} kg
</p>

<p>
SCORE: ${route.score}/10
</p>


        </div>


        `;


    });



    document
    .getElementById("routes")
    .innerHTML = html;


}








// SELECT ROUTE


function selectRoute(index){


    drawRoute(
        currentRoutes[index]
    );


}
