let circle = document.querySelector('.circle')


function setPosition() {
    circle.style.position = 'absolute';
    circle.style.top=0;
    circle.style.left=0;
}
window.addEventListener('load', setPosition)



window.addEventListener('keyup',function(e) {
    console.log(e)
    switch(e.key){
        case 'ArrowLeft':
            circle.style.left = parseInt(circle.style.left) - 10 + 'px'
            break;
        case 'ArrowRight':
            circle.style.left = parseInt(circle.style.left) + 10 + 'px'
            break;
        case 'ArrowUp':
            circle.style.top = parseInt(circle.style.top) - 10 + 'px'
            break;    
        case 'ArrowDown':
            circle.style.top = parseInt(circle.style.top) + 10 + 'px'
            break;    
    }
})