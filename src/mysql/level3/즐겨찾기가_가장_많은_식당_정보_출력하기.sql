SELECT T1.food_type AS food_type
    , T1.rest_id AS rest_id
    , T1.rest_name AS rest_name
    , T1.favorites AS favorites
FROM rest_info AS T1
    -- MAX결과를 원본 테이블과 JOIN 함으로써 MAX결과가 포함된 row를 추출할 수 있게 됨
    INNER JOIN (SELECT food_type, MAX(favorites) AS favorites
                FROM rest_info GROUP BY food_type) AS T2
    ON T1.food_type = T2.food_type AND T1.favorites = T2.favorites
ORDER BY food_type DESC;