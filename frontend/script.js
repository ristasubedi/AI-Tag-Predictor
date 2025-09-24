async function predict() {
    const question = document.getElementById("question").value;
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "<em>Thinking...</em>";
  
    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
      });
  
      const data = await response.json();
      const tags = data.predicted_tags;
      const difficulty = data.predicted_difficulty;
  
      if (!tags || tags.length === 0) {
        resultDiv.innerHTML = "<p>No tags predicted 😕</p>";
        return;
      }
  
      // 🧠 Show predicted difficulty at the top
      resultDiv.innerHTML = `
        <div style="margin-bottom: 20px;">
          <strong>📌 Predicted Difficulty:</strong> 
          <span style="background:#ffcc70;padding:6px 12px;border-radius:10px;color:#333;">
            ${difficulty}
          </span>
        </div>
      `;
  
      // Add predicted tags with explanations
      resultDiv.innerHTML += tags.map(tagObj => `
        <div class="result-item">
          <div class="tag-name">${tagObj.tag}</div>
          <div class="tag-description">${tagObj.explanation}</div>
          <a href="${tagObj.link}" target="_blank">Learn More →</a>
        </div>
      `).join("");
  
    } catch (error) {
      resultDiv.innerHTML = `<p style="color: #ffdddd">❌ Couldn't connect to the server.</p>`;
      console.error(error);
    }
  }
  