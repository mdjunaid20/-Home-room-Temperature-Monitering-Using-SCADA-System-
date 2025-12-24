// Home Room Temperature Monitoring - SCADA Demo
// Simulated temperature readings
// Later replace with real sensor code if needed

float temp = 24.0;  // starting temperature in Celsius

void setup() {
  Serial.begin(9600); // initialize serial communication
}

void loop() {
  // simulate temperature change randomly
  temp += random(-5, 6) * 0.1; // -0.5°C to +0.5°C change

  // print the temperature to serial
  Serial.println(temp);

  // wait 1 second before next reading
  delay(1000);
}
