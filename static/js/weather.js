$(document).ready(function () {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;

        $.getJSON(
          "https://api.weatherapi.com/v1/current.json?key=972be9a2469c4754835105331242102&q=" +
            lat +
            "," +
            lon,
          function (data) {
            var current = data.current;
            var location = data.location;
            var condition = current.condition;

            var weatherIcon = '<i class="fas fa-sun"></i>';
            switch (condition.code) {
              case 1000:
                weatherIcon = '<i class="fas fa-sun"></i>';
                break;
              case 1003:
              case 1006:
              case 1009:
                weatherIcon = '<i class="fas fa-cloud-sun"></i>';
                break;
              case 1030:
                weatherIcon = '<i class="fas fa-smog"></i>';
                break;
              case 1063:
              case 1180:
              case 1183:
              case 1186:
                weatherIcon = '<i class="fas fa-cloud-showers-heavy"></i>';
                break;
              case 1066:
              case 1210:
              case 1213:
              case 1216:
              case 1219:
              case 1222:
              case 1225:
              case 1255:
                weatherIcon = '<i class="fas fa-snowflake"></i>';
                break;
              case 1069:
              case 1072:
              case 1150:
              case 1153:
              case 1168:
              case 1171:
                weatherIcon = '<i class="fas fa-cloud-rain"></i>';
                break;
            }

            $("#weather-icon").html(
              '<div class="weather-icon">' + weatherIcon + "</div>"
            );
            $("#weather-details").html(
              '<div class="weather-details">' +
                "<h2>" +
                location.name +
                ", " +
                location.region +
                "</h2>" +
                "<p>Temperature: " +
                current.temp_c +
                "°C</p>" +
                "<p>Humidity: " +
                current.humidity +
                "%</p>" +
                "<p>Wind Speed: " +
                current.wind_kph +
                " km/h</p>" +
                "<p>Condition: " +
                condition.text +
                "</p>" +
                "</div>"
            );
          }
        ).fail(function (jqxhr, textStatus, error) {
          console.error("Request Failed: " + textStatus + ", " + error);
          $("#weather-details").html(
            '<div class="alert alert-danger" role="alert">Weather data fetch failed. Please try again later.</div>'
          );
        });
      },
      function (error) {
        // User denied access or an error occurred
        let message = "Unable to access location.";
        if (error.code === 1) message = "Please allow location access to get weather updates.";
        else if (error.code === 2) message = "Location unavailable.";
        else if (error.code === 3) message = "Location request timed out.";

        $("#weather-details").html(
          '<div class="alert alert-warning" role="alert">' + message + "</div>"
        );
      }
    );
  } else {
    $("#weather-details").html(
      '<div class="alert alert-warning" role="alert">Geolocation is not supported by your browser.</div>'
    );
  }
});
