-- engagement_check.sql
-- Calculates average transactions per active user per month
SELECT
    DATE_TRUNC('month', transaction_date) AS month,
    COUNT(DISTINCT transaction_id)/COUNT(DISTINCT user_id) AS avg_tx_per_user
FROM transactions
GROUP BY 1
ORDER BY 1;
