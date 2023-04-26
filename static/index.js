function deleteRow(id) {
    // Confirmar con el usuario si realmente desea eliminar la fila
    if (confirm("Are you sure you want to delete this job?")) {
      // Enviar una solicitud AJAX al servidor para eliminar la fila
      const xhr = new XMLHttpRequest();
      xhr.open("DELETE", `/delete-row/${id}`, true);
      xhr.onload = function () {
        // Si la solicitud se completó correctamente, borrar la fila de la tabla
        if (xhr.status === 200) {
          const fila = document.getElementById(`fila-${id}`);
          fila.remove();
        }
      };
      xhr.send();
    }
  }