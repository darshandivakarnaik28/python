const display = document.getElementById('display');
const numbers=document.getElementsByClassName('number');
for (let i=0;i<numbers.length;i++){
    numbers[i].addEventListener("click",function(){
        const num=numbers[i].textContent;
        display.value+=num;
    });
}
const clear=document.getElementById("clear");
clear.addEventListener("click",function(){
    display.value="";
});

const del=document.getElementById("delete");
del.addEventListener("click",function(){
    display.value=display.value.slice(0,-1);
});

const decimal=document.getElementById("decimal");
decimal.addEventListener("click",function(){
if(display.value.includes(".")){
    
}
else{
    display.value+=decimal.textContent;
}
});

