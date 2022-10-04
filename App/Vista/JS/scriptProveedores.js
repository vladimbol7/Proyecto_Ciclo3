const url = 'http://127.0.0.1:5000/listarProveedores';
const contenedor = document.querySelector('tbody');
let resultados = '';

const modalProveedor = new bootstrap.Modal(document.getElementById('modalProveedor'));
const formProveedor = document.querySelector('form');

const nombre = document.getElementById('nombre');
const nit = document.getElementById('nit');
const telefono = document.getElementById('telefono');
const email = document.getElementById('email');
const idProveedor = document.getElementById('idFormProveedor');

let opcion = '';

btncrearProveedor.addEventListener('click', () => {
    nombre.value = '';
    nit.value = '';
    telefono.value = '';
    email.value = '';
    opcion = 'crear';
    modalProveedor.show();
})

$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
    }).done(function(data){
        console.log(data)
        data.forEach(proveedor => {
            resultados += `<tr>
                                <td>${proveedor.nombre}</td>
                                <td>${proveedor.nit}</td>
                                <td>${proveedor.telefono}</td>
                                <td>${proveedor.email}</td>
                                <td class="text-center"><a class="btnEditar btn btn-primary">Editar</a><a class="btnBorrar btn btn-danger">Borrar</a>
                                <input type="hidden" id="idProveedor" name="idProveedor" value=${proveedor.id_proveedores}></td>
                        </tr>
                        `
            })
            contenedor.innerHTML = resultados;
    })
});

$(document).on('click', '.btnBorrar', function(e) {
    const fila = e.target.parentNode.parentNode;
    const id = fila.children[4].children[2].value
    alertify.confirm("Eliminar proveedor",
    function(){
        $.ajax({
            type: "DELETE",
            url: 'http://127.0.0.1:5000/eliminarProveedor/' + id,
            dataType: "json",
        }).done(function(){
            location.reload();
        })
    },
    function(){
        alertify.error('Cancel');
    });
    console.log(id);
})

$(document).on('click', '.btnEditar', function(e) {
    const fila = e.target.parentNode.parentNode;
    const id = fila.children[4].children[2].value;
    console.log(id);
    const nombreForm = fila.children[0].innerHTML;
    const nitForm = fila.children[1].innerHTML;
    const telefonoForm = fila.children[2].innerHTML;
    const emailForm = fila.children[3].innerHTML;
    nombre.value = nombreForm;
    nit.value = nitForm;
    telefono.value = telefonoForm;
    email.value = emailForm;
    idProveedor.value = id;
    opcion = 'editar';
    modalProveedor.show();
})

function submitForm(){
    if (opcion == 'crear'){
        const data = {
            'txtnombre': nombre.value,
            'txtnit': nit.value,
            'txttelefono': telefono.value,
            'txtemail': email.value
        }
        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:5000/crearProveedor',
            data: data,
            dataType: "json",
            success: function(){
                alert('Creado exitosamente')
            }
        })
    }
    if (opcion == 'editar'){
        const id = idProveedor.value;
        const data = {
            'txtnombre': nombre.value,
            'txtnit': nit.value,
            'txttelefono': telefono.value,
            'txtemail': email.value,
        }
        $.ajax({
            type: "PUT",
            url: 'http://127.0.0.1:5000/modificarProveedor/' + id,
            data: data,
            dataType: "json"
        }).done(function(){
            alert('Modificado exitosamente');
        });
    }
    windows.location.reload(true);
}
