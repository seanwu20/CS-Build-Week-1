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
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InRlc3RpbmciLCJleHAiOjE1ODIyMjc4ODUsImVtYWlsIjoidGVzdGluZ0B0ZXN0aW5nLmNvbSJ9.TKXMP2oVXiblsFptYj9RDzyjGgVI_HF5aOvl1_LOV0k",
    "user": {
        "pk": 2,
        "username": "testing",
        "email": "testing@testing.com",
        "first_name": "",
        "last_name": ""
    }
}
```

### Get Tokens

Post Request: `api/token/`

```
Request: 
{
    "username": "testing",
    "email": "testing@gmail.com",
    "password":"testingtesting"
}

Response
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4MjMxNDQ4MywianRpIjoiMzgwZDJkM2UzNGY5NGNiOTgzZTE1ZDc4ZjMxZTYyOTYiLCJ1c2VyX2lkIjoyfQ.xMAxZF_m2ZTGL_878Af_tEm2gzUVlZFJyd_0omS1lWA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgyMjI4MzgzLCJqdGkiOiIyNTM4ZmUwMTIwYzU0ZmE2YTczMzM5MWY3NGVkY2QxYiIsInVzZXJfaWQiOjJ9.GksutPjkxZQo3CtYyFAUVt3h7PPtQKGW4_cg37U5YyU"
}
```


### Refresh token

Post Request: `api/token/refresh`

```
Request: 
{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4MjMxNDk4MSwianRpIjoiZTlmNWNjOThmNDU0NGE3YTllMjYyNThmOTNiODQ2YjciLCJ1c2VyX2lkIjoyfQ.dGJ0CgT66nfBxHvJFZFqVBIEW5FAoLOSOahCH9nTB04"}

Response
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgyMjI4ODk1LCJqdGkiOiI1YjQ3ZjVkMTJjOWE0MzViOTVmOGFjZGUyZDc4ZDc0MyIsInVzZXJfaWQiOjJ9._KFX2D2wCoGSTap7ZyzI0HzT5GvvSizaRpOsJqmzt_g"
}
```



### Login

Post Request: `api/login/`

```
Authorization header: Bearer token

Request: 
{
    "username":"testing", 
    "email":"testing@testing.com", 
    "password":"testingtesting" 
}


Response
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InRlc3RpbmciLCJleHAiOjE1ODIyMjg1NTgsImVtYWlsIjoidGVzdGluZ0B0ZXN0aW5nLmNvbSJ9.No9p4NDEUgSiLi0DdARXPa-1GcVOCnkFOAvJEPDR7-w",
    "user": {
        "pk": 2,
        "username": "testing",
        "email": "testing@testing.com",
        "first_name": "",
        "last_name": ""
    }
}
```

### Logout
Post Request: `api/logout/`

```
Authorization header: Bearer token

Request: {}


Response
{
    "detail": "Successfully logged out."
}
```

### User Info
Post Request: `api/userinfo`

```
Authorization header: Bearer token

Request: {}


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

```

```
