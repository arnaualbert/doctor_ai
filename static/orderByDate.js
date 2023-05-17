$(document).ready(function() {
    var finishDateOrder = 1; // 1 para orden ascendente, -1 para orden descendente
$("#finish-date-header").on("click", function() {
    finishDateOrder *= -1; // Cambia el orden al hacer clic

    $("#table tbody").html(
      $("#table tbody tr").toArray().sort(function(c, d) {
        var dateC = new Date($(c).find("td:nth-child(5)").text());
        var dateD = new Date($(d).find("td:nth-child(5)").text());

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
  $("#filter-input").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#table tbody tr").filter(function () {
      var query = $(this).find("td:nth-child(2)").text().toLowerCase();
      var filename = $(this).find("td:nth-child(3)").text().toLowerCase();
      var filterMatch = query.indexOf(value) > -1 ||
        filename.indexOf(value) > -1;
      $(this).toggle(filterMatch);
    });
  });
  
  });
