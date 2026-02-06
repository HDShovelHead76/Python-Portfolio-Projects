from flask import Flask, render_template, request
import pandas as pd
import math
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():
    stations_df = pd.read_csv("data_small/stations.txt", skiprows=17)
    stations_df.columns = stations_df.columns.str.strip()
    # Select only the columns you want
    stations_df = stations_df[['STAID', 'STANAME']]
    # Strip whitespace inside station names
    stations_df['STANAME'] = stations_df['STANAME'].str.strip()

    stations_table = stations_df.to_html(classes="table table-striped table-sm", index=False)
    return render_template("home.html", stations=stations_table, data=None)


@app.route("/api/v1/station-all")
def station_all():
    station = request.args.get("station")
    page = int(request.args.get("page", 1))
    per_page = 100  # rows per page

    if not station:
        return "Error: Please provide a station parameter, e.g., ?station=10", 400

    try:
        filename = f"data_small/TG_STAID{int(station):06d}.txt"
        df = pd.read_csv(filename, skiprows=20)

        # Clean and prepare data
        df.rename(columns={"    DATE": "DATE", "   TG": "TG"}, inplace=True)
        df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
        df = df[["DATE", "TG"]].copy()

        # ✅ Convert TG to degrees Celsius and format with °C
        df["TG"] = (df["TG"] / 10).map(lambda x: f"{x:.1f} °C" if pd.notnull(x) else "N/A")

        # Pagination calculations
        total_rows = len(df)
        total_pages = math.ceil(total_rows / per_page)
        start = (page - 1) * per_page
        end = start + per_page
        df_page = df.iloc[start:end]

        # Convert current page dataframe to HTML
        table = df_page.to_html(classes="table table-bordered table-sm table-responsive", index=False)

        # Prepare pages list for template
        pages = list(range(1, total_pages + 1))

    except FileNotFoundError:
        return f"Error: Data file for station {station} not found.", 404
    except Exception as e:
        return f"Error reading data: {str(e)}", 500

    return render_template(
        "station_data.html",
        station=station,
        data=table,
        page=page,
        total_pages=total_pages,
        pages=pages
    )


@app.route("/api/v1/station-date")
def station_by_year_month():
    station = request.args.get("station")
    year = request.args.get("year")
    month = request.args.get("month")
    page = int(request.args.get("page", 1))

    if not (station and year and month):
        return "Error: Please provide 'station', 'year', and 'month' parameters."

    # Read the CSV file
    filename = f"data_small/TG_STAID{int(station):06d}.txt"
    df = pd.read_csv(filename, skiprows=20)
    df.rename(columns={"   TG": "TG"}, inplace=True)
    df["DATE"] = df["    DATE"].astype(str)
    df["YEAR"] = df["DATE"].str[:4]
    df["MONTH"] = df["DATE"].str[4:6]

    # Filter by year and month
    filtered = df[(df["YEAR"] == str(year)) & (df["MONTH"] == str(month))]

    # ✅ Keep only relevant columns
    filtered = filtered[["STAID", "DATE", "TG"]].copy()

    # ✅ Convert TG to degrees Celsius and format with °C
    filtered["TG"] = (df["TG"] / 10).map(lambda x: f"{x:.1f} °C" if pd.notnull(x) else "N/A")

    # Continue with pagination
    per_page = 100
    total = len(filtered)
    total_pages = math.ceil(total / per_page)
    start = (page - 1) * per_page
    end = start + per_page

    table_html = filtered.iloc[start:end].to_html(classes="table table-sm table-bordered", index=False)

    return render_template(
        "station_date.html",
        data=table_html,
        station=station,
        station_name="",  # Optional: Add a lookup if desired
        year=year,
        month=month,
        page=page,
        pages=list(range(1, total_pages + 1)),
        total_pages=total_pages
    )


if __name__=="__main__":
    app.run(debug=True)
    #app.run(debug=True,  # port=5001 if running multiple)
