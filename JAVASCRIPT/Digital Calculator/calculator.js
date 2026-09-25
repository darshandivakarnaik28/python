const display = document.getElementById('display');
const numbers=document.getElementsByClassName('number');
for (let i=0;i<numbers.length;i++){
    numbers[i].addEventListener("click",function(){
        const num=numbers[i].textContent;
        display.value=num;
    });
}