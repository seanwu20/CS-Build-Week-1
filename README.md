# Endpoints

### JSON Representation of map
https://we-cant-name-things.herokuapp.com/api/map/

### Play with play data:
Link: https://we-cant-name-things.herokuapp.com/api/players
Auto generated from Django Rest Framework. Creates an UI to mess around with player data
___


### POST: Player info
Link: https://we-cant-name-things.herokuapp.com/api/player

Send body: `{"email":"some@email.com"}`

Recieve:
```
{
    "id": 1,   
    "email": "seanwu20@gmail.com",
    "food": 12, //how much supplies user has
    "water": 32,
    "state": "Florida", //user current city and state
    "city": "Miami",
    "location": "hotel", //room 1 with amount of supplies
    "food_available": 4,
    "water_available": 4,
    "location_2": "bank", //room 2 with amount of supplies
    "food_available_2": 3,
    "water_available_2": 9,
    "left": "Jacksonville", // city to the left and right (forward direction)
    "right": "Tallahassee", 
    "previous": null //the city the user just came from
}
```
___


### PUT: Move city
Link: https://we-cant-name-things.herokuapp.com/api/move

Send body:
```
{
    "email": "seanwu20@gmail.com",
    "food":12, //updated food user has
    "water":32, //updated water user has
    "new_city":"Atlanta" //city that user travelled to
}
```
Recieve 
```
{
    "id": 1,
    "email": "seanwu20@gmail.com",
    "food": 12,
    "water": 32,
    "state": "Georgia",
    "city": "Atlanta",
    "location": "store",
    "food_available": 3,
    "water_available": 6,
    "location_2": "fast_food",
    "food_available_2": 9,
    "water_available_2": 4,
    "left": "Chattanooga",
    "right": null,
    "previous": "Macon"
}
```

