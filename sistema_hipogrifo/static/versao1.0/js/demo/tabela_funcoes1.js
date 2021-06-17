var linhasNovas = 0;	// variável auxiliar
var linhaEmEdicao = null;

function ExcluirLinha(idLinha) {
	console.log("este é o idlinha do excluir:"+idLinha);
	if(!linhaEmEdicao) {
		var linha = document.getElementById(idLinha);
		linha.className='linhaSelecionada';
		if(confirm("Tem certeza que deseja excluir este registro?")) {
			//Aviso(1);	// exibe o aviso "Aguarde..."
			linhaEmEdicao = idLinha;
			var celulas = document.getElementById(idLinha).cells;
			var cod = idLinha;
			var url="tabelaDados.php?acao=excluir&cod="+cod;
			requisicaoHTTP("GET",url,true);
		}
		else linha.className='linha';
	}
	else alert("Voc� est� com um registro aberto. Feche-o antes de prosseguir.");
}

function NovoRegistro(){	
	// insere uma nova linha na tabela
		if(linhaEmEdicao)
			alert("Você está com um registro aberto. Feche-o antes de prosseguir.");
		else {
			proxIndice = document.getElementById('dataTable').rows.length-1;
			var novaLinha = document.getElementById('dataTable').insertRow(proxIndice);
			novaLinha.className='linhaSelecionada';
		
			// define o id da nova linha (que será usado em caso de edição/exclusão)
			novoId = "nova"+linhasNovas;
			novaLinha.setAttribute('id',novoId);
			linhasNovas++;
			linhaEmEdicao = novoId;
		
			// insere as células na linha criada
			var novasCelulas = new Array(9);
			for(var i=0; i<novasCelulas.length; i++)
				novasCelulas[i] = novaLinha.insertCell(i);
		
			novasCelulas[0].innerHTML = '<input type="text" name="nome_materia" >'; 
			novasCelulas[1].innerHTML = '<select name= "semestre" id="novocombo">'+
										'<option value= "PRIMEIRO">1-PRIMEIRO</option>'+
										'<option value= "SEGUNDO">2-SEGUNDO</option>'+
										'<option value= "TERCEIRO">3-TERCEIRO</option>'+
										'<option value= "QUARTO">4-QUARTO</option>'+
										'<option value= "QUINTO">5-QUINTO</option>'+
										'<option value= "SEXTO">6-SEXTO</option>'+
										'<option value= "SETIMO">7-SETIMO</option>'+
										'<option value= "OITAVO">8-OITAVO</option>';
			
			novasCelulas[2].innerHTML = '<input type="text" name="nota_1">';
			novasCelulas[3].innerHTML = '<input type="text" name="nota_2">';
			novasCelulas[4].innerHTML = '<input type="text" name="professor">';
			novasCelulas[5].innerHTML = '<input type="text" name="media">';
			novasCelulas[6].innerHTML = '<input type="text" name="nota_Nescessaria">';
			novasCelulas[7].innerHTML = '<a href="#" onclick="Cadastrar('+linhaEmEdicao+')">Cadastrar</a>'; // botão de cadastro
			novasCelulas[8].innerHTML = '<a href="javascript:CancelarInclusao()">Cancelar</a>'; // botão de cancelamento
		}
	
}

function CancelarInclusao() {
	var linha = document.getElementById(linhaEmEdicao);
	linha.parentNode.removeChild(linha); 
	linhasNovas--;
	linhaEmEdicao=null;
}

