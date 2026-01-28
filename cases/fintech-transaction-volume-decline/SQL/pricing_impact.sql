-- pricing_impact.sql
-- Analyzes impact of product fee changes on transaction volume
SELECT
    p.product_id,
    p.fee AS current_fee,
    COUNT(t.transaction_id) AS tx_count,
    SUM(t.amount) AS tx_volume
FROM transactions t
JOIN pricing p ON t.product_id = p.product_id
WHERE t.transaction_date >= '2025-11-01'
GROUP BY p.product_id, p.fee
ORDER BY tx_volume ASC;
