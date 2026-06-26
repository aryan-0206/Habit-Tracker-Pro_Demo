# ⚡ Habit Tracker Pro

<p align="center">
  <img src="static/img/logo.svg" alt="HabitPro Logo" width="120px" height="120px">
</p>

<h3 align="center">Habit Tracker Pro</h3>

<p align="center">
  A premium, high-performance dark-themed web application designed to help you track daily habits, visualizes streaks, and analyze completion metrics in real time.
</p>

<p align="center">
  <a href="https://github.com/aryan-0206/Habit-Tracker-Pro/blob/main/LICENSE"><img src="https://img.shields.io/github/license/aryan-0206/Habit-Tracker-Pro?style=for-the-badge&color=22c55e" alt="License"></a>
  <img src="https://img.shields.io/badge/PRs-welcome-3b82f6?style=for-the-badge" alt="PRs Welcome">
  <img src="https://img.shields.io/badge/Platform-Render-ec4899?style=for-the-badge" alt="Platform">
</p>

---

## 🔗 Live Application Link

🚀 **Access the live web application here:**  
👉 **[Habit Tracker Pro — Live on Render 🚀](https://habit-tracker-pro-1-a51y.onrender.com)** 👈

---

## ✨ Features

🎨 **Premium Glassmorphic Theme**
- Harmonious, dark-mode color scheme styled with vibrant HSL colors (neon greens, cyan, blue, pink, and orange).
- Premium blurred glass components and custom smooth hover interactions.

🗂️ **Split Screen Architecture**
- **Dashboard View:** Dedicated purely to your habit tracking, keeping the core screen clean and fast.
- **Analytics View:** Hosts visual graphs, KPI counters, and a detailed breakdown table.

🔥 **Streak & Habit Insights**
- Dynamic streak calculations showing your current consecutive days of completion.
- Automated completion rates calculated for the selected month.
- Sleek progress bars colored dynamically based on performance (green for excellent, orange/blue for on-track, red for needs focus).

📊 **Interactive Charting**
- **Daily Trend:** A smooth line chart displaying habit completion trends over the days of the month.
- **Weekly Performance:** A bar chart tracking success across the 5 weeks of the month.
- **Progress Overview:** A modern cutout doughnut chart visualizing completed vs. remaining tasks.

📱 **Responsive Touch Optimizations**
- Designed first for mobile and tablet devices.
- Checkbox tap targets enlarged to `26px` with custom column widths for effortless touch interaction.
- Smooth horizontal swipe-scrolling for month-wide grids.

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite (file-based database with environment path overrides for persistence)
- **Frontend:** Vanilla JS (ES6+), Bootstrap 5, custom CSS variables
- **Visuals:** Chart.js, Google Fonts (Plus Jakarta Sans)
- **Deployment:** Render-ready with gunicorn and persistence configurations

---

## 📂 Project Structure

```plaintext
Habit-Tracker-Pro/
├── app.py              # Main Flask web application & api endpoints
├── database.py         # SQLite connection setup & database initializer
├── requirements.txt    # Python production dependencies list
├── Procfile            # Render deployment runner configuration
├── index.html          # Static HTML mirror
├── templates/
│   └── index.html      # Dynamic Flask application entry point
├── static/
│   ├── css/
│   │   └── style.css   # Main glassmorphic styling sheet & media queries
│   ├── js/
│   │   └── app.js      # App state management, analytics, & chart updates
│   └── img/
│       └── logo.svg    # HabitPro vector icon
├── LICENSE             # Open-source MIT license terms
├── .gitignore          # Version control file exclusions
└── TODO.md             # Development checklist
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/habits` | Retrieve all active habits |
| `POST` | `/api/habits` | Create and insert a new habit |
| `DELETE` | `/api/habits/<id>` | Delete a habit and its completed log history |
| `POST` | `/api/habits/clear` | Clear all habits and logs (Reset DB) |
| `GET` | `/api/logs/<year>/<month>` | Retrieve completion logs for a given month |
| `POST` | `/api/toggle` | Toggle habit completion status for a date |
| `GET` | `/api/stats/<year>/<month>` | Retrieve dashboard summary stats and chart data |

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/aryan-0206">Aryan</a>
</p>

