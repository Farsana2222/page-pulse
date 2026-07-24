async function analyzeWebsite() {

    let url = document.getElementById("urlInput").value.trim();

    const loading = document.getElementById("loading");
    const result = document.getElementById("result");

    if (url === "") {
        alert("Please enter a website URL.");
        return;
    }

    loading.style.display = "block";
    result.innerHTML = "";

    try {

        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();

        loading.style.display = "none";

        if (data.error) {

            result.innerHTML = `
            <div class="card">
                <h2>❌ Error</h2>
                <p>${data.error}</p>
            </div>
            `;

            return;
        }

        const statusColor =
            data.status === 200 ? "green" :
            data.status === 404 ? "red" :
            "orange";

        result.innerHTML = `
        <div class="card">

        <h2>📊 Audit Report</h2>

        <p><strong>🔗 URL:</strong> ${data.url}</p>

        <p><strong>Status:</strong>
        <span style="color:${statusColor};font-weight:bold;">
        ${data.status}
        </span>
        </p>

        <p>⚡ <strong>Response Time:</strong> ${data.response_time}</p>

        <p>📄 <strong>Title:</strong> ${data.title}</p>

        <p>📝 <strong>Meta Description:</strong> ${data.meta_description}</p>

        <p>📰 <strong>H1 Tags:</strong> ${data.h1_count}</p>

        <p>🖼️ <strong>Total Images:</strong> ${data.total_images}</p>

        <p>⚠️ <strong>Images Missing Alt:</strong> ${data.missing_alt}</p>

        <p>📚 <strong>Word Count:</strong> ${data.word_count}</p>

        <button onclick="copyReport()">📋 Copy Report</button>

        </div>
        `;
    }

    catch (error) {

        loading.style.display = "none";

        result.innerHTML = `
        <div class="card">
            <h2>❌ Error</h2>
            <p>Unable to connect to the server.</p>
        </div>
        `;
    }
}

function copyReport() {

    const text = document.getElementById("result").innerText;

    navigator.clipboard.writeText(text);

    alert("Report copied successfully!");
}