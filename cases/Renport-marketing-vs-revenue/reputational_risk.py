# Merge sentiment score
sentiment = pd.read_csv('campaign_sentiment.csv')
data = data.merge(sentiment, on='campaign_id', how='left')

# Correlation of sentiment with order-to-revenue conversion
correlation = data['sentiment_score'].corr(data['order_to_revenue_rate'])
print(f"Correlation between sentiment and conversion: {correlation:.2f}")
