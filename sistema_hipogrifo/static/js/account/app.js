
var url_atual = window.location.href;
var is_url_login = url_atual.indexOf('signin')!=-1?true:false; 
var is_url_cadastrar = url_atual.indexOf('signup')!=-1?true:false; 

window.onload = () => { 
	if(is_url_login){
		ativar_sign_in_js()
	}else if(is_url_cadastrar){
		ativar_sign_up_js()
	}
	
} 


var btnSignin = document.querySelector("#signin");
var btnSignup = document.querySelector("#signup");

var body = document.querySelector("body");

ativar_sign_in_js = () =>{
	body.className = "sign-in-js";
}

ativar_sign_up_js = () =>{
	body.className = "sign-up-js";
}

btnSignin.addEventListener("click", ativar_sign_in_js);

btnSignup.addEventListener("click",ativar_sign_up_js);
