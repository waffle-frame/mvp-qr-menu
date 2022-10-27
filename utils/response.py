dict_of_errors = {
    "place_not_found": ("place not found", 404),
    "banner_not_found": ("banner not found", 404),
    "photo_banner_not_found": ("banner photo not found", 404),
    "food_category_not_found": ("category not found", 404),
    "bad_request": ("bad request", 400),
    "wrong_data": ("wrong username or password", 401),
    "permission_denied": ("permission denied", 403),
    "internal_server": ("internal server error", 500),
    
}

def error_response(error: str):
    error_message, status = dict_of_errors[error]

    json_data = {
        "error": error_message
    }

    return json_data, status
