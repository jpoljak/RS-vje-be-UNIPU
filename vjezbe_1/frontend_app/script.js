// Nakon deploymenta backenda ovdje upiši njegov Render URL (bez završne kose crte)
const API_URL = "http://localhost:8000";

const statusEl = document.getElementById("status");
const listEl = document.getElementById("list");
const errorEl = document.getElementById("error");

async function request(path, options) {
  const res = await fetch(API_URL + path, options);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

async function checkHealth() {
  try {
    const data = await request("/health");
    statusEl.textContent = data.status;
  } catch {
    statusEl.textContent = "nedostupan";
  }
}

async function loadItems() {
  try {
    const items = await request("/items");
    listEl.innerHTML = "";
    for (const item of items) {
      const li = document.createElement("li");
      li.textContent = item.name;
      const btn = document.createElement("button");
      btn.textContent = "Obriši";
      btn.onclick = async () => {
        await request(`/items/${item.id}`, { method: "DELETE" });
        loadItems();
      };
      li.appendChild(btn);
      listEl.appendChild(li);
    }
    errorEl.textContent = "";
  } catch (e) {
    errorEl.textContent = "Greška pri dohvatu: " + e.message;
  }
}

document.getElementById("form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const input = document.getElementById("name");
  try {
    await request("/items", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: input.value }),
    });
    input.value = "";
    loadItems();
  } catch (err) {
    errorEl.textContent = "Greška pri dodavanju: " + err.message;
  }
});

checkHealth();
loadItems();
