# Cyclistic Bike-Share Analysis
**Google Data Analytics Certificate — Capstone Project**
**Analyst:** Adaeze Princess Umahi | [LinkedIn](https://linkedin.com/in/adaezeumahi) | [Tableau Dashboard](https://public.tableau.com/app/profile/adaeze.princess.umahi/viz/CyclisticBike-ShareAnalysisAdaezePrincessUmahi/Dashboard1)

---

## Business Question
How do annual members and casual riders use Cyclistic bikes differently?

---

## Data
- **Source:** Divvy Trip Data (Motivate International Inc.)
- **Period:** January 2025 – April 2026
- **Raw data:** 5,697,455 rides
- **After cleaning:** 5,535,677 rides
- **Cleaning removed:** 161,778 rides (under 1 min, over 24 hrs, duplicates)

---

## Tools Used
- **Python (pandas)** — data loading, cleaning and analysis
- **Tableau Public** — interactive visualisations and dashboard
- **Folium** — interactive geographic station map
- **GitHub** — version control and portfolio

---

## Analysis Framework — Google Data Analysis Process

This project follows the 6-phase data analysis process from the Google Data Analytics Certificate:

### 1. Ask
Defined the business question: *How do annual members and casual riders use Cyclistic bikes differently?*
Identified the goal: generate data-backed recommendations to convert casual riders into annual members.

### 2. Prepare
Downloaded 12 months of Divvy trip data (January 2025 – April 2026) from Motivate International Inc.
Verified data credibility — reliable, original, comprehensive, current and cited (ROCCC).
Confirmed 13 columns across 5,697,455 rows with no personally identifiable information.

### 3. Process
Cleaned and transformed data using Python (pandas):
- Converted timestamps to datetime format
- Calculated `ride_length_mins` from start and end times
- Extracted `day_of_week`, `month`, `hour_of_day` and `season`
- Removed 161,778 invalid rides (under 1 minute, over 24 hours, duplicates)
- Final clean dataset: 5,535,677 rides

### 4. Analyse
Generated 8 summary tables to identify patterns and differences between rider types:
- Ride length by rider type
- Rides by day of week, month, hour of day and season
- Bike type preference
- Top 15 start stations for casual and member riders
- Created an interactive geographic map using Folium

### 5. Share
Communicated findings through:
- 8 interactive Tableau visualisations published on Tableau Public
- A combined dashboard: *Cyclistic Bike-Share Analysis: Member vs Casual Riders*
- An interactive Folium map showing the geographic split between rider types across Chicago
- This GitHub repository with full documentation, screenshots and analysis files

### 6. Act
Three data-backed recommendations for converting casual riders to annual members:
1. **Weekend-to-Member Conversion Campaign** — target casual riders at leisure stations on Saturdays and Sundays
2. **Summer Pass Product** — discounted 3-month membership targeting the June–August spike
3. **Electric Bike Member Incentives** — priority access to electric bikes to increase membership value

---

## Key Findings
1. **Ride Length:** Casual riders average 19.72 mins vs members at 12.26 mins — casuals ride 60% longer per trip
2. **Day Pattern:** Casuals peak on weekends (Saturday/Sunday), members peak on weekdays (Thu/Fri) — leisure vs commute behaviour
3. **Time of Day:** Members show clear commute peaks at 8am and 5pm; casuals build gradually through the afternoon
4. **Seasonality:** Both groups peak in summer — casual ridership drops 90% in winter vs 70% for members
5. **Top Casual Stations:** Navy Pier, DuSable Lake Shore, Millennium Park — all tourist and leisure locations
6. **Top Member Stations:** Kingsbury/Kinzie, Canal/Madison, Clinton St — all downtown commuter corridors
7. **Bike Preference:** Both groups prefer electric bikes; casuals on classic bikes ride nearly twice as long (29 mins vs 14 mins)

---

## Visualisations

### Rides by Day of Week
![Rides by Day of Week](Rides%20by%20Day%20of%20Week.png)

### Rides by Month
![Rides by Month](Rides%20by%20Month.png)

### Rides by Hour of Day
![Rides by Hour of Day](Rides%20by%20Hour%20of%20Day.png)

### Average Ride Length by Day
![Avg Ride Length by Day](Avg%20Ride%20Length%20by%20Day.png)

### Rides by Season
![Rides by Season](Rides%20by%20Season.png)

### Bike Type Preference
![Bike Type Preference](Bike%20Type%20Preference.png)

### Top Casual Stations
![Top Casual Stations](Top%20Casual%20Stations.png)

### Top Member Stations
![Top Member Stations](Top%20Member%20Stations.png)

---

## Three Data-Backed Recommendations

### 1. Weekend-to-Member Conversion Campaign
Target casual riders at top leisure stations (Navy Pier, Millennium Park) on Saturdays and Sundays with a discounted annual membership offer. 37% of all casual rides happen on weekends — this is the highest-impact conversion window.

### 2. Summer Pass Product
Introduce a discounted 3-month membership targeting the June–August casual ridership spike (910,681 casual rides in summer alone), with automatic renewal prompts before the winter drop-off.

### 3. Electric Bike Member Incentives
Both groups prefer electric bikes. Offer members priority access or reduced per-minute rates on electric bikes to increase the value proposition of annual membership and accelerate casual-to-member conversion.

---

## Tableau Dashboard
[View Interactive Dashboard](https://public.tableau.com/app/profile/adaeze.princess.umahi/viz/CyclisticBike-ShareAnalysisAdaezePrincessUmahi/Dashboard1)

---

## Interactive Station Map

The file `cyclistic_station_map.html` is included in this repository. To view the interactive map:
1. Click on `cyclistic_station_map.html` in the file list above
2. Click **"Download raw file"**
3. Open the downloaded file in any browser

The map shows top casual rider stations (🔴 red) and member stations (🔵 blue) across Chicago, visually confirming the leisure vs commuter geographic split.

---

## Repository Files

| File | Description |
|------|-------------|
| `cyclistic_analysis.py` | Full Python script — loading, cleaning, analysis and map generation |
| `01_ride_length_summary.csv` | Average, median and max ride length by rider type |
| `02_rides_by_day.csv` | Ride counts and average length by day of week |
| `03_rides_by_month.csv` | Monthly ride patterns by rider type |
| `04_rides_by_hour.csv` | Hourly ride distribution by rider type |
| `05_rides_by_season.csv` | Seasonal breakdown by rider type |
| `06_rides_by_bike_type.csv` | Bike type preference by rider type |
| `07_top_stations_casual.csv` | Top 15 casual rider start stations |
| `08_top_stations_member.csv` | Top 15 member start stations |
| `cyclistic_station_map.html` | Interactive Folium map — casual vs member start stations |
| `Rides by Day of Week.png` | Chart — total rides by day of week |
| `Rides by Month.png` | Chart — monthly ride patterns |
| `Rides by Hour of Day.png` | Chart — hourly ride distribution |
| `Avg Ride Length by Day.png` | Chart — average ride length by day |
| `Rides by Season.png` | Chart — seasonal ride breakdown |
| `Bike Type Preference.png` | Chart — bike type usage by rider type |
| `Top Casual Stations.png` | Chart — top 15 casual start stations |
| `Top Member Stations.png` | Chart — top 15 member start stations |

---

## About Me
**Adaeze (Princess) Umahi**  
Data Analyst | Medical Doctor (MBBS) | MPH — Epidemiology, Biostatistics & Data Science (University of Glasgow)  
SQL · Python · R · Power BI · Tableau · Microsoft Dynamics 365  
Google Data Analytics Certified | Code First Girls & DataCamp — SQL, Python, AI & Machine Learning | Data Analyst with Python (DataCamp) | Machine Learning Fundamentals (DataCamp) | Microsoft Power BI PL-300 (In Progress)  
Building a portfolio at the intersection of health data, business intelligence and real-world analytical impact.  
[LinkedIn](https://www.linkedin.com/in/adaezeumahi/) | [GitHub](https://github.com/PrincessUmahi)
