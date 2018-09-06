# Write your MySQL query statement below
SELECT weather_a.Id FROM Weather AS weather_a
    INNER JOIN Weather AS weather_b 
    ON weather_a.Temperature > weather_b.Temperature
   AND weather_a.RecordDate = date_add(weather_b.RecordDate, interval 1 day);