$(document).ready(function () {
  const chartContainer = $("#weather-chart");

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      async function (position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        const apiKey = "465ad6304f12419481b476deed2c4188";
        const url = `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&exclude=current,minutely,hourly,alerts&appid=${apiKey}&units=metric`;

        chartContainer.html('<p class="text-muted">Loading upcoming weather...</p>');

        try {
          const response = await fetch(url);
          const data = await response.json();

          const dailyData = data.daily.slice(1, 8); // Next 7 days

          const labels = dailyData.map((day) =>
            new Date(day.dt * 1000).toLocaleDateString()
          );
          const temperatures = dailyData.map((day) => day.temp.day);

          // Clear container and draw chart
          chartContainer.html('<canvas id="weatherChartCanvas"></canvas>');
          const ctx = document.getElementById("weatherChartCanvas").getContext("2d");

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
                  borderWidth: 2,
                  fill: true,
                  tension: 0.3,
                },
              ],
            },
            options: {
              responsive: true,
              plugins: {
                title: {
                  display: true,
                  text: "7-Day Temperature Forecast",
                  font: { size: 18 }
                }
              },
              scales: {
                y: {
                  beginAtZero: false,
                  title: {
                    display: true,
                    text: "Temperature (°C)"
                  }
                },
                x: {
                  title: {
                    display: true,
                    text: "Date"
                  }
                }
              },
            },
          });
        } catch (error) {
          console.error("Error fetching weather data:", error);
          chartContainer.html(
            '<div class="alert alert-danger" role="alert">Failed to fetch weather data. Please try again later.</div>'
          );
        }
      },
      function (error) {
        let message = "Unable to access your location.";
        if (error.code === 1) message = "Please allow location access to view weather forecasts.";
        else if (error.code === 2) message = "Location unavailable.";
        else if (error.code === 3) message = "Location request timed out.";

        chartContainer.html(
          `<div class="alert alert-warning" role="alert">${message}</div>`
        );
      }
    );
  } else {
    chartContainer.html(
      '<div class="alert alert-warning" role="alert">Geolocation is not supported by your browser.</div>'
    );
  }
});
