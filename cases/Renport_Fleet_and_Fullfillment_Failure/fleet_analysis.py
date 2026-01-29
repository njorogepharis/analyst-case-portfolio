import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
orders = pd.read_csv('orders.csv', parse_dates=['order_date','approval_date','fulfillment_date'])
fleet = pd.read_csv('fleet_assignments.csv')

# Merge datasets
data = orders.merge(fleet, on='order_id')

# Calculate delays and cancellation impact
data['fulfillment_delay'] = (data['fulfillment_date'] - data['approval_date']).dt.days
fleet_summary = data.groupby('fleet_id').agg(
    total_orders=('order_id','count'),
    failed_orders=('status', lambda x: (x=='Failed').sum()),
    cancelled_orders=('status', lambda x: (x=='Cancelled').sum()),
    avg_delay=('fulfillment_delay','mean')
).reset_index()

# Visualize top bottleneck fleets
fleet_summary.sort_values('avg_delay', ascending=False, inplace=True)
plt.figure(figsize=(10,6))
plt.bar(fleet_summary['fleet_id'], fleet_summary['avg_delay'])
plt.title('Average Fulfillment Delay by Fleet')
plt.xlabel('Fleet ID')
plt.ylabel('Avg Delay (Days)')
plt.show()
