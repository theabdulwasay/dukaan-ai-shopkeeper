let cart = {}; // { productId: { id, name, price, qty, maxStock } }

function renderCart() {
  const linesEl = document.getElementById('cartLines');
  const items = Object.values(cart);
  if (items.length === 0) {
    linesEl.innerHTML = '<p id="emptyCart" style="opacity:0.6;">Cart is empty.</p>';
  } else {
    linesEl.innerHTML = items.map(item => `
      <div class="cart-line">
        <span>${item.name}<br><small>Rs. ${item.price.toFixed(2)} each</small></span>
        <span class="qty-controls">
          <button type="button" onclick="changeQty(${item.id}, -1)">-</button>
          <strong style="margin:0 8px;">${item.qty}</strong>
          <button type="button" onclick="changeQty(${item.id}, 1)">+</button>
        </span>
      </div>
    `).join('');
  }
  const total = items.reduce((sum, item) => sum + item.qty * item.price, 0);
  document.getElementById('cartTotal').textContent = total.toFixed(2);
  document.getElementById('cartJson').value = JSON.stringify(
    items.map(item => ({ id: item.id, qty: item.qty }))
  );
}

function addToCart(id, name, price, maxStock) {
  if (cart[id]) {
    if (maxStock === 0 || cart[id].qty < maxStock) cart[id].qty += 1;
  } else {
    cart[id] = { id, name, price, qty: 1, maxStock };
  }
  renderCart();
}

function changeQty(id, delta) {
  if (!cart[id]) return;
  cart[id].qty += delta;
  if (cart[id].qty <= 0) {
    delete cart[id];
  } else if (cart[id].maxStock > 0 && cart[id].qty > cart[id].maxStock) {
    cart[id].qty = cart[id].maxStock;
  }
  renderCart();
}

document.getElementById('productSearch').addEventListener('input', (e) => {
  const term = e.target.value.toLowerCase();
  document.querySelectorAll('.product-pick').forEach(el => {
    el.style.display = el.dataset.name.includes(term) ? 'flex' : 'none';
  });
});

document.getElementById('checkoutForm').addEventListener('submit', (e) => {
  if (Object.keys(cart).length === 0) {
    e.preventDefault();
    alert('Please add at least one product to the cart.');
  }
});

renderCart();
