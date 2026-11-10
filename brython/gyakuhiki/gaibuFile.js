const dialog = document.getElementById("jsDialog");
const jsInput = document.getElementById("jsInput");

document.getElementById("jsSubmit").addEventListener("click", function(ev) {
    const name = jsInput.value;
    dialog.close();
    alert(`こんにちは、${name}さん！`);
});

document.getElementById("jsClose").addEventListener("click", function(ev) {
    dialog.close();
});

document.getElementById("button_02").addEventListener("click", function(ev) {
    jsInput.value = "";
    dialog.showModal();
});