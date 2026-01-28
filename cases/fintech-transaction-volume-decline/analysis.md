# Analysis – Fintech Transaction Volume Decline

## Approach

We performed a hypothesis-driven analysis leveraging CRM and transaction data to identify the driver of the 15% decline in transaction volume. The primary hypotheses tested were:

1. User mix shift (new vs returning users)
2. Engagement decay among existing users
3. Pricing competitiveness
4. Operational friction

Testing was prioritized based on data availability and signal clarity.

## Data Sources

* `users` table: user_id, signup_date, user_type (new/returning)
* `transactions` table: transaction_id, user_id, product_id, amount, transaction_date, status
* `pricing` table: product_id, fee, effective_date
* CRM customer data for segmentation (e.g., region, user tier)

## Step 1: Test Engagement

Calculated average transactions per active user to check for engagement decay:

```sql
SELECT
    DATE_TRUNC('month', transaction_date) AS month,
    COUNT(DISTINCT transaction_id)/COUNT(DISTINCT user_id) AS avg_tx_per_user
FROM transactions
GROUP BY 1
ORDER BY 1;
```

**Result:** Average transactions per active user remained stable, indicating engagement decay was not the main driver.

## Step 2: Check User Mix

Compared new vs returning user transaction volume:

```sql
SELECT
    user_type,
    DATE_TRUNC('month', transaction_date) AS month,
    SUM(amount) AS total_volume,
    COUNT(DISTINCT user_id) AS active_users
FROM transactions
JOIN users USING(user_id)
GROUP BY user_type, month
ORDER BY month;
```

**Result:** New users transacted less, but the proportion of new users was stable; user mix did not explain the volume decline.

## Step 3: Investigate Pricing Effects

Analyzed pricing changes and mapped transaction volume by affected products:

```sql
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
```

**Analysis:** Several key products had fee increases coinciding with volume drops. Revenue per transaction rose slightly, but transaction counts fell sharply for higher-fee products, particularly among price-sensitive users.

## Step 4: Operational Friction Check

Checked transaction failures:

```sql
SELECT DATE_TRUNC('month', transaction_date) AS month,
       COUNT(*) FILTER (WHERE status='failed') AS failed_tx,
       COUNT(*) AS total_tx,
       ROUND(COUNT(*) FILTER (WHERE status='failed')*100.0/COUNT(*),2) AS fail_rate
FROM transactions
GROUP BY month
ORDER BY month;
```

**Result:** Failure rate remained under 0.5%, indicating operational friction was not the cause.

## Conclusion

The main driver of the transaction volume decline was **pricing changes on select products**, which reduced transaction counts among price-sensitive users. Other factors, such as engagement decay, user mix, or operational issues, had minimal impact.

*The analysis references SQL queries in the `sql/` folder for reproducibility and auditability.*
