SELECT p.name         AS product_name,
       COALESCE(
               CASE
                   WHEN c.parent_id IS NULL THEN c.name
                   ELSE (SELECT name FROM categories WHERE id = c.parent_id AND parent_id IS NULL)
                   END,
               'Без категории'
       )              AS top_level_category,
       SUM(oi.amount) AS total_sold_units
FROM order_items oi
         JOIN orders o ON oi.order_id = o.id
         JOIN products p ON oi.product_id = p.id
         LEFT JOIN categories c ON p.category_id = c.id
WHERE o.order_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
  AND o.order_date < DATE_TRUNC('month', CURRENT_DATE)
GROUP BY p.id, p.name, top_level_category
ORDER BY total_sold_units DESC
LIMIT 5;