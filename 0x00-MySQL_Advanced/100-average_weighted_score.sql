DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_weighted_score DECIMAL(10, 2);
    DECLARE total_weight INT;

    -- Calculate the total weighted score and total weight for the given user
    SELECT SUM(score * p.weight), SUM(p.weight)
    INTO average_weighted_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET average_weighted_score = average_weighted_score / total_weight;
    ELSE
        SET average_weighted_score = 0;
    END IF;

    -- Update the user's average weighted score in the users table
    UPDATE users SET average_score = average_weighted_score WHERE id = user_id;
END //

DELIMITER ;