// prepara uma linha para edi��o
function EditarLinha(idLinha) {
	if(!linhaEmEdicao) {
		linhaEmEdicao = idLinha;
		// obt�m a linha a ser editada e altera sua cor
		var linha = document.getElementById(idLinha);
		linha.className='linhaSelecionada';
		var celulas = linha.cells;

		// salva os dados atuais (para o caso de cancelamento)
		SalvaDados(idLinha);
		console.log('esse é o id linha: '+idLinha);
		
		// cria os campos de texto edit�veis
		celulas[0].innerHTML = '<input type="text" name="nome_materia" value="'+celulas[0].innerHTML+'">';
		console.log(celulas[1]);
		celulas[1];
		var idid=("boxbox"+idLinha);
		var semestre = document.getElementById(idid);
		semestre.removeAttribute("disabled");
		celulas[2].innerHTML = '<input type="text" name="nota_1" value="'+celulas[2].innerHTML+'">';
		celulas[3].innerHTML = '<input type="text" name="nota_2" value="'+celulas[3].innerHTML+'">';
		celulas[4].innerHTML = '<input type="text" name="professor" value="'+celulas[4].innerHTML+'">';
		celulas[5].innerHTML = '<input type="text" name="media" value="'+celulas[5].innerHTML+'">';
		celulas[6].innerHTML = '<input type="text" name="nota_nescessaria" value="'+celulas[6].innerHTML+'">';

		celulas[7].innerHTML = '<a href="#" onclick="Atualizar('+idLinha+')">Atualizar</a><br>';
								
		celulas[8].innerHTML = '<a href="#" onclick="Cancelar()">Cancelar</a>';
	}
	else alert("Voc� j� est� editando um registro!");
}

// atualiza o conte�do da linha
function Atualizar(id) {
	//Aviso(1);	// exibe o aviso "Aguarde..."
	var form = document.forms.formulario;
	console.log(form);
	var dados = ObtemDadosForm(form);
	console.log('este é o dados: '+dados);
	var cod = id;
	var combo = ("boxbox"+id);
	var semestre1 = document.getElementById(combo);
	var str = semestre1.options[semestre1.selectedIndex].value;
	console.log("como manual     :"+str);
	console.log("este é o id: "+cod);
	var url="tabelaDados.php?acao=atualizar";
	url += "&cod="+cod+"&semestre="+str+"&"+dados;
	console.log(url);
	requisicaoHTTP("GET",url,true);
}
// salva os dados atuais da linha em um array
function SalvaDados(idLinha){
	var celulas = document.getElementById(idLinha).cells;
	dadosAtuais = new Array(celulas.length);
	for(var i=0; i<celulas.length; i++)
		dadosAtuais[i] = celulas[i].innerHTML;
}

// cancela a edi��o de uma linha
function Cancelar() {
	// volta o formato original
	var linha = document.getElementById(linhaEmEdicao);
	linha.className='linha';

	// coloca os dados anteriores
	var celulas	 = linha.cells;
	for(var i=0; i<dadosAtuais.length; i++)
		celulas[i].innerHTML = dadosAtuais[i];
	linhaEmEdicao=null;
}

// cancela a inclus�o de uma linha, excluindo-a
function CancelarInclusao() {
	var linha = document.getElementById(linhaEmEdicao);
	linha.parentNode.removeChild(linha); 
	linhasNovas--;
	linhaEmEdicao=null;
}

// chamada programa PHP que cadastra no banco de dados
function Cadastrar (linhaE) {
	//Aviso(1);
	var meuForm = document.forms.formulario;
	var dados = ObtemDadosForm(meuForm);
	var semestre1 = document.getElementById("novocombo");
	console.log("manual combo    :"+semestre1);
	var str = semestre1.options[semestre1.selectedIndex].value;
	console.log("manual combo    :"+str);
	var url="tabelaDados.php?acao=cadastrar&"+"&semestre="+str+"&"+dados;
	requisicaoHTTP("GET",url,true);
	console.log(url);
}

// coloca os dados do formul�rio em formato de query string
function ObtemDadosForm(meuForm) {
	console.log('entrou no obterdados');
	console.log(meuForm);
	var parametros = new Array();
	console.log("tamanho do length"+meuForm.elements.length);

	// percorre os elementos do formul�rio
	for(var i=2; i<meuForm.elements.length; i++) {
		if(!( (meuForm.elements[i].name=="semestre") || (meuForm.elements[i].name=="media") || (meuForm.elements[i].name=="nota_nescessaria") ) ){
		var param = meuForm.elements[i].name;
		console.log("Esse é o param:"+param);
		param += "=";
		param += encodeURIComponent(meuForm.elements[i].value);
		console.log('este é parametro:'+param);
		parametros.push(param);
		}
	}
	// retona os par�metros separados por &, para uso na query string
	return parametros.join("&");
}

