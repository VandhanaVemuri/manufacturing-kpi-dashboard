from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route("/")
def dashboard():

    # Load data
    df = pd.read_csv("data/production_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])

    # KPIs
    total_production = df["Units_Produced"].sum()
    defect_rate = round(df["Defective_Units"].sum() / df["Units_Produced"].sum() * 100, 2)
    total_downtime = df["Downtime_Minutes"].sum()

    df["Efficiency"] = (df["Units_Produced"] - df["Defective_Units"]) / df["Units_Produced"]
    avg_efficiency = round(df["Efficiency"].mean() * 100, 2)

    # Chart 1: Daily Production
    daily_production = df.groupby("Date")["Units_Produced"].sum().reset_index()
    fig1 = px.line(daily_production, x="Date", y="Units_Produced",
                   title="Daily Production Output")
    graph1 = pio.to_html(fig1, full_html=False)

    # Chart 2: Defect Rate by Line
    defect_by_line = df.groupby("Production_Line").apply(
        lambda x: x["Defective_Units"].sum() / x["Units_Produced"].sum()
    ).reset_index(name="Defect_Rate")

    fig2 = px.bar(defect_by_line, x="Production_Line",
                  y="Defect_Rate",
                  title="Defect Rate by Production Line")
    graph2 = pio.to_html(fig2, full_html=False)

    # Chart 3: Inventory Trend
    inventory_trend = df.groupby("Date")["Inventory_Level"].mean().reset_index()
    fig3 = px.line(inventory_trend, x="Date",
                   y="Inventory_Level",
                   title="Inventory Trend")
    graph3 = pio.to_html(fig3, full_html=False)

    # Chart 4: Downtime by Line
    downtime_by_line = df.groupby("Production_Line")["Downtime_Minutes"].sum().reset_index()
    fig4 = px.bar(downtime_by_line, x="Production_Line",
                  y="Downtime_Minutes",
                  title="Total Downtime by Line")
    graph4 = pio.to_html(fig4, full_html=False)

    return render_template("dashboard.html",
                           total_production=total_production,
                           defect_rate=defect_rate,
                           total_downtime=total_downtime,
                           avg_efficiency=avg_efficiency,
                           graph1=graph1,
                           graph2=graph2,
                           graph3=graph3,
                           graph4=graph4)


if __name__ == "__main__":
    app.run(debug=True)
