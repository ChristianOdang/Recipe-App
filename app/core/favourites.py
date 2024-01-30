''' 
Module for favourite CRUD
'''

from core.db import session
from core.model import Favourite


def getfirst_item():
    # call the session with model as param
    results = session.query(Favourite).first()

    # close session
    session.close()
    # return object
    return results


def get_all():
    # call the session with model as param
    results = session.query(Favourite).all()

    # close db connection
    session.close()

    # return DB object
    return results


def add_favourite(favourite_uri):
    # use mode to get table details
    fav = Favourite(favourites=favourite_uri)

    # use the add method to add param
    session.add(fav)

    # commit changes
    session.commit()


def remove_uri(uri_id):
    # call get element and delete
    session.query(Favourite).filter(Favourite.favourites == uri_id).delete()
    session.commit()


def get_item(id):
    results = session.query(Favourite).filter(
        Favourite.favourites == id).first()
    session.close()
    return results
