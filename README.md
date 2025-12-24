# Home Room Temperature Monitoring SCADA System

This project is a **Home Room Temperature Monitoring System** built using an IoT sensor and a SCADA-style dashboard.  
It continuously monitors the room temperature and displays the readings in real-time, allowing users to observe temperature trends, log historical data, and trigger alerts when limits are exceeded.

---

## 🔥 Key Features
- Real-time room temperature monitoring
- Live dashboard (SCADA-style visualization)
- Data logging for history and trend analysis
- Upper and lower temperature alert thresholds
- Modular code — easy to extend
- Lightweight and simple architecture

---

## 🧠 System Architecture (Concept)
**Sensor → Microcontroller → Python App → Dashboard + Data Log**

1. A temperature sensor reads room temperature  
2. Data is sent to a microcontroller (e.g., Arduino / ESP32)  
3. The PC receives the data via Serial (USB)  
4. A Python program:
   - Reads the sensor value
   - Logs the data
   - Displays real-time graphs (SCADA-style)

---

## 🛠️ Technologies Used
- **Hardware**
  - Temperature Sensor (e.g., DHT11 / LM35 / DS18B20)
  - Arduino / ESP32 / Similar board
- **Software**
  - Python 3
  - Matplotlib (graph)
  - CSV logging
  - PySerial library
- **GitHub**
  - Version control + documentation

---

## 📂 Project Structure

