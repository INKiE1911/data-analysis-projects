import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('B:\\Studies\\Finlatics DS+ML\\online_advertising_performance_data.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df.drop(columns=['Unnamed: 12','Unnamed: 13'],inplace=True)#removing unnamed columns
df['campaign_number'].replace({'camp 1':1,'camp 2':2,'camp 3':3},inplace=True)#replacing campaign number with respective numbers
#print number of naN values in each column
nan_counts = df.isna().sum()
#print("NaN value counts per column:\n", nan_counts)
#print(df['placement'].value_counts())
#here 413 values are NaN in placement column where the total number is 15000, i decided to drop these values as it is not a significant amount and maintain data purity
df.dropna(subset=['placement'],inplace=True)
nan_counts = df.isna().sum()
#print("NaN value counts per column after dropping NaNs in 'placement':\n", nan_counts)
#now data is clean and ready for analysis
#-----------------------------------------------------------------------------------
#overall trend in user engagement throughout the campaign period
df['date'] = pd.to_datetime(
    df['day'].astype(str) + ' ' +
    df['month'] + ' ' +
    '2020' # or any constant year
)

#print(df['date'].sort_values())
engagement_trend = df.groupby('date')['clicks'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=engagement_trend, x='date', y='clicks', marker='o')
plt.title('Overall User Engagement Trend Over Campaign Period')
plt.xlabel('Date')
plt.ylabel('Total Clicks')
plt.show
#-----------------------------------------------------------------------------------
#how does the size of ad impacts the numbber of clicks received
ad_size_engagement = df.groupby('placement')['clicks'].sum().reset_index().sort_values(by='clicks', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=ad_size_engagement, x='placement', y='clicks', palette='viridis')
plt.title('Impact of Ad Size on User Engagement')
plt.xlabel('Ad Size')
plt.ylabel('Total Clicks')
plt.show()
#-----------------------------------------------------------------------------------
#which placement yielded the highest number of displays and clicks
placement_performance_displays = df.groupby('placement').agg({'displays': 'sum',}).reset_index().sort_values(by='displays', ascending=False)
placement_performance_clicks = df.groupby('placement').agg({'clicks': 'sum',}).reset_index().sort_values(by='clicks', ascending=False)
print(placement_performance_displays.iloc[0],'had the highest number of displays')
print(placement_performance_clicks.iloc[0],'had the highest number of clicks')
#-----------------------------------------------------------------------------------
#correlation between cost of serving ads and revenue generated from clicks
correlation = df['cost'].corr(df['revenue'])
print(f'Correlation between cost of serving ads and revenue generated from clicks: {correlation}')
correlation_matrix = df[['cost', 'revenue']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix,annot=True,fmt=".2f",cmap='PuBuGn')
plt.title('Correlation between Cost and Revenue')
plt.show()
#-----------------------------------------------------------------------------------
#average revenue generated per click 
df['revenue_per_click'] = df['revenue'] / df['clicks']
average_revenue_per_click = df['revenue_per_click'].mean()
print(f'Average Revenue Generated per Click: {average_revenue_per_click}')
#-----------------------------------------------------------------------------------
#campaign with highest post-click conversion rate
df['post_click_conversion_rate'] = df['post_click_conversions'] / df['clicks']
campaign_performance = df.groupby('campaign_number')['post_click_conversion_rate'].mean().reset_index().sort_values(by='post_click_conversion_rate', ascending=False)
top_campaign = campaign_performance.iloc[0]
print(f'Campaign with Highest Post-Click Conversion Rate:\n{top_campaign}')
#-----------------------------------------------------------------------------------
#specific trends or patterns in post-click sales amounts over time
post_click_sales_trend = df.groupby('date')['post_click_sales_amount'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=post_click_sales_trend, x='date', y='post_click_sales_amount', marker='o', color='orange')
plt.title('Post-Click Sales Amount Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Post-Click Sales Amount')
plt.show()
#post click sales falls over time
#-----------------------------------------------------------------------------------
#How does the level of user engagement vary across different banner sizes
engagement_by_banner_size = df.groupby('placement')['clicks'].mean().reset_index().sort_values(by='clicks', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(data=engagement_by_banner_size, x='placement', y='clicks', palette='magma')
plt.title('User Engagement by Banner Size')
plt.xlabel('Banner Size')
plt.ylabel('Average Clicks')
plt.show()
#ghi banner sizes tend to have higher user engagement 
#-----------------------------------------------------------------------------------
#placement types result in the highest post-click conversion rates
conversion_by_placement = df.groupby('placement')['post_click_conversions'].mean().reset_index().sort_values(by='post_click_conversions', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(data=conversion_by_placement, x='placement', y='post_click_conversions', palette='PuBuGn')
plt.title('Post-Click Conversion Rates by Placement Type')
plt.xlabel('Placement Type')
plt.ylabel('Average Post-Click Conversion Rate')
plt.show()
#ghi placement types have higher post-click conversion rates
#-----------------------------------------------------------------------------------
#identify any seasonal patterns or fluctuations in displays and clicks throughout the campaign period
weekly_trend = (
    df
    .sort_values('date')
    .groupby(pd.Grouper(key='date', freq='W'))
    [['displays', 'clicks']]
    .sum()
    .reset_index()
)
#display over time
plt.figure(figsize=(12, 5))
plt.plot(weekly_trend['date'], weekly_trend['displays'], marker='o')

plt.title('Weekly Trend of Ad Displays')
plt.xlabel('Date')
plt.ylabel('Total Displays')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#clicks over time
plt.figure(figsize=(12, 5))
plt.plot(weekly_trend['date'], weekly_trend['clicks'], marker='o')

plt.title('Weekly Trend of Clicks')
plt.xlabel('Date')
plt.ylabel('Total Clicks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Displays and clicks exhibit noticeable short-term fluctuations throughout the campaign period, but no strong recurring seasonal pattern. Clicks generally follow display trends, with periods of divergence suggesting declining user engagement rather than pure exposure-driven seasonality.
#-----------------------------------------------------------------------------------
#correlation between user engagement levels and the revenue generated
engagement_revenue_correlation = df['clicks'].corr(df['revenue'])
print(f'Correlation between User Engagement Levels and Revenue Generated: {engagement_revenue_correlation}')
engagement_revenue_matrix = df[['clicks', 'revenue']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(engagement_revenue_matrix,annot=True,fmt=".2f",cmap='PuBuGn')
plt.title('Correlation between User Engagement and Revenue')
plt.show()
#there is a strong positive correlation between user engageement levels and revenue generated
#-----------------------------------------------------------------------------------
#outliers in terms of cost, clicks, or revenue that warrant further investigation
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1) #(rows, columns, postion)
sns.boxplot(y='cost', data=df, color='lightblue')
plt.title('Boxplot of Cost')
plt.subplot(1, 3, 2)
sns.boxplot(y='clicks', data=df, color='lightgreen')
plt.title('Boxplot of Clicks')
plt.subplot(1, 3, 3)
sns.boxplot(y='revenue', data=df, color='lightcoral')
plt.title('Boxplot of Revenue')
plt.tight_layout()
plt.show()
#The boxplots reveal significant right-skewed outliers in cost, clicks, and revenue. These indicate a small number of campaign instances with disproportionately high spend, engagement, or revenue. Such observations warrant further investigation to distinguish inefficient spend from high-performing opportunities.
#-----------------------------------------------------------------------------------
#How does the effectiveness of campaigns vary based on the size of the ad and placement type
campaign_effectiveness = df.groupby(['campaign_number', 'placement']).agg({
    'clicks': 'sum',
    'displays': 'sum',
    'post_click_conversions': 'sum'
}).reset_index()
campaign_effectiveness['click_through_rate'] = campaign_effectiveness['clicks'] / campaign_effectiveness['displays']
plt.figure(figsize=(12, 6))
sns.barplot(data=campaign_effectiveness, x='placement', y='click_through_rate', hue='campaign_number', palette='Set2')
plt.title('Campaign Effectiveness by Ad Size and Placement Type')
plt.xlabel('Placement Type')
plt.ylabel('Click-Through Rate')
plt.show()
#Campaign effectiveness varies notably across ad sizes and placement types. Larger ad sizes and premium placements generate higher engagement volumes, while certain placement types demonstrate superior conversion efficiency. This highlights a trade-off between scale and efficiency, emphasizing the importance of optimizing both ad size and placement strategy to maximize campaign performance.
#-----------------------------------------------------------------------------------
#any specific campaigns or banner sizes that consistently outperform others in terms of ROI
df['ROI'] = (df['revenue'] - df['cost']) / df['cost']
roi_performance = df.groupby(['campaign_number', 'placement'])['ROI'].mean().reset_index().sort_values(by='ROI', ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(data=roi_performance, x='placement', y='ROI', hue='campaign_number', palette='Set3')
plt.title('ROI Performance by Campaign and Banner Size')
plt.xlabel('Banner Size')
plt.ylabel('Average ROI')
plt.show()
#ROI of DEF campaign is consistently higher across various banner sizes, indicating superior cost efficiency and revenue generation compared to other campaigns. Additionally, larger banner sizes tend to yield better ROI, suggesting that investing in more prominent ad placements can enhance overall campaign profitability.
#-----------------------------------------------------------------------------------
#the distribution of post-click conversions across different placement types
plt.figure(figsize=(10, 6))
sns.boxplot(x='placement', y='post_click_conversions', data=df, palette='Pastel1')
plt.title('Distribution of Post-Click Conversions by Placement Type')
plt.xlabel('Placement Type')
plt.ylabel('Post-Click Conversions')
plt.show()
#The boxplot reveals that certain placement types, particularly 'ghi', exhibit higher median post-click conversions and greater variability. This suggests that these placements are more effective at driving user actions post-click, likely due to better visibility or relevance. Conversely, placements like 'abc' show lower conversion rates, indicating potential inefficiencies in those ad formats.
#-----------------------------------------------------------------------------------
#any noticeable differences in user engagement levels between weekdays and weekends
df['day_of_week'] = df['date'].dt.day_name()
engagement_by_day = (df.groupby('day_of_week')['clicks'].sum().reindex(['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']).reset_index())
plt.figure(figsize=(10, 6))
sns.barplot(data=engagement_by_day,x='day_of_week',y='clicks',palette='coolwarm')
plt.title('Total Clicks by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Clicks')
plt.show()
#weekends are little higher in user engagement levels compared to weekdays (except wednesday)
#-----------------------------------------------------------------------------------
#how does the cost per click (CPC) vary across different campaigns and banner sizes
df = df[df['clicks'] > 0].copy()#to avoid division by zero
df['CPC'] = df['cost'] / df['clicks']
cpc_performance = df.groupby(['campaign_number', 'placement'])['CPC'].mean().reset_index().sort_values(by='CPC', ascending=True)
plt.figure(figsize=(12, 6))
sns.barplot(data=cpc_performance, x='placement', y='CPC', hue='campaign_number', palette='Set1')
plt.title('Cost Per Click (CPC) by Campaign and Banner Size')
plt.xlabel('Banner Size')
plt.ylabel('Average CPC')
plt.show()
#highest for mno lowest for ghi
#-----------------------------------------------------------------------------------
#any campaigns or placements that are particularly cost-effective in terms of generating post-click conversions
df = df[df['post_click_conversions'] > 0].copy()#to avoid division by zero
df['cost_per_conversion'] = df['cost'] / df['post_click_conversions']
cost_effectiveness = df.groupby(['campaign_number', 'placement'])['cost_per_conversion'].mean().reset_index().sort_values(by='cost_per_conversion', ascending=True)
plt.figure(figsize=(12, 6))
sns.barplot(data=cost_effectiveness, x='placement', y='cost_per_conversion', hue='campaign_number', palette='Set2')
plt.title('Cost Effectiveness by Campaign and Placement')
plt.xlabel('Placement Type')
plt.ylabel('Average Cost per Conversion')
plt.show()
#tbd
#-----------------------------------------------------------------------------------
#identify any trends or patterns in post-click conversion rates based on the day of the week
conversion_by_day = df.groupby('day_of_week')['post_click_conversions'].mean().reindex(['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=conversion_by_day, x='day_of_week', y='post_click_conversions', palette='Set3')
plt.title('Post-Click Conversion Rates by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Post-Click Conversions')
plt.show()
#lowest on thursday,friday
#-----------------------------------------------------------------------------------
#effectiveness of campaigns vary throughout different user engagement types in terms of post-click conversions
engagement_types = (df.groupby('user_engagement').agg({'post_click_conversions': 'sum','clicks': 'sum'}).reset_index())
engagement_types = engagement_types[engagement_types['clicks'] > 0]
engagement_types['conversion_rate'] = (engagement_types['post_click_conversions'] / engagement_types['clicks'])
plt.figure(figsize=(10, 6))
sns.barplot(data=engagement_types,x='user_engagement',y='conversion_rate',palette='viridis')
plt.title('Effectiveness of Engagement Types in Post-Click Conversions')
plt.xlabel('Engagement Type')
plt.ylabel('Conversion Rate')
plt.show()
#high engagement types have higher conversion rates
#-----------------------------------------------------------------------------------
#donee yay


