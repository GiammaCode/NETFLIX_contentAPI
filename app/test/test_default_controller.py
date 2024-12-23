# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.actor import Actor  # noqa: E501
from app.models.film import Film  # noqa: E501
from app.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_actors_actor_id_delete(self):
        """Test case for actors_actor_id_delete

        Remove a specific Actor.
        """
        response = self.client.open(
            '/content_api/actors/{actorId}'.format(actor_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_actor(self):
        """Test case for create_actor

        Add a new actor
        """
        body = Actor()
        response = self.client.open(
            '/content_api/actors',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_films_get(self):
        """Test case for films_get

        Return a list of all available films.
        """
        response = self.client.open(
            '/content_api/films',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_films_id_delete(self):
        """Test case for films_id_delete

        Remove a specific film.
        """
        response = self.client.open(
            '/content_api/films/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_films_id_get(self):
        """Test case for films_id_get

        Return information about specific film.
        """
        response = self.client.open(
            '/content_api/films/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_films_id_put(self):
        """Test case for films_id_put

        Update information about specific film
        """
        body = Film()
        response = self.client.open(
            '/content_api/films/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_films_post(self):
        """Test case for films_post

        Add a new film (work with singol film)
        """
        body = Film()
        response = self.client.open(
            '/content_api/films',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_actor_by_id(self):
        """Test case for get_actor_by_id

        gets a specific actor
        """
        response = self.client.open(
            '/content_api/actors/{actorId}'.format(actor_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_actors(self):
        """Test case for get_actors

        gets all actors
        """
        response = self.client.open(
            '/content_api/actors',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_films_by_actor(self):
        """Test case for get_films_by_actor

        gets all film of specific actor
        """
        response = self.client.open(
            '/content_api/actors/{actorId}/films'.format(actor_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_actor(self):
        """Test case for update_actor

        Update all details about actor
        """
        body = Actor()
        response = self.client.open(
            '/content_api/actors/{actorId}'.format(actor_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
