const listItems = document.querySelector(".table-items");
const messageBox = document.querySelector(".message-box");

async function getItems() {
    return fetch("/get-product/").then((res) => res.json())
}

async function showItems() {
    listItems.innerHTML = '';
    let output = "";
    const items = await getItems()
    items.forEach(item => {
        output += `
        <div class="row list-items justify-content-center">
            <div class="col-3 mepet">
                    <p class="border-minecraft mepet fs-5">${item.fields.name}</p>
                </div>
                <div class="col-1 mepet">
                    <p class="border-minecraft mepet fs-5">${item.fields.amount}</p>
                </div>
                <div class="col-4 mepet">
                    <p class="border-minecraft mepet fs-5">${item.fields.description}</p>
                </div>
                <div class="col-1 p-0" >
                    <button onclick="deleteItem(${item.pk});" class="button-minecraft lebar-max">Delete</button>
                </div>
                <div class="col-1 p-0" >
                    <button onclick="editItem()" class="button-minecraft lebar-max">Edit</button>
                </div>
                <div class="col-1 p-0">
                    <button onclick="plusItem(${item.pk});" class="button-minecraft lebar-max">+</button>       
                </div>
                <div class="col-1 p-0">
                    <button onclick="minItem(${item.pk});" class="button-minecraft lebar-max">-</button>
                </div>
            </div>
        </div>
    `;
    });
    listItems.innerHTML = output;
}

showItems()

async function addProduct() {
    fetch("/create-ajax/", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    })
    .then(res => res.json())
    .then(data =>{
        if (data.success){
            showItems();
            messageBox.innerHTML = `
            <p class="text-center">${data.message}<p>
            `;
        }
    })
    document.getElementById("form").reset()
    return false
}

document.getElementById("button_add").onclick = addProduct

async function plusItem(itemId) {
    fetch("/tambah_item/"+itemId+"/", {
    }).then(showItems)
}

function minItem(itemId) {
    fetch("/kurang_item/"+itemId+"/", {
    }).then(showItems)
}

async function deleteItem(itemId) {
    fetch("/delete-item-ajax/"+itemId+"/", {
        method: "DELETE"
    })
    .then(res => res.json())
    .then(data =>{
        if (data.success){
            showItems();
            messageBox.innerHTML = `
            <p class="text-center">${data.message}<p>
            `;
        }
    })
    
}