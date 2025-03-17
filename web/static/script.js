function createItem() {
    let itemId = document.getElementById("itemId").value;
    let name = document.getElementById("itemName").value;
    let price = document.getElementById("itemPrice").value;

    fetch(`/items/${itemId}?name=${name}&price=${price}`, { method: "POST" })
        .then(response => response.json())
        .then(data => alert(data.message));
}

function getAllItems() {
    fetch(`/items`)
        .then(response => response.json())
        .then(data => document.getElementById("allItems").innerText = JSON.stringify(data, null, 2));
}

function getItem() {
    let itemId = document.getElementById("getItemId").value;

    fetch(`/items/${itemId}`)
        .then(response => response.json())
        .then(data => document.getElementById("getResult").innerText = JSON.stringify(data, null, 2));
}

function updateItem() {
    let itemId = document.getElementById("updateItemId").value;
    let name = document.getElementById("updateItemName").value;
    let price = document.getElementById("updateItemPrice").value;

    fetch(`/items/${itemId}?name=${name}&price=${price}`, { method: "PUT" })
        .then(response => response.json())
        .then(data => alert(data.message));
}

function deleteItem() {
    let itemId = document.getElementById("deleteItemId").value;

    fetch(`/items/${itemId}`, { method: "DELETE" })
        .then(response => response.json())
        .then(data => alert(data.message));
}
