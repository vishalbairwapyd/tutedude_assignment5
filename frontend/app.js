const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
const PORT = 3000;

// Flask backend URL from environment or default localhost
const URL = process.env.BACKEND_URL || "http://localhost:5000/receive";

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json()); // Handle JSON body
app.set("view engine", "ejs");

// Route to render form (form.ejs should be in /views)
app.get("/", (req, res) => {
  res.render("form");
});

// Route to handle form submission
app.post("/submit", async (req, res) => {
  const studentData = req.body;

  try {
    // Send data to Flask backend
    const response = await axios.post(URL, studentData, {
      headers: { "Content-Type": "application/json" }
    });

    // Return JSON confirmation
    res.json({
      message: "Data Sent Successfully!",
      flaskResponse: response.data
    });
  } catch (error) {
    console.error("❌ Error sending data to Flask:", error.message);
    res.status(500).json({
      message: "Error sending data to Flask",
      error: error.message
    });
  }
});

// Start Express server
app.listen(PORT, () => {
  console.log(`✅ Express server running on http://localhost:${PORT}`);
  console.log(`🔗 Connected to Flask backend at: ${URL}`);
});
