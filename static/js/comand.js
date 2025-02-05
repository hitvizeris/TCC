menu = document.getElementById('itens');

function clickMenu(){
    if(menu.style.display == 'flex'){
        menu.style.display = 'none'
    }else{
        menu.style.display = 'flex'
    }
}

function ativaCategoria(categoria){
    entrada = document.getElementById("mainEntrada");
    principal = document.getElementById("mainPrincipal");
    sobremesa = document.getElementById("mainSobremesa");
    entradaA = document.getElementById("e");
    principalA = document.getElementById("p");
    sobremesaA = document.getElementById("s");

    if(categoria=="mainEntrada"){
        entrada.style.display = "grid";
        entradaA.style.backgroundColor = " #fadfb4";
        principal.style.display = "none";
        principalA.style.backgroundColor = "rgb(255, 255, 255)";
        sobremesa.style.display = "none";
        sobremesaA.style.backgroundColor = "rgb(255, 255, 255)";
    }else if(categoria=="mainPrincipal"){
        entrada.style.display = "none";
        entradaA.style.backgroundColor = "rgb(255, 255, 255)";
        principal.style.display = "grid";
        principalA.style.backgroundColor = " #fadfb4";
        sobremesa.style.display = "none";
        sobremesaA.style.backgroundColor = "rgb(255, 255, 255)";
    }else if(categoria=="mainSobremesa"){
        entrada.style.display = "none";
        entradaA.style.backgroundColor = "rgb(255, 255, 255)";
        principal.style.display = "none";
        principalA.style.backgroundColor = "rgb(255, 255, 255)";
        sobremesa.style.display = "grid";
        sobremesaA.style.backgroundColor = " #fadfb4";
    }
}