SELECT 
    fleet_id,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN status = 'Failed' THEN 1 ELSE 0 END) AS failed_orders,
    SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders,
    AVG(DATEDIFF(day, approval_date, fulfillment_date)) AS avg_delay_days
FROM orders
JOIN fleet_assignments USING(order_id)
GROUP BY fleet_id
ORDER BY avg_delay_days DESC;
