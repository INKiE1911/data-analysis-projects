Digital Advertising Performance Analysis

Exploratory Data Analysis using Python

Overview

This project analyzes a digital advertising campaign dataset to understand how campaigns, placements, and user engagement influence clicks, conversions, and overall return on investment.

The objective was to evaluate campaign performance from a practical business perspective and identify where advertising spend is effective and where it is inefficient.

The analysis is implemented in Python using Pandas for data manipulation and Matplotlib and Seaborn for visualization.

Dataset

The dataset contains performance metrics for multiple advertising campaigns, including:

• Campaign number
• Placement or banner size
• Displays
• Clicks
• Cost
• Revenue
• Post click conversions
• Post click sales amount
• User engagement type
• Day and month, used to construct a date column

Before analysis, the data was cleaned by removing irrelevant columns, handling missing placement values, standardizing campaign identifiers, and constructing a proper datetime field for time based analysis.

Analysis Performed

The project explores campaign performance from several perspectives.

Engagement Trends

Total clicks were aggregated by date to evaluate how user engagement changed during the campaign period.

Placement and Banner Performance

Click volumes and average engagement were compared across different banner sizes to identify high performing placements.

Campaign Effectiveness

Campaign performance was evaluated using metrics such as CTR, ROI, and post click conversion rate. Comparisons were made across campaigns and placements to understand relative efficiency.

Cost and Revenue Relationships

Correlation analysis was conducted to examine the relationship between cost and revenue, as well as clicks and revenue. A heatmap was used to visualize the strength of these relationships.

Revenue and Efficiency Metrics

The following metrics were calculated:

CTR calculated as clicks divided by displays
CPC calculated as cost divided by clicks
ROI calculated as revenue minus cost divided by cost
Revenue per click
Post click conversion rate
Cost per conversion

Weekly Trends

Displays and clicks were aggregated weekly to observe short term fluctuations and detect broader patterns over time.

Outlier Detection

Boxplots were used to identify extreme values in cost, clicks, and revenue that may require further investigation.

Engagement Based Conversion Analysis

Conversion rates were compared across different user engagement types. Performance differences between weekdays and weekends were also evaluated.

Technologies Used

Python 3
Pandas
NumPy
Matplotlib
Seaborn

How to Run

Install dependencies:

pip install -r requirements.txt


Update the dataset path inside the script:

df = pd.read_csv("path_to_online_advertising_data.csv")


Run the script:

python FinlaticsProject01.py

What This Project Demonstrates

Data cleaning and preprocessing
Computation of core marketing performance metrics
Exploratory data analysis
Trend and correlation evaluation
Ability to translate raw campaign data into meaningful performance insights

Author

Amartya
