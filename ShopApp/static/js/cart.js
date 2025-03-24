document.addEventListener("DOMContentLoaded", function () {
  attachEventListeners();
});

function handleAddToCart(e) {
  e.preventDefault();

  console.log("Add to Cart Clicked!");

  let productId = this.dataset.product;
  console.log("Product ID:", productId, "Action: add");

  this.disabled = true;
  updateCart(productId, "add");
}

function handleCartUpdate(e) {
  e.preventDefault();
  let productId = this.dataset.product;
  let action = this.dataset.action;

  console.log(
    "Cart update clicked - Product ID:",
    productId,
    "Action:",
    action
  );

  this.disabled = true;
  updateCart(productId, action);
}

function attachEventListeners() {
  let addToCartBtns = document.querySelectorAll(".add-to-cart");
  let updateCartBtns = document.querySelectorAll(".update-cart");

  addToCartBtns.forEach((btn) => {
    btn.removeEventListener("click", handleAddToCart);
    btn.addEventListener("click", handleAddToCart);
  });

  updateCartBtns.forEach((btn) => {
    btn.removeEventListener("click", handleCartUpdate);
    btn.addEventListener("click", handleCartUpdate);
  });
}

function updateCart(productId, action) {
  let checkUser = document.getElementById("checking");
  if (!checkUser || checkUser.dataset.auth !== "true") {
    // alert("Login fist bro to Inorder to buy phone");
    Swal.fire({
      title: "Login Required",
      text: "You need to log in to continue.",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#d33",
      cancelButtonColor: "#3085d6",
      confirmButtonText: "Yes, Login",
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = "/login/";
      }
    });

    return;
  }

  console.log(
    "Sending AJAX request... Product ID:",
    productId,
    "Action:",
    action
  );

  let url = "/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to update cart");
      }
      return response.json();
    })
    .then((data) => {
      document.querySelector(
        ".price_cart_total"
      ).innerText = `$${data.cart_total}`;

      console.log("Cart updated successfully:", data);
      document.querySelector(
        ".cart-title"
      ).innerText = `(${data.cart_quantity} Items in Cart)`;
      document.querySelector(".count_item").innerText = data.cart_quantity;

      viewCart(data.cart_items);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function viewCart(cartItems) {
  console.log("Updating cart in DOM:", cartItems);

  let cartContainer = document.querySelector(".demi");
  cartContainer.innerHTML = "";

  if (!cartItems || cartItems.length === 0) {
    cartContainer.innerHTML = `<p class="empty-cart">Your cart is empty.</p>`;
    return;
  }

  cartItems.forEach((item) => {
    cartContainer.innerHTML += `
            <div class="cart-info" data-id="${item.id}">
                <div class="cart-img">
                    <img src="${item.image}" alt="${item.name}" />
                </div>
                <div class="cart-detail">
                    <h3>${item.name}</h3>
                    <div class="price">
                        <span>$${item.price}</span>
                    </div>
                    <div class="btn">
                        <button class="update-cart" data-product="${item.id}" data-action="remove">-</button>
                        <span>${item.quantity}</span>
                        <button class="update-cart" data-product="${item.id}" data-action="add">+</button>
                    </div>
                </div>
              
            </div>
        `;
  });
  attachEventListeners();
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");

    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
