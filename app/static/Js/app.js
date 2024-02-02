// add all item to cart btn in the page
const cart = document.querySelector("#cart-btn");
if (cart) {
  cart.forEach((item) => {
    item.addEventListener("click", (e) => {
      // add item to cart
      addItemToCart(item.value);
    });
  });
}

/**
 * @function addItemToCart
 * @param {String} item
 * @returns None
 * @description this function add an item to storage
 */
function addItemToCart(item) {
  // get the current cart items
  let cart = JSON.parse(localStorage.getItem("cart")) || {};

  // check if cart has value with item as key
  if (cart.hasOwnProperty(item)) {
    // increment the cart
    cart[item]++;
  } else {
    // assign one to the cart
    cart[item] = 1;
  }

  // set the cart with the item value
  localStorage.setItem("cart", JSON.stringify(cart));

  // show the cart
  // displayCart();
  displayCart();
}

/**
 * @function removeItemfromCart
 * @param {String} item
 * @returns None
 * @description this function remove an item from storage
 */
function removeItemfromCart(cart) {
  // Get current cart object
  let cart = JSON.parse(localStorage.getItem("cart"));

  // check if the item is part of the object and the object is not empty
  if (cart.hasOwnProperty(item) && cart[item] > 1) {
    // decrement the value of the item if > 1
    cart[item] = cart[item] - 1;

    // write the current value back to the session storage
    localStorage.setItem("cart", JSON.stringify(cart));

    // this code block only run if you decrement cart to be less than 1
  } else if (cart[item] <= 1) {
    // remove object to remove item from the cart
    delete cart[item];

    // replace the cart with the new items
    localStorage.setItem("cart", JSON.stringify(cart));
  }
  // display the current cart
  displayCart();
}

/**
 * @function getCartFromStorage
 * @param {} None
 * @returns None
 * @description Return the available cart from the storage
 */
function getCartFromStorage() {
  // check if there is item in the session storage
  if (sessionStorage.length >= 0) {
    // convert the item to JSON object
    const cart_object = JSON.parse(localStorage.getItem("cart"));

    // return the value
    return cart_object;
  } else {
    // this code block run if the session storage is empty
    return "";
  }
}

/**
 * @function displayCart
 * @param {} None
 * @returns None
 * @description send the number of item in cart to page
 */
function displayCart() {
  // clear the previous cart display element
  const cart_display = document.getElementById("cart-item");
  cart_display.textContent = "";

  // get element from storage
  const cart = getCartFromStorage();

  // check if the request return empty
  if (cart != null || cart != undefined) {
    // using the object key loop throught the cart
    Object.keys(cart).forEach(function (key) {
      // check if the cart object has values
      if (Object.values(cart) != 0) {
        var sum = 0;
        // check the total number of item in the storage
        for (let i = 0; i < Object.values(cart).length; i++) {
          // sum the values
          sum += Object.values(cart)[i];
        }

        // send result to display
        const cart_display = document.getElementById("cart-item");
        cart_display.textContent = sum;
      }
    });
  }
}

// send local storage data to backend
// add url to the cart li
function send_cart_to_backend() {
  const add_href = document.getElementById('cart');
  add_href.style.cursor = 'pointer';
  add_href.addEventListener('click', () => {
    data_to_send = getCartFromStorage();
    fetch('/cart', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data_to_send),

    }).then(response => {
      if (response.redirected) {
        window.location.href = response.url;
      } else {
        response.json();
      }
    });
  })
}
/**
 * @function update_cart_from_storage
 * @param {} None
 * @returns None
 * @description render cart count to cart page
 */

function update_cart_from_storage() {
  // create an array from page url value
  let cart_uri = [];
  const cart_temp = document.querySelectorAll('#cart-uri');
}