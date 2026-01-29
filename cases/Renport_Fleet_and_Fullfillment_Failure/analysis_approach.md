## Analytical Approach

The analysis combined **data-driven investigation** with **systems thinking**:

1. **Data Collection & Integration**
   - SQL queries extracted order, fleet, and operational workflow data from renport database: 
```sql
-- Identify delayed orders by fleet
SELECT 
    o.order_id,
    o.customer_id,
    o.order_date,
    o.approval_date,
    o.fulfillment_date,
    f.fleet_id,
    f.status AS fleet_status,
    DATEDIFF(day, o.approval_date, o.fulfillment_date) AS fulfillment_delay
FROM orders o
JOIN fleet_assignments f
    ON o.order_id = f.order_id
WHERE o.order_date BETWEEN '2024-01-01' AND '2024-12-31';
