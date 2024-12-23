import connexion
import six

from app.models.actor import Actor  # noqa: E501
from app.models.film import Film  # noqa: E501
from app import util


def actors_actor_id_delete(actor_id):  # noqa: E501
    """Remove a specific Actor.

     # noqa: E501

    :param actor_id: Actor&#x27;s ID
    :type actor_id: int

    :rtype: None
    """
    return 'do some magic!'


def create_actor(body):  # noqa: E501
    """Add a new actor

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Actor
    """
    if connexion.request.is_json:
        body = Actor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def films_get():  # noqa: E501
    """Return a list of all available films.

     # noqa: E501


    :rtype: List[Film]
    """
    return 'do some magic!'


def films_id_delete(id):  # noqa: E501
    """Remove a specific film.

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def films_id_get(id):  # noqa: E501
    """Return information about specific film.

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Film
    """
    return 'do some magic!'


def films_id_put(body, id):  # noqa: E501
    """Update information about specific film

     # noqa: E501

    :param body: new details of film
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Film.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def films_post(body):  # noqa: E501
    """Add a new film (work with singol film)

     # noqa: E501

    :param body: add film details
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Film.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_actor_by_id(actor_id):  # noqa: E501
    """gets a specific actor

     # noqa: E501

    :param actor_id: Actor&#x27;s ID
    :type actor_id: int

    :rtype: Actor
    """
    return 'do some magic!'


def get_actors():  # noqa: E501
    """gets all actors

     # noqa: E501


    :rtype: List[Actor]
    """
    return 'do some magic!'


def get_films_by_actor(actor_id):  # noqa: E501
    """gets all film of specific actor

     # noqa: E501

    :param actor_id: Actor&#x27;s ID
    :type actor_id: int

    :rtype: List[Film]
    """
    return 'do some magic!'


def update_actor(body, actor_id):  # noqa: E501
    """Update all details about actor

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param actor_id: Actor&#x27;s ID
    :type actor_id: int

    :rtype: Actor
    """
    if connexion.request.is_json:
        body = Actor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
