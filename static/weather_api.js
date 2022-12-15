const apiKey = "794bc234d44ce063d594d5840c40263d";

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