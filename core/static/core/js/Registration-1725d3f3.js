import{_ as i,r,o as d,c as n,b as e,d as t,a as c,w as l,e as p}from"./index-8254f191.js";const _={name:"App",watch:{$route:{immediate:!0,handler(s,a){document.title=s.meta.title||"XGenius - Registration"}}}},u={id:"reg"},m={class:"registration"},h=p('<div class="reg-title"> Create new account </div><div class="reg-input"><input type="text" name="Name" id="" placeholder="Name"></div><div class="reg-input"><input type="text" name="Name" id="" placeholder="Email"></div><div class="reg-input"><input type="password" name="" id="" placeholder="Password*" title="Write your desired password"></div><div class="reg-input"><input type="password" name="" id="" placeholder="Confirm password*" title="Re-enter your password"></div>',5),v={class:"form-radio reg-flex"},g=e("div",{class:"enter"},[e("label",{class:"custom-radio"},[e("input",{type:"radio",name:"radio-button"}),e("span",{class:"radio-mark"})])],-1),f={class:"form-radio_text custom-width-radio_text"},y=e("button",{class:"form-send form-send-heigth"},"Sign up",-1);function w(s,a,x,N,k,$){const o=r("router-link");return d(),n("div",u,[e("div",m,[h,e("div",v,[g,e("div",f,[e("span",null,[t("I have read the "),c(o,{to:""},{default:l(()=>[t("privacy policy")]),_:1}),t(" and agree to the processing of my personal data")])]),y])])])}const C=i(_,[["render",w]]);export{C as default};
