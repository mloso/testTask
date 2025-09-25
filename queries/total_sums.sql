SELECT c.name                                AS customer_name,
       COALESCE(SUM(oi.amount * p.price), 0) AS total_amount
FROM customers c
         LEFT JOIN orders o ON c.id = o.customer_id
         LEFT JOIN order_items oi ON o.id = oi.order_id
         LEFT JOIN products p ON p.id = oi.product_id
GROUP BY c.id, c.name
ORDER BY total_amount DESC;