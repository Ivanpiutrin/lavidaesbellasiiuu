function confirmarEliminacion(id){
    Swal.fire({
        title: '¿Desea Eliminar Este Usuario?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si',
        cancelButtonText: 'No'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            window.location.href='eliminarcliente/'+id
          )
        }
      })
}