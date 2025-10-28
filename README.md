# 🌪️ Cyclone Montha: Andhra Pradesh Impact Dashboard

<p align="center">
  <!--<b>Built with</b><br>-->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white"/>
</p>

---

A **real-time, interactive dashboard** built with **Python** + **Streamlit** to track and analyse the impact of **Cyclone Montha** on 17 districts in **Andhra Pradesh**.

> 🖼️ *Note:* Replace the placeholder image below with a screenshot or GIF of your running application.

---

## 📍 Overview

This project was developed in response to **Cyclone Montha (October 2025)** to provide a single, comprehensive source of truth for its impact.  
The dashboard consolidates and visualizes key data — from storm intensity and evacuation numbers to the progress of relief and recovery efforts.

The data used is **simulated**, based on real-world reports from the India Meteorological Department (IMD) and the Andhra Pradesh State Disaster Management Authority (APSDMA).

---

## ✨ Key Features

### 📈 Multi-Tab Interface  
- **🗺️ Overview & Evacuation:** At-a-glance metrics, interactive district map, evacuation treemap.  
- **⏳ Impact Over Time:** Time-series showing storm progression, bar chart for total rainfall.  
- **🤝 Relief & Recovery:** Grouped charts tracking distribution of food/water and restoration of power/comms.

### 🛠️ Advanced Analysis Tools (Sidebar)  
- **📍 District Spotlight:** Deep-dive view of specific district.  
- **🌧️ Rainfall Filter:** Slider to filter dashboard by minimum rainfall threshold.  
- **🎨 Dark Mode:** Toggle to switch all charts between light and dark themes.

### 📊 Dynamic & Interactive  
- Visualisations built with **Plotly** (hover, zoom, pan).  
- A “Key Insights” box highlights most impacted districts.  
- “Last Updated” timestamp shows data freshness.  
- **📥 Data Download:** Users can download the full 17-district dataset as CSV from the sidebar.

---

## 💻 Tech Stack

| Component | Description |
|-----------|-------------|
| **Python**         | Core programming language |
| **Streamlit**      | Framework for interactive web app |
| **Pandas**         | Data manipulation, filtering, aggregation |
| **Plotly Express** | Rich, interactive data visualisations |
| **Matplotlib**     | Styling and fallback plots |

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ravi-kumar-chinta/cyclone-montha-dashboard.git
cd cyclone-montha-dashboard
```

### 2️⃣ Create & Activate a Virtual Environment

#### 🪟 Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### 🍎 macOS / 🐧 Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

Your default browser will open automatically at 👉 **http://localhost:8501**

---

## 🧩 Suggested Folder Structure
```
cyclone-montha-dashboard/
│
├── app.py
├── data/
│   └── cyclone_data.csv
├── assets/
│   └── images/
│       └── dashboard_preview.png
├── requirements.txt
└── README.md
```

---

## 📅 Changelog

### v1.0.0
- Initial release of the Cyclone Montha Dashboard  
- Implemented all three tabs (Overview, Impact, Relief)  
- Added CSV download, dark mode, rainfall filter  

### v1.1.0 (Upcoming)
- Real-time data integration from IMD APIs  
- Enhanced visual themes  
- Deployment to Streamlit Cloud or AWS  

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature-new-section
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Added new chart for district impact"
   ```
4. **Push to your branch**
   ```bash
   git push origin feature-new-section
   ```
5. **Open a Pull Request**

---

## 📞 Contact

<p align="left">
  <b>Author:</b> Ravi Kumar Chinta<br><br>
  <a href="mailto:chintharavikumar9908@gmail.com">
    <img src="https://img.shields.io/badge/Email-chintharavikumar9908%40gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
  <a href="https://www.linkedin.com/in/chinta-ravi-kumar-a0a763280">
    <img src="https://img.shields.io/badge/LinkedIn-Chinta%20Ravi%20Kumar-blue?style=for-the-badge&logo=linkedin"/>
  </a>
  <a href="https://github.com/ravi-kumar-chinta/cyclone-montha-dashboard">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github"/>
  </a>
</p>


---

## 🙌 Acknowledgements
- India Meteorological Department (IMD)  
- Andhra Pradesh State Disaster Management Authority (APSDMA)  
- Streamlit, Pandas, and Plotly teams for their open-source contributions  
- All testers and community members who supported this dashboard  

---

## ⚠️ Disclaimer

> This project is created **strictly for educational and research purposes only**.  
> It uses **simulated or public data** and should **not be used for any emergency decision-making, real-time forecasting, or misuse** of disaster information.  
> The author is **not responsible for any improper use** or misinterpretation of the data or code.  

---

## 💖 Thanks for Visiting!

<p align="center">
  <b>⭐ If you found this project helpful, consider giving it a star on GitHub! ⭐</b><br>
  <em>Developed with ❤️ by Ravi Kumar Chinta</em>
</p>
