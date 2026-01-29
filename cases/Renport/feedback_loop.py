# Rolling 30-day failure rate
data['order_month'] = data['order_date'].dt.to_period('M')
monthly_failures = data.groupby('order_month').agg(
    failed_orders=('status', lambda x: (x=='Failed').sum()),
    cancelled_orders=('status', lambda x: (x=='Cancelled').sum())
)
monthly_failures['failure_rate'] = monthly_failures['failed_orders'] / monthly_failures['failed_orders'].sum()
monthly_failures['cancellation_rate'] = monthly_failures['cancelled_orders'] / monthly_failures['cancelled_orders'].sum()
monthly_failures.rolling(3).mean().plot(title='3-Month Rolling Failure & Cancellation Rate')
