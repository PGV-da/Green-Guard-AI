async function getWeather() {
  const city = document.getElementById("cityInput").value;
  const apiKey = "eabbae4fff449239cbed098c5b2d2952";
  const url = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);

    displayWeather(data);
  } catch (error) {
    console.error("Error fetching weather data:", error);
  }
}

function displayWeather(data) {
  const weatherContainer = document.getElementById("weatherContainer");
  weatherContainer.innerHTML = `
      <h3>${data.city.name}, ${data.city.country}</h3>
      <p>Temperature: ${data.list[0].main.temp}°C</p>
      <p>Weather: ${data.list[0].weather[0].description} <i class="wi wi-owm-${data.list[0].weather[0].id}"></i></p>
      <p>Humidity: ${data.list[0].main.humidity}%</p>
      <p>Wind Speed: ${data.list[0].wind.speed} m/s</p>
  `;

  const threeDayTemps = [[], [], []];

  data.list.forEach((item) => {
    const date = new Date(item.dt * 1000);
    const dayIndex = date.getDate() - new Date().getDate(); // 0 for today, 1 for tomorrow, 2 for the day after tomorrow
    if (dayIndex >= 0 && dayIndex <= 2) {
      threeDayTemps[dayIndex].push(item.main.temp);
    }
  });

  const averageTemps = threeDayTemps.map((dayTemps) => {
    const total = dayTemps.reduce((acc, temp) => acc + temp, 0);
    return total / dayTemps.length;
  });

  const ctx = document.getElementById("weatherChart").getContext("2d");
  const chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: ["Today", "Tomorrow", "Day after Tomorrow"],
      datasets: [
        {
          label: "Average Temperature (°C)",
          data: averageTemps,
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
          fill: false,
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
}
