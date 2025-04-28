from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dummy data
dummy_data = {
    "bar_chart_data": [
        { "Date": "2025-04-15", "Applications": 12 },
        { "Date": "2025-04-16", "Applications": 14 },
        { "Date": "2025-04-17", "Applications": 18 },
        { "Date": "2025-04-18", "Applications": 15 },
        { "Date": "2025-04-19", "Applications": 21 },
        { "Date": "2025-04-20", "Applications": 10 },
        { "Date": "2025-04-21", "Applications": 17 }
    ],
    "radar_chart_data": [
        { "Experience Level": "0-1 years", "Count": 21 },
        { "Experience Level": "1-3 years", "Count": 17 },
        { "Experience Level": "3-5 years", "Count": 10 },
        { "Experience Level": "5-7 years", "Count": 8 },
        { "Experience Level": "7+ years", "Count": 5 }
    ],
    "line_chart_data": [
        { "Date": "2025-04-15", "LinkedIn Applicants": 2 },
        { "Date": "2025-04-16", "LinkedIn Applicants": 5 },
        { "Date": "2025-04-17", "LinkedIn Applicants": 2 },
        { "Date": "2025-04-18", "LinkedIn Applicants": 7 },
        { "Date": "2025-04-19", "LinkedIn Applicants": 4 },
        { "Date": "2025-04-20", "LinkedIn Applicants": 6 },
        { "Date": "2025-04-21", "LinkedIn Applicants": 8 }
    ]
}

# GET endpoint for full dummy data
@app.get("/data")
async def get_all_data():
    return dummy_data

# GET endpoint for bar chart data
@app.get("/data/bar-chart")
async def get_bar_chart_data():
    return dummy_data["bar_chart_data"]

# GET endpoint for radar chart data
@app.get("/data/radar-chart")
async def get_radar_chart_data():
    return dummy_data["radar_chart_data"]

# GET endpoint for line chart data
@app.get("/data/line-chart")
async def get_line_chart_data():
    return dummy_data["line_chart_data"]
