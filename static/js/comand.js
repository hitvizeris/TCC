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

    if(categoria=="mainEntrada"){
        entrada.style.display = "grid";
        principal.style.display = "none";
        sobremesa.style.display = "none";
    }else if(categoria=="mainPrincipal"){
        entrada.style.display = "none";
        principal.style.display = "grid";
        sobremesa.style.display = "none";
    }else if(categoria=="mainSobremesa"){
        entrada.style.display = "none";
        principal.style.display = "none";
        sobremesa.style.display = "grid";
    }
}