INSERT INTO users(username, password, created_at)
VALUES ('admin', 'admin', CURRENT_TIMESTAMP);

INSERT INTO places(name, user_id)
VALUES ('28makaka', 1);

INSERT INTO banners(name, photo, position, place_id, hide)
VALUES ('Banner nigga name', 'no_photo.png', 1, 1, 0);

INSERT INTO foodcategories(name, position, place_id, hide)
VALUES ("Food category name", 1, 1, 0);

INSERT INTO food(name, photo, composition, time_for_preparing, weight, price, position, place_id, hide)
VALUES ("Baked nigga", 'no_photo.png', 'Nigger, oil', 10, 551, 110, 1, 1, 0);

