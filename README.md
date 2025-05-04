# Meesho Data Analysis(Interactive Dashboard creation using MS Excel) 

## Project Objective 
To analyze Meesho e-commerce order data to track performance metrics such as total orders, revenue, return rates, and order status trends, and to uncover insights into customer behavior, top-selling products, and regional sales performance—ultimately guiding data-driven decisions to optimize operations and reduce return rates.

## Dataset used 
- <a href="https://www.kaggle.com/datasets/sahilr05/meesho-orders">Dataset</a>

## Questions(KPIs)
- Which month had the highest number of orders, and what might have driven that peak?
- How many delivered orders were returned, and what is the return rate?
- What are the top selling products, and how much revenue did they generate individually?
- Is the revenue concentrated in just a few products or spread across many?
- Which states have the most orders, and are there any emerging regions to target next?
- How do Delivered, Cancelled, and Returned orders compare-and are any of thm unusually high?
- What are the top reasons for returns, and are certain products returned more often?
  
- Dashboard Interaction <a href="Dashboard_image.jpg">View Dashboard</a>

## Process
- Imported datasets into Python using pandas.
- Verified and cleaned data by handling missing values, duplicates, and incorrect data types.
- Merged order and return datasets using a common key (e.g., Sub Order Number).
- Calculated key metrics such as total orders, returns, return rate, and total revenue.
- Used matplotlib to visualize trends by month, product performance, and state-wise orders.
- Exported cleaned data to Excel for reporting and dashboard creation.
- Built an interactive Excel dashboard to present insights effectively.

## Dashboard 

![Dashboard_image](https://github.com/user-attachments/assets/351ad897-19e3-44e4-a36d-d26e384e7184)

## Project Insight 

- August saw the highest spike in orders, indicating a possible seasonal trend or successful campaign.
- More than 55% of delivered orders were returned, pointing to major post-purchase issues.
- "PARTY WEAR LOOK HEAVY EMBROIDERY AND 5mm SEQUINS WORK GOWN WITH DUPATTA" was the top-selling product, generating the most revenue alone.
- Revenue is concentrated in a few products, with others contributing very little.
- Uttar Pradesh had the highest number of orders, followed by Tamil Nadu and Kerala.
- Delivered orders accounted for only 50 out of 139 total, while returns and cancellations made up the rest.
- High return volumes indicate issues with quality, fit, or customer satisfaction.
- Cancelled orders were almost as frequent as delivered ones, suggesting buyer hesitation or shipping issues.
- States like Odisha and West Bengal also showed decent engagement, worth targeting further.
- Revenue and order volumes shift monthly, with a huge peak in August and near-zero in other months.

## Final Conclusion 

The analysis reveals that August had a significant spike in orders, indicating a successful campaign or seasonal trend. While most orders were successfully delivered, a considerable portion (over 77%) of returns came from delivered items, suggesting potential quality or expectation issues. Revenue is heavily concentrated among a few top-selling products, while some products show high return rates, needing further review. Gujarat leads in order volume, but there is scope to expand into underrepresented states. The dashboard provides clear visibility into order trends, product performance, regional activity, and return behavior—enabling data-driven decisions to optimize logistics, marketing strategies, and product quality.

