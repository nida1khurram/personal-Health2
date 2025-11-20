run
uv run streamlit run main.py

## Application Overview

Your Personal Health Record Dashboard is a web application built with Python and Streamlit, designed for tracking, visualizing, and managing personal health data.

**Key Features:**

*   **Secure User Authentication:** Supports multi-user registration and login using email and password, with credentials securely stored and session management handled by `streamlit-authenticator`.
*   **Personalized Health Record Management:** Users can add daily health records including Blood Pressure, Sugar Level, Pulse Rate, and Notes, now with precise **date and time** entries.
*   **User-Specific Data Storage:** All health records are securely stored in separate, dedicated files for each user (`data/<username>/health_records.csv`), ensuring data privacy and organization.
*   **Interactive Data Visualization:** View health trends over time through interactive charts for Blood Pressure, Sugar Level, and Pulse Rate.
*   **Health Analytics & Insights:** Access key statistics, BMI calculation with recommendations, and basic checks for out-of-range values.
*   **Smart Health Recommendations:** Receive personalized health advice based on your recorded data trends, displayed directly in the app.
*   **Professional PDF Reports:** Generate and download detailed PDF reports summarizing selected health data, which now prominently display the logged-in **username** and include **time** alongside the date for each record.
*   **Clean and Intuitive User Interface:** Features a prominent app name and a streamlined user experience for login and registration.

**Tech Stack:**

*   **Language:** Python 3.11+
*   **Framework:** Streamlit
*   **Data Handling:** Pandas
*   **Visualization:** Plotly Express (and potentially Matplotlib/Seaborn)
*   **PDF Generation:** FPDF2
*   **Authentication:** Streamlit-Authenticator

This app serves as a comprehensive digital health diary, offering users intelligent tools to monitor their well-being effectively.
