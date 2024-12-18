fetch("https://api.weather.gov/gridpoints/PQR/113,104/forecast")
	.then(response => response.json())
	.then(data => console.log(data))
