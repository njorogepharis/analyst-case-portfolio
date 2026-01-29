import pandas as pd

# Load campaign and orders data
campaigns = pd.read_csv('campaigns.csv')
orders = pd.read_csv('orders.csv')

# Merge datasets
data = campaigns.merge(orders, on='campaign_id', how='left')

# Compute conversion metrics
conversion_summary = data.groupby('campaign_id').agg(
    clicks=('clicks','sum'),
    orders=('order_id','nunique'),
    revenue=('revenue','sum')
)
conversion_summary['click_to_order_rate'] = conversion_summary['orders'] / conversion_summary['clicks']
conversion_summary['order_to_revenue_rate'] = conversion_summary['revenue'] / conversion_summary['orders']

conversion_summary.sort_values('order_to_revenue_rate', ascending=True, inplace=True)
