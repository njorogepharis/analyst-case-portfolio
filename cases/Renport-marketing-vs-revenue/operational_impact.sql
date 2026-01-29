-- Campaigns affected by operational delays
SELECT 
    c.campaign_id,
    r.region,
    AVG(DATEDIFF(day, o.approval_date, o.fulfillment_date)) AS avg_fulfillment_delay,
    SUM(o.revenue) AS total_revenue
FROM campaigns c
JOIN orders o
    ON c.campaign_id = o.campaign_id
JOIN regions r
    ON o.region_id = r.region_id
GROUP BY c.campaign_id, r.region
ORDER BY avg_fulfillment_delay DESC;
