# NETFLIX_content_service
NETFLIX content API for ASEE signature

## ENTITY CLASSES
### Film class
- titolo : string
- filmId : Int
- release : Date
- duration: Int
- actors_inside : array Actor
- genre: String
- rating: Int
### Actor class
- actorID: Int
- name : String
- surname : String
- dateOfBirthday : Date
- filmRecite : array Film

## API NOTES
Spring Boot Server
### Content service
- /films/
    - GET
    - POST
- /films/{id}
    - GET
    - PUT
    - DELETE
- /actors
    - GET
    - POST
- /actors/{actorId}
    - GET
    - PUT
    - DELETE
- /actors/{actorId}/films
    - GET

## Overview

