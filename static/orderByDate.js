$(document).ready(function() {
    var startDateOrder = 1; // 1 para orden ascendente, -1 para orden descendente
    var finishDateOrder = 1; // 1 para orden ascendente, -1 para orden descendente

    $("#start-date-header").on("click", function() {
      startDateOrder *= -1; // Cambia el orden al hacer clic
    
    $("#table tbody").html(
      $("#table tbody tr").toArray().sort(function(a, b) {
        var dateA = new Date($(a).find("td:nth-child(4)").text());
        var dateB = new Date($(b).find("td:nth-child(4)").text());

      return startDateOrder * (dateA - dateB);
    })
  );
  

  // Actualiza el estilo visual del encabezado para mostrar el orden actual
  if (startDateOrder === 1) {
    $(this).removeClass("desc");
    $(this).addClass("asc");
  } else {
    $(this).removeClass("asc");
    $(this).addClass("desc");
  }
});
$("#finish-date-header").on("click", function() {
    finishDateOrder *= -1; // Cambia el orden al hacer clic
    
    $("#table tbody").html(
      $("#table tbody tr").toArray().sort(function(a, b) {
        var dateC = new Date($(a).find("td:nth-child(5)").text());
        var dateD = new Date($(b).find("td:nth-child(5)").text());

      return finishDateOrder * (dateC - dateD);
    })
  );
  

  // Actualiza el estilo visual del encabezado para mostrar el orden actual
  if (finishDateOrder === 1) {
    $(this).removeClass("desc");
    $(this).addClass("asc");
  } else {
    $(this).removeClass("asc");
    $(this).addClass("desc");
  }
});
$("#filter-input").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#table tbody tr").filter(function() {
      var query = $(this).find("td:nth-child(2)").text().toLowerCase();
      var filename = $(this).find("td:nth-child(3)").text().toLowerCase();
      var filterMatch = query.indexOf(value) > -1 ||
                        filename.indexOf(value) > -1;
      $(this).toggle(filterMatch);
    });
  });
  });