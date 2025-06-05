CREATE TABLE `users` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_nisit` varchar(255),
  `password` varchar(255),
  `coupon_meal_used` integer,
  `coupon_sweet_used` integer,
  `created_at` timestamp
);

CREATE TABLE `stores` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `store_type` varchar(255),
  `user_store` varchar(255),
  `password` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `orders` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `store_id` integer NOT NULL,
  `created_at` timestamp
);

ALTER TABLE `orders` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `orders` ADD FOREIGN KEY (`store_id`) REFERENCES `stores` (`id`);