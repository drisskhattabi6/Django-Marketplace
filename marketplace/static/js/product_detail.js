
let increaseBtn = document.getElementById('increase-btn');
let decreaseBtn = document.getElementById('decrease-btn');
let counterInput = document.getElementById('counter-input');

function increaseCounter() {
    if (counterInput.value == 100) return
    counterInput.value++;
    console.log("+");
}

function decreaseCounter() {
    if (counterInput.value == 1) return
    counterInput.value--;
    console.log("-");
}

increaseBtn.addEventListener('click', increaseCounter);
decreaseBtn.addEventListener('click', decreaseCounter);

// ---------------------------------------

document.addEventListener('DOMContentLoaded', function() {
    const mainImage = document.getElementById('main-image');
    const thumbnails = document.querySelectorAll('.thumbnail');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            mainImage.src = this.src;
            
            thumbnails.forEach(thumbnail2 => {thumbnail2.classList.remove('selected-img')});

            thumbnail.classList.add('selected-img');
        });
    });
});

// ---------------------------------------
