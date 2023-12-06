-- name: create-new-grade<!
INSERT INTO grade (grade_name)
VALUES (:grade_name)
RETURNING
    id, created_at, updated_at;


-- name: create-new-class<!
INSERT INTO class (class_name, grade_id)
VALUES (:class_name, :grade_id)
RETURNING
    id, created_at, updated_at;