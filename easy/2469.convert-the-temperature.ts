function convertTemperature(celsius: number): number[] {
    let kelvin = celsius + 273.15;
    let fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]
};

console.log(convertTemperature(36.50))