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

let firstnumber=0;
let operator="";
const add=document.getElementById("add");
const minus=document.getElementById("minus");
const multiply=document.getElementById("multiply");
const divide = document.getElementById("divide");
const mod=document.getElementById("mod");

function chooseop(op){
    firstnumber=Number(display.value);
    operator=op;
    display.value="";
}

add.addEventListener("click",function(){
    chooseop(add.textContent);
});

minus.addEventListener("click",function(){
    chooseop(minus.textContent);
});

multiply.addEventListener("click",function(){
    chooseop(multiply.textContent);
});

divide.addEventListener("click",function(){
    chooseop(divide.textContent);
});

mod.addEventListener("click",function(){
    chooseop(mod.textContent);
});
