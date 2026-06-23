df=spark.sql('SELECT country_code,temperature_avg FROM samples.accuweather.forecast_daily_calendar_imperial where date = "2024-07-14"')

df.show()