// başa dön button
let yukari = document.getElementsByClassName("yukaricik")[0];
window.addEventListener("scroll",function(){
    let mesafe=window.scrollY;
   if(mesafe>300){
    yukari.classList.add("goster")
   }
   else{
     yukari.classList.remove("goster")
   }
});

yukari.addEventListener("click",function(){
    window.scrollTo(0,0)
});

 