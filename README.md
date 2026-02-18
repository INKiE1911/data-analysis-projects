📊 Digital Advertising Performance Analysis (Python EDA)
📌 Overview

This project performs exploratory data analysis (EDA) on an online advertising campaign dataset to evaluate campaign performance, user engagement trends, conversion efficiency, and return on investment (ROI).

The analysis is implemented in Python using Pandas for data manipulation and Matplotlib/Seaborn for visualization.

📂 Dataset

The dataset contains advertising performance metrics including:

Campaign number

Placement (banner size)

Displays

Clicks

Cost

Revenue

Post-click conversions

Post-click sales amount

User engagement type

Day & month (used to construct date)

The script:

Cleans missing values

Removes irrelevant columns

Standardizes campaign identifiers

Constructs a proper datetime column

🔎 Key Analyses Performed
1️⃣ User Engagement Trend Over Time

Aggregates clicks by date

Identifies overall engagement trend during campaign period

2️⃣ Impact of Banner Size

Total clicks by placement

Average engagement by banner size

3️⃣ Placement Performance

Highest displays

Highest clicks

Post-click conversion comparison

4️⃣ Correlation Analysis

Cost vs Revenue correlation

Clicks vs Revenue correlation

Heatmap visualization

5️⃣ Revenue Metrics

Revenue per click

ROI calculation

Cost per click (CPC)

Cost per conversion

6️⃣ Campaign Effectiveness

Click-through rate (CTR)

ROI by campaign and placement

Conversion performance comparison

7️⃣ Weekly & Seasonal Trends

Weekly aggregation of displays and clicks

Trend visualization

8️⃣ Outlier Detection

Boxplots for:

Cost

Clicks

Revenue

9️⃣ Engagement-Based Conversion Analysis

Conversion rates by user engagement type

Weekday vs weekend comparison

📈 Metrics Computed

CTR = Clicks / Displays

CPC = Cost / Clicks

ROI = (Revenue − Cost) / Cost

Revenue per Click

Post-click Conversion Rate

Cost per Conversion

🛠 Technologies Used

Python 3

Pandas

NumPy

Matplotlib

Seaborn

▶ How to Run

Install dependencies:

pip install -r requirements.txt


Update dataset path inside the script:

df = pd.read_csv("path_to_online_advertising_data.csv")


Run:

python FinlaticsProject01.py

📌 Notes

The dataset path is currently hardcoded and should be modified before running.

Division-by-zero cases are handled before computing CPC and conversion metrics.

Missing placement values are removed to maintain data consistency.

📊 Output

The script generates multiple visualizations including:

Line plots (trend analysis)

Bar charts (placement & campaign comparison)

Heatmaps (correlation)

Boxplots (outlier detection)

👤 Author

Amartya
