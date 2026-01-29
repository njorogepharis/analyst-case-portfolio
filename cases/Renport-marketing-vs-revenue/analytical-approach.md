## Analytical Approach

The analysis aimed to uncover why strong marketing signals were not translating into revenue:

1. **Data Integration**
   - Combined marketing campaign data (clicks, impressions, leads) with operational and fulfillment data to analyze the full **marketing-to-revenue pipeline**.

```sql
-- Combine campaign engagement with actual orders
SELECT 
    c.campaign_id,
    c.platform,
    c.engagements,
    c.clicks,
    o.order_id,
    o.status,
    o.revenue
FROM campaigns c
LEFT JOIN orders o
    ON c.campaign_id = o.campaign_id
WHERE c.campaign_date BETWEEN '2025-01-01' AND '2025-12-31';
