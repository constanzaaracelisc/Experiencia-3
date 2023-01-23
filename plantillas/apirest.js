 <! ––« 

Este codigo nos muestra la forna de implementar el API Y DE DONDE TOMA ESTE MISMO PARA PODER TOMAR LOS DATOS DE ESTE MISMO NOS MANDA   «––>

   const API_URL= 'https://jsonplaceholder.typicode.com/';

const xhi=new XMLHttpRequest();



function onRequestHandler() {
	if(this.readyState ===4 && this.status===200){
		console.log(this.response);
	}
}


xhi.addEventListener("load",onRequestHandler);
xhi.open('GET','${API_URL}/users');
xhi.send();