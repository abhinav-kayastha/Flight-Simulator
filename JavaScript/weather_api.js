const apiKey = "40c87dc6bc79464a367a089991c33997";

const cityName = "Helsinki";

const url = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}&units=metric`;

// Function to fetch weather data from OpenWeather API
const fetchWeatherData = async () => {
  try {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};

fetchWeatherData();