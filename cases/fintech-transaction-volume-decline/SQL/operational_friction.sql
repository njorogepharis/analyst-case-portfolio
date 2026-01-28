-- operational_friction.sql
-- Checks transaction failure rates per month
SELECT DATE_TRUNC('month', transaction_date) AS month,
       COUNT(*) FILTER (WHERE status='failed') AS failed_tx,
       COUNT(*) AS total_tx,
       ROUND(COUNT(*) FILTER (WHERE status='failed')*100.0/COUNT(*),2) AS fail_rate
FROM transactions
GROUP BY month
ORDER BY month;
