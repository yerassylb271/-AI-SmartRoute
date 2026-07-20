import requests


HEADERS = {
    "User-Agent": "AI-SmartRoute/1.0"
}



# ===============================
# GEOCODING
# ===============================

def geocode(place):

    # Coordinates input
    try:

        lat, lon = map(
            float,
            place.split(",")
        )

        return lat, lon

    except:
        pass



    url = "https://nominatim.openstreetmap.org/search"


    params = {

        "q": place,

        "format": "json",

        "limit": 1

    }


    response = requests.get(
        url,
        params=params,
        headers=HEADERS
    )


    data = response.json()



    if not data:

        return None



    return (

        float(data[0]["lat"]),

        float(data[0]["lon"])

    )







# ===============================
# ROUTING
# ===============================

def get_route(start, end, profile):


    url = (

        "https://router.project-osrm.org/route/v1/"

        f"{profile}/"

        f"{start[1]},{start[0]};"

        f"{end[1]},{end[0]}"

        "?overview=full&geometries=geojson"

    )



    response = requests.get(url)



    if response.status_code != 200:

        return None



    data = response.json()



    if "routes" not in data:

        return None



    if len(data["routes"]) == 0:

        return None



    return data["routes"][0]








# ===============================
# SCORE
# ===============================

def calculate_score(
        time,
        price,
        co2
):


    score = 10



    # time

    score -= min(
        time / 30,
        3
    )



    # price

    score -= min(
        price / 500,
        2
    )



    # pollution

    score -= min(
        co2,
        2
    )



    return round(
        max(score,5),
        1
    )








def stars(score):


    if score >= 9:

        return "★★★★★"


    elif score >= 8:

        return "★★★★☆"


    elif score >= 7:

        return "★★★☆☆"


    elif score >= 6:

        return "★★☆☆☆"


    else:

        return "★☆☆☆☆"








# ===============================
# BUILD ROUTE
# ===============================

def build_route(

        profile,

        category,

        name,

        price_km,

        co2_km,

        start,

        end

):


    route = get_route(
        start,
        end,
        profile
    )



    if not route:

        return None



    distance = (
        route["distance"]
        /
        1000
    )



    time = (
        route["duration"]
        /
        60
    )



    price = round(
        distance * price_km
    )



    co2 = round(
        distance * co2_km,
        2
    )



    score = calculate_score(

        time,

        price,

        co2

    )



    return {


        "category":category,


        "name":name,


        "profile":profile,


        "distance":
        round(distance,2),



        "time":
        round(time),



        "price":
        price,



        "co2":
        co2,



        "score":
        score,



        "stars":
        stars(score),



        "recommended":
        False,



        "eco":
        False,



        "geometry":
        route["geometry"]


    }









# ===============================
# MAIN FUNCTION
# ===============================

def get_routes(
        start_name,
        destination_name
):


    start = geocode(start_name)


    end = geocode(destination_name)



    if not start or not end:

        return []



    routes = []



    # CAR

    car = build_route(

        "driving",

        "⚡ Fastest",

        "🚗 Car",

        35,

        0.18,

        start,

        end

    )



    # BIKE

    bicycle = build_route(

        "cycling",

        "💰 Cheapest",

        "🚴 Bicycle",

        0,

        0,

        start,

        end

    )



    # WALK

    walking = build_route(

        "walking",

        "🌱 Eco",

        "🚶 Walking",

        0,

        0,

        start,

        end

    )





    if car:

        routes.append(car)



    if bicycle:

        routes.append(bicycle)



    if walking:

        routes.append(walking)







    if not routes:

        return []







    # ===============================
    # AI RECOMMENDATION
    # ===============================


    routes.sort(

        key=lambda x:x["score"],

        reverse=True

    )


    routes[0]["recommended"] = True







    # ===============================
    # ECO BADGE
    # ===============================


    eco_route = min(

        routes,

        key=lambda x:x["co2"]

    )



    eco_route["eco"] = True







    # Sort back

    return routes