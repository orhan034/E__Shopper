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

//  sayi ve fiyat toplamı
let arti= document.querySelector(".buton");
let eksi= document.querySelector(".buton1");
let adet=document.querySelector(".adet2");
let toplam=document.querySelector(".toplam");
let sifirla=document.querySelector(".sifirla-boton");
let card_total1=document.querySelector(".card_total1");
let card_total2=document.querySelector(".card_total2");
let card_total3=document.querySelector(".card_total3");
let a=0;
 
arti.onclick=() => {
  a++;
  let t=((a*59)+(b*59)+(c*59));
  adet.innerHTML=a;
  toplam.innerHTML="$"+a*59;
  card_total1.innerHTML="$"+t;
  card_total2.innerHTML="$"+((a*2)+(b*2)+(c*2));
  card_total3.innerHTML="$"+((t)+((a*2)+(b*2)+(c*2)));
}
eksi.onclick= () => {
  if(a>0){
  a--;
  let t=((a*59)+(b*59)+(c*59));
  adet.innerHTML=a;
  toplam.innerHTML="$"+a*59;
  card_total1.innerHTML="$"+t;
  card_total2.innerHTML="$"+((a*2)+(b*2)+(c*2));
  card_total3.innerHTML="$"+((t)+((a*2)+(b*2)+(c*2)));
  }
}
sifirla.onclick= () => {
  adet.innerHTML="0";
  toplam.innerHTML="$";
  a=0;
  let t=((a*59)+(b*59)+(c*59));
  card_total1.innerHTML="$"+t;
  card_total2.innerHTML="$"+((a*2)+(b*2)+(c*2));
  card_total3.innerHTML="$"+((t)+((a*2)+(b*2)+(c*2)));

}

let btnArti= document.querySelector(".buton111");
let btnEksi= document.querySelector(".buton11");
let adet2= document.querySelector(".adet22");
let toplam1= document.querySelector(".toplam11");
let sifirla2=document.querySelector(".sifirla-boton1");

let b=0;
btnArti.onclick= () => {
  b++;
  let t=((a*59)+(b*59)+(c*59));
  adet2.innerHTML=b;
  toplam1.innerHTML="$"+b*59;
  card_total1.innerHTML="$"+t;
  card_total2.innerHTML="$"+((a*2)+(b*2)+(c*2));
  card_total3.innerHTML="$"+((t)+((a*2)+(b*2)+(c*2)));
}
btnEksi.onclick= () => {
  if(b>0){
  b--;
  let t=((a*59)+(b*59)+(c*59));
  adet2.innerHTML=b;
  toplam1.innerHTML="$"+b*59;
  card_total1.innerHTML="$"+t;
  card_total2.innerHTML="$"+((a*2)+(b*2)+(c*2));
  card_total3.innerHTML="$"+((t)+((a*2)+(b*2)+(c*2)));
  }
}
sifirla2.onclick= () => {
  adet2.innerHTML="0";
  toplam1.innerHTML="$";
  b=0;
  let t=((a*59)+(b*59)+(c*59));
  card_total1.innerHTML="$"+t;
  card_total2.innerHTML="$"+((a*2)+(b*2)+(c*2));
  card_total3.innerHTML="$"+((t)+((a*2)+(b*2)+(c*2)));
}

let arti1= document.querySelector(".buton1111");
let eksi1= document.querySelector(".buton_1");
let adet1=document.querySelector(".adet222");
let toplam2=document.querySelector(".toplam111");
let sifirla3=document.querySelector(".sifirla-boton11");
let c=0;

arti1.onclick= () => {
  c++;
  let t=((a*59)+(b*59)+(c*59));
  adet1.innerHTML=c;
  toplam2.innerHTML="$"+c*59;
  card_total1.innerHTML="$"+t;
  card_total2.innerHTML="$"+((a*2)+(b*2)+(c*2));
  card_total3.innerHTML="$"+((t)+((a*2)+(b*2)+(c*2)));
}
eksi1.onclick= () => {
  if(c>0){
  c--;
  let t=((a*59)+(b*59)+(c*59));
  adet1.innerHTML=c;
  toplam2.innerHTML="$"+c*59;
  card_total1.innerHTML="$"+t;
  card_total2.innerHTML="$"+((a*2)+(b*2)+(c*2));
  card_total3.innerHTML="$"+((t)+((a*2)+(b*2)+(c*2)));
  }
}
sifirla3.onclick= () => {
  adet1.innerHTML="0";
  toplam2.innerHTML="$";
  c=0;
  let t=((a*59)+(b*59)+(c*59));
  card_total1.innerHTML="$"+t;
  card_total2.innerHTML="$"+((a*2)+(b*2)+(c*2));
  card_total3.innerHTML="$"+((t)+((a*2)+(b*2)+(c*2)));
}