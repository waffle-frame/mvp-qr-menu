from flask_jwt_extended import current_user, verify_jwt_in_request, get_jwt

from models.places import Places
from utils.response import error_response

# The decorator allows you to check the authorized user 
# during the request for membership to the place.
def check_user_permission():
    def wrapper(fn):
        def decorator(*args, **kwargs):
            verify_jwt_in_request()

            place = Places.get_or_none(name=kwargs.get("place"))
            if place is None:
                return error_response("permission_denied")

            print(args)

            claims = get_jwt()
            if claims["sub"] == place.user.id:
                return fn(place.id)
            else:
                return error_response("permission_denied")

        return decorator

    return wrapper