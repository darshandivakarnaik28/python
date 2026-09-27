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

const equal=document.getElementById("equal");
equal.addEventListener("click",function(){
    let secondnumber=Number(display.value);
    let result;
    switch(operator)
    {
        case '+':result=firstnumber+secondnumber;
        break
        case '-':result=firstnumber-secondnumber;
        break
        case '*':result=firstnumber*secondnumber;
        break
        case '/':if(secondnumber===0){
            result="Error division by zero is not allowed"
        }
        else{
            result=firstnumber/secondnumber;
        }
        break
        case '%':result=firstnumber%secondnumber;
        break

    }
    display.value=result;
    const historyitem=`${firstnumber} ${operator} ${secondnumber} = ${result}`;
    history.push(historyitem);
    localStorage.setItem("history",JSON.stringify(history));
    renderhistory();
});


document.addEventListener("keydown",function(event){
    if(event.key>="0" && event.key<="9"){
        display.value+=event.key;
    }
    else if(event.key=="Delete"){
        del.click();
        }
    else if(event.key=="Enter"){
        equal.click();                
    }
    else if(event.key=="Escape"){
        clear.click();
    }
    else if(event.key=="+"){
        add.click();
    }
    else if(event.key=="-"){
        minus.click();
    }
    else if(event.key=="*"){
        multiply.click();
    }
    else if(event.key=="/"){
        divide.click();
    }
    else if(event.key=="%"){
        mod.click();
    }
    else if(event.key=="."){
        decimal.click();
    }
    else if(event.key=="Backspace"){
        del.click();
    }
});

let history=[];
if (localStorage.getItem("history")){
    history=JSON.parse(localStorage.getItem("history"));
}
const historylist=document.getElementById("history-list");
function renderhistory(){
    historylist.innerHTML="";
    history.forEach(function(item){
        const li=document.createElement("li");   
        li.innerText=item;     
        historylist.appendChild(li)
    });
}