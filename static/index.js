function mostrarPantallaEmergente(result) {
  var pantallaEmergente = document.getElementById("pantalla-emergente");
  var result = result
  console.log(result)
  pantallaEmergente.style.display = "block";
}

function ocultarPantallaEmergente() {
  var pantallaEmergente = document.getElementById("pantalla-emergente");
  pantallaEmergente.style.display = "none";
}