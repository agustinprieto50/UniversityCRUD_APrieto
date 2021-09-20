(function (){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e)=>{
            const confrimacion=confirm('Sgeuro que quiere eliminar el curso?');
            if (!confrimacion){
                e.preventDefault();
            }
        })  
    })
})();