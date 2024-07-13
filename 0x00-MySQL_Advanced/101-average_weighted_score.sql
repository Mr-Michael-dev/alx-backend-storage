-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN cur;

    read_loop: LOOP
        -- Fetch the next user_id
        FETCH cur INTO user_id;

        -- Exit the loop if there are no more rows
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the average weighted score for the current user
        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END //

DELIMITER ;
