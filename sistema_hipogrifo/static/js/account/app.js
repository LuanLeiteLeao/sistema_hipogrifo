var url_atual = window.location.href;

var is_url_login = url_atual.indexOf('signin')!=-1?true:false; 
var is_url_cadastrar = url_atual.indexOf('signup')!=-1?true:false; 

var is_url_login = url_atual.indexOf('login')!=-1?true:false; 
var is_url_cadastrar = url_atual.indexOf('signup')!=-1?true:false; 

window.onload = () => { 
	// começar no topo
	  window.scrollTo(0, 0);
	  // selecionar a tela que deve começar
	if(is_url_login){
		ativar_sign_in_js()
	}else if(is_url_cadastrar){
		ativar_sign_up_js()
	}
	
} 

 on_submit=()=>{
	 // var $seuCampoCpf = $("#id_cpf");
        $("#id_cpf").unmask();
        // $seuCampoCpf.mask('00000000000', {reverse: true});

 	 	alert($('#id_cpf').val())
//  	var value = $('#id_cpf').maskMoney('unmasked')[0];
// console.log("-------------")
//  	console.log(value)
//     $('#id_cpf').val(value);
// alert(document.getElementById('id_cpf').value);
 	// ( '#id_cpf' ).mask( 'MASK', { placeholder: '' } );

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
