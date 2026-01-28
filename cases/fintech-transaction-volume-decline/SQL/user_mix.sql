-- user_mix.sql
-- Compares transaction volume of new vs returning users per month
SELECT
    user_type,
    DATE_TRUNC('month', transaction_date) AS month,
    SUM(amount) AS total_volume,
    COUNT(DISTINCT user_id) AS active_users
FROM transactions
JOIN users USING(user_id)
GROUP BY user_type, month
ORDER BY month;