// exibe ou oculta a mensagem de espera
/* function Aviso(exibir) {
	var saida = document.getElementById("avisos");
	if(exibir){
		saida.className = "aviso";
		saida.innerHTML = "Aguarde...processando!";
	}
	else {
		saida.className = "";
		saida.innerHTML = "";
	}
} */

// trata a resposta do servidor, de acordo com a opera��o realizada
function trataDados(){
	var resposta = ajax.responseText;
	var linha = document.getElementById(linhaEmEdicao);
	
	if(resposta.match(/atualizou.*/)) {		// registro foi atualizado
		// volta o estilo antigo
		linha.className='linha';
		var celulas	 = linha.cells;
		// coloca os novos valores nas c�lulas
		var meuForm = document.forms.formulario;
		var nome_materia = meuForm.nome_materia.value;
		var semestre = meuForm.semestre.value;
		var nota_1 = meuForm.nota_1.value.replace(",",".");
		var nota_2 = meuForm.nota_2.value.replace(",",".");		
		var professor = meuForm.professor.value;
		var media = (nota_1*2 + nota_2*3)/5;
		var nota_nescessaria = (30-nota_1*2)/3;
		celulas[0].innerHTML = nome_materia;
		celulas[1];
		var idid=("boxbox"+linhaEmEdicao);
		var semestre = document.getElementById(idid);
		semestre.setAttribute("disabled","");
		celulas[2].innerHTML = nota_1.replace(".",",");
		celulas[3].innerHTML = nota_2.replace(".",",");
		celulas[4].innerHTML = professor;
		celulas[5].innerHTML = media.toFixed(2).replace(".",",");
		celulas[6].innerHTML = nota_nescessaria.toFixed(2).replace(".",",");

		celulas[7].innerHTML = dadosAtuais[7]; // bot�o de edi��o
		celulas[8].innerHTML = dadosAtuais[8]; // bot�o de exclus�o
		linhaEmEdicao=null;
	}
	else if(resposta=="excluiu") {		// registro foi exclu�do
		linha.parentNode.removeChild(linha); 
		linhaEmEdicao=null;
	}
	else if(resposta.substring(0,9)=="cadastrou") {	// registro foi inclu�do
		linha.className='linha';
		var celulas	 = linha.cells;
		
		// obt�m o c�digo gerado para o produto no banco de dados
		novoCodigo = resposta.substring(10);
		
		// coloca os novos valores nas c�lulas
		var meuForm = document.forms.formulario;
		var nome_materia = meuForm.nome_materia.value;
		var semestre = meuForm.semestre.value;
		var nota_1 = meuForm.nota_1.value.replace(",",".");
		var nota_2 = meuForm.nota_2.value.replace(",",".");		
		var professor = meuForm.professor.value;
		var media = (nota_1*2 + nota_2*3)/5;
		var nota_nescessaria = (30-nota_1*2)/3;
		celulas[0].innerHTML = nome_materia;
		celulas[1];
		var idid=(linhaEmEdicao);
		var semestre = document.getElementById("novocombo");
		//semestre.removeAttribute("disabled");
		semestre.setAttribute("disabled","");
		celulas[2].innerHTML = nota_1.replace(".",",");
		celulas[3].innerHTML = nota_2.replace(".",",");
		celulas[4].innerHTML = professor;
		celulas[5].innerHTML = media.toFixed(2).replace(".",",");
		celulas[6].innerHTML = nota_nescessaria.toFixed(2).replace(".",",");
		celulas[7].innerHTML = '<a href="#" onclick="EditarLinha(\''+linhaEmEdicao+'\');">Editar</a>';
		celulas[8].innerHTML = '<a href="#" onclick="ExcluirLinha(\''+linhaEmEdicao+'\');">Excluir</a>';
		linhaEmEdicao=null;
	}
	else // mensagem de erro
		alert(resposta);
	//Aviso(0);
}
