$(document).ready(function () {
  // Get user's geolocation
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(async function (position) {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      const apiKey = "465ad6304f12419481b476deed2c4188";
      const url = `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&exclude=current,minutely,hourly&appid=${apiKey}&units=metric`;

      try {
        const response = await fetch(url);
        const data = await response.json();
        console.log("Weather data:", data);

        const dailyData = data.daily.slice(1, 8); // Get weather data for the next 7 days

        // Extract labels (dates) and temperatures from the data
        const labels = dailyData.map((day) =>
          new Date(day.dt * 1000).toLocaleDateString()
        );
        const temperatures = dailyData.map((day) => day.temp.day);

        // Create a line chart
        const ctx = document.getElementById("weather-chart").getContext("2d");
        new Chart(ctx, {
          type: "line",
          data: {
            labels: labels,
            datasets: [
              {
                label: "Temperature (°C)",
                data: temperatures,
                borderColor: "rgba(75, 192, 192, 1)",
                backgroundColor: "rgba(75, 192, 192, 0.2)",
                borderWidth: 1,
              },
            ],
          },
          options: {
            scales: {
              y: {
                beginAtZero: false,
              },
            },
          },
        });
      } catch (error) {
        console.error("Error fetching weather data:", error);
        $("#weather-chart").html(
          '<div class="alert alert-info" role="alert">Failed to fetch weather data.</div>'
        );
      }
    });
  } else {
    $("#weather-chart").html(
      '<div class="alert alert-warning" role="alert">Geolocation is not supported by your browser.</div>'
    );
  }
});
