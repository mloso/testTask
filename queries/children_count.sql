SELECT parent.id,
       parent.name     AS category_name,
       COUNT(child.id) AS children_count
FROM categories parent
         LEFT JOIN categories child ON parent.id = child.parent_id
GROUP BY parent.id, parent.name
ORDER BY children_count DESC;