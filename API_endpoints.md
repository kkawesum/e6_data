# API Template

## Description

This is an api to perform CRUD operations on Blog posts

## Base URL

The base URL for all blog API requests is:

(http://127.0.0.1:8000/home-api/)

## Endpoints

### `GET /all`

Returns a paginated list of all blog posts(for un-authenticated users).


### Response

Returns a JSON object with the following properties:


    - `uid`: The unique identifier of the blog.
    - `title`: The title of the Blog.
    - `user`: The author of the Blog.
    - `blog_text`: A brief description of the Blog.
    
### Example

Request:

```
GET /all?page=2
```

Response:

```json
{
    "data": [
        {
            "uid": "995def2b-633e-4d11-9464-a400369e7f49",
            "title": "gfhggffg",
            "blog_text": "test  anotjher",
            "user": 1
        },
        {
            "uid": "e05cfd80-58e9-463e-985f-a20a0c9f05a3",
            "title": "hghjhj",
            "blog_text": "tezst3",
            "user": 3
        }
    ],
    "message": "blogs fetched successfully"
}
```

## HTTP status 

This API uses the following return codes:

- `400 Bad Request`: The request was malformed or missing required parameters.

- `200 Request OK`: The records were fetched successfully


### `GET /blog`

Returns a paginated list of all blog posts along with search functionality (intended onlyfor authorized users).


### Response

Returns a JSON object with the following properties:


    - `uid`: The unique identifier of the blog.
    - `title`: The title of the Blog.
    - `user`: The author of the Blog.
    - `blog_text`: A brief description of the Blog.
    
### Example

Request:

```
GET /blog
```

Response:

```json
{
    "data": [
        {
            "uid": "c66651fd-fe5b-4119-a23d-e0631003a4db",
            "title": "sample blog",
            "blog_text": "checking it out",
            "user": 2
        },
        {
            "uid": "3067728e-af40-494f-8451-6835f53c7037",
            "title": "sdsdadffs",
            "blog_text": "testig whether paginationnworks",
            "user": 2
        },
        {
            "uid": "c7494e8b-a580-4cf5-b05a-802000a06392",
            "title": "gfdhgjkj;kl'",
            "blog_text": "sadsghhjl;kl",
            "user": 2
        },
        {
            "uid": "e8a3080c-44ed-49cc-8b29-0124d1dde4a2",
            "title": "hjhkljkl;",
            "blog_text": ";lkn;k'nl;'k'n",
            "user": 2
        },
        {
            "uid": "d04e3b82-e08e-4df2-9d04-fa5340857b91",
            "title": "sample blog",
            "blog_text": "checking it out",
            "user": 2
        }
    ],
    "message": "blogs fetched successfully"
}
```

## HTTP status 

This API uses the following return codes:

- `400 Bad Request`: The request was malformed or missing required parameters.

- `200 Request OK`: The records were fetched successfully



### `POST /blog`

Creates a new Blog post after authenticating the user


### Response

Returns a JSON object with the following properties:


    - `uid`: The unique identifier of the blog.
    - `title`: The title of the Blog.
    - `user`: The author of the Blog.
    - `blog_text`: A brief description of the Blog.
    
### Example

Request:

```
POST /blog
```

Response:

```json
{
    "data": {
        "uid": "4389dd22-f096-4d78-aa77-71a42db19e65",
        "title": "sample blog",
        "blog_text": "checking it out",
        "user": 2
    },
    "message": "blog created successfully"
}
```

## HTTP status 

This API uses the following return codes:

- `400 Bad Request`: The request was malformed or missing required parameters.

- `201 Object created`: The records were created successfully


### `PATCH /blog`

Updates a Blog post after authenticating the user


### Response

Returns a JSON object with the following properties:


    - `uid`: The unique identifier of the blog.
    - `title`: The title of the Blog.
    - `user`: The author of the Blog.
    - `blog_text`: A brief description of the Blog.
    
### Example

Request:

```
PATCH /blog
```

Response:

```json
{
    "data": {
        "uid": "c66651fd-fe5b-4119-a23d-e0631003a4db",
        "title": "patchedtitle",
        "blog_text": "checking it out",
        "user": 2
    },
    "message": "blog updated successfully"
}
```

## HTTP status 

This API uses the following return codes:

- `400 Bad Request`: The request was malformed or missing required parameters.

- `201 Object updated`: The records were updated successfully


### `DELETE /blog`

Deletes a Blog post after authenticating the user


### Response

Returns a JSON object with the following properties:


    - `uid`: The unique identifier of the blog.
    - `title`: The title of the Blog.
    - `user`: The author of the Blog.
    - `blog_text`: A brief description of the Blog.
    
### Example

Request:

```
DELETE /blog
```

Response:

```json
{
    "data": {
        "uid": "c66651fd-fe5b-4119-a23d-e0631003a4db",
        "title": "patchedtitle",
        "blog_text": "checking it out",
        "user": 2
    },
    "message": "blog deleted successfully"
}
```

## HTTP status 

This API uses the following return codes:

- `400 Bad Request`: The request was malformed or missing required parameters.

- `200 OK`: The records were deleted successfully


## Authentication Handling (JWT Based)

The authentication is carried out via Django's inbuilt USER Model in conjunction with the simpleJWT module.

### Register Endpoint

http://localhost:8000/user-api/register/

It allows a new user to register to the web application.

The required parameters to be supplied with the request include:

1) Username: The username of the to be registered user
2) password: The password of the said user

Example: 

```
{   "firstname": "kk",
    "lastname": "shri",
    "username":"kk",
    "password":"7676"
}
```

### Login Endpoint

http://localhost:8000/user-api/login/

It allows a registered user to login to the system.


The required parameters to be supplied with the request include:

1) Username: The username of the to be registered user
2) password: The password of the said user


Example: 

```
{   
    "username":"kk",
    "password":"7676"
}
```
