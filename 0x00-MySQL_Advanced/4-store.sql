-- Script creates a TRIGGER that decreases the quantity OF an item after adding a new ORDER

DROP TRIGGER decrease_items;
DELIMITER $$
CREATE TRIGGER decrease_items AFTER INSERT ON `orders`
FOR EACH ROW
UPDATE `items`
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name$$
DELIMITER ;