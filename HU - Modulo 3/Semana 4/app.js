// ====== REFERENCIAS AL DOM ======
const form = document.getElementById("productForm");
const productList = document.getElementById("productList");
const message = document.getElementById("message");
const syncBtn = document.getElementById("syncBtn");

// ====== CONFIG ======
const API_URL = "http://localhost:3001/products";
let products = [];

// ====== MENSAJES ======
const showMessage = (text) => {
  message.textContent = text;
  setTimeout(() => (message.textContent = ""), 3000);
};

// ====== RENDER ======
const renderProducts = () => {
  productList.innerHTML = "";

  products.forEach(product => {
    const li = document.createElement("li");
    li.textContent = `${product.name} - $${product.price}`;

    const btn = document.createElement("button");
    btn.textContent = "Eliminar";

    btn.addEventListener("click", async () => {
      await fetch(`${API_URL}/${product.id}`, { method: "DELETE" });
      products = products.filter(p => p.id !== product.id);
      renderProducts();
    });

    li.appendChild(btn);
    productList.appendChild(li);
  });
};

// ====== GET ======
const fetchProducts = async () => {
  try {
    const res = await fetch(API_URL);
    products = await res.json();
    renderProducts();
  } catch (error) {
    console.error("Error GET:", error);
  }
};

// ====== POST ======
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const price = document.getElementById("price").value;

  if (!name || price <= 0) {
    showMessage("Datos inválidos");
    return;
  }

  const newProduct = { name, price };

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newProduct)
    });

    const saved = await res.json();
    products.push(saved);
    renderProducts();
    form.reset();
  } catch (error) {
    console.error("Error POST:", error);
  }
});

// ====== BOTÓN SYNC ======
syncBtn.addEventListener("click", fetchProducts);

// ====== INIT ======
fetchProducts();

