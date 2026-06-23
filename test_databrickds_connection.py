# Databricks connection test script
# Place this file inside the workspace root so VS Code can show Databricks run options.

df=spark.sql('SELECT city_name,temperature_avg FROM samples.accuweather.forecast_daily_calendar_imperial where date = "2024-07-14"')

df.show()
