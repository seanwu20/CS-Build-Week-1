# Endpoints
___

### Register
Post Request:`api/register/`

```
Request: 
{
    "username":"testing", 
    "email":"testing@testing.com", 
    "password1":"testingtesting", 
    "password2":"testingtesting" 
}

Response
{
    "key": "82682e95a3c23ab8ea88c891c3399b106143cd7e"
}
```


### Login

Post Request: `api/login/`

```
Request: 
{
    "username":"testing", 
    "email":"testing@testing.com", 
    "password":"testingtesting" 
}


Response
{
    "key": "4a4caa0f1252583d1009809ad124cc9e6551b4fe",
}
```

### Logout
Post Request: `api/logout/`

```
Request: {}


Response
{
    "detail": "Successfully logged out."
}
```

### User Info
Post Request: `api/userinfo/`

```
Authorization header: Token ${token}

Request: 
{
    "id":1
}


Response
{
    "detail": "Successfully logged out."
}
```


### JSON Representation of map

Get Request: `api/map/`


```
Authorization header: Bearer token

Request: {}


Response
{
    "name": "Miami",
    "attributes": {
        "state": "Florida"
    },
    "children": [
        {
            "name": "Jacksonville",
            "attributes": {
                "state": "Florida"
            },
            "children": [
                {

etc etc
```


### Change User info

Get, put, post, delete request: `api/userinfo/`

Please see Django Rest Framework model serializers and routers for more info

### Change cities and update user food and water 

Put Request: `api/move/`

```
Authorization header: Bearer token

Request: 
{
    "user_id": 1,
    "user_food": 10,
    "user_water": 12,
    "state": "Florida",
    "new_city": "Jacksonville"
}


Response
{
    "user_id_id": 1,
    "user_food": 10,
    "user_water": 12,
    "state": "Florida",
    "city": "Jacksonville",
    "location": "fast_food",
    "food_available": 9,
    "water_available": 2,
    "location_2": "hotel",
    "food_available_2": 6,
    "water_available_2": 3,
    "left": "Macon",
    "right": null,
    "previous": "Miami"
}
```
