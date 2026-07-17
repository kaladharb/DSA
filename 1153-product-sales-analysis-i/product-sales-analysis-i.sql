SELECT 
    p.product_name,
    s.year,
    s.price
FROM Sales AS s
INNER JOIN Product AS P
ON s.product_id=p.product_id;