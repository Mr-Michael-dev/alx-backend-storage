-- creates a trigger that resets the attribute valid_email
-- only when the email has been changed

DELIMITER //
CREATE TRIGGER reset_valid_email_trigger
BEFORE UPDATE ON `users`
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        IF NEW.email REGEXP '^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' AND NEW.email NOT LIKE '%+%' THEN
            SET NEW.valid_email = 1;
        ELSE
            SET NEW.valid_email = 0;
        END IF;
    END IF;
END//

DELIMITER ;