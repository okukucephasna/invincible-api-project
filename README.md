## 🧩 Project Overview

This is a **simple full-stack project** that leverages **Flask**, **Flask-RESTful**, **PostgreSQL**, and **React** to create an API-driven application.
The backend is powered by Flask and serves data from a PostgreSQL database, while the frontend (built with React) consumes the API endpoints to display content dynamically.

---

## ⚙️ Step 1: Installing React on the Frontend

The first step is to set up a React project in the frontend directory.
React provides the user interface and will fetch data from the Flask API.

You can initialize it by running:

```bash
npx create-react-app frontend
```

This command creates a new folder called `frontend` containing all the necessary files to start a React project.

<img width="776" height="375" alt="Installing React on the frontend" src="https://github.com/user-attachments/assets/43e47313-2c7b-4103-9f45-3becdbd9afb9" />

---

## ⚙️ Step 2: Installing Axios

Next, install **Axios**, a popular JavaScript library used for making HTTP requests.
It allows the frontend to send and receive data from the Flask backend seamlessly.

Run this command inside your frontend folder:

```bash
npm install axios
```

<img width="508" height="192" alt="Installing Axios in the frontend" src="https://github.com/user-attachments/assets/0de44ed1-68ba-44bc-b8e8-11a2e7bbcd61" />

---

## ⚙️ Step 3: Installing React Router DOM

After setting up Axios, install **React Router DOM** — a routing library that enables page navigation in React applications without refreshing the browser.

Use the command below:

```bash
npm install react-router-dom
```

This will allow you to create routes for different pages, such as Home, About, or specific content pages fetched from the API.

<img width="520" height="195" alt="Installing React Router DOM" src="https://github.com/user-attachments/assets/0f75a560-75bd-43a2-932e-6b74d0315b0a" />

---

## ⚙️ Step 4: Building the Frontend for Integration

Once the React app is ready and configured, you need to **build** it so that Flask can serve the static files (the compiled frontend) when the backend runs.

Run:

```bash
npm run build
```

This generates a production-ready build of your React app in the `frontend/build` folder.
When you start your Flask backend, it will automatically serve this built frontend, allowing both parts of the project to run together smoothly.

<img width="512" height="221" alt="Building React and removing Git from the frontend" src="https://github.com/user-attachments/assets/4d35b35e-c387-4a56-9018-7c46be3cfa17" />

---

Would you like me to add a short **introduction paragraph and conclusion** (so it reads like a professional GitHub RE
