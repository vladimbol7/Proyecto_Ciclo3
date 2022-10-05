const url = 'http://127.0.0.1:5000/listarEmpleados';
const contenedor = document.querySelector('tbody');
let resultados = '';

const modalEmpleado = new bootstrap.Modal(document.getElementById('modalEmpleado'));
const formEmpleado = document.querySelector('form');

const nombres = document.getElementById('nombres');
const apellidos = document.getElementById('apellidos');
const documento = document.getElementById('documento');
const telefono = document.getElementById('telefono');
const email = document.getElementById('email');
const rol = document.getElementById('rol');
const clave = document.getElementById('clave');
const idEmpleado = document.getElementById('idFormEmpleado');
const fieldRol = document.getElementById('field-rol');
const fieldClave = document.getElementById('field-clave');

let opcion = '';

btncrearEmpleado.addEventListener('click', () => {
    nombres.value = '';
    apellidos.value = '';
    documento.value = '';
    telefono.value = '';
    email.value = '';
    rol.value = '';
    clave.value = '';
    opcion = 'crear';
    fieldRol.style.display = 'none';
    fieldClave.style.display = 'none';
    modalEmpleado.show();
})

$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
    }).done(function(data){
        console.log(data)
        data.forEach(empleado => {
            resultados += `<tr>
                                <td>${empleado.nombres}</td>
                                <td>${empleado.apellidos}</td>
                                <td>${empleado.documento}</td>
                                <td>${empleado.telefono}</td>
                                <td>${empleado.email}</td>
                                <td class="text-center"><a class="btnEditar btn btn-primary">Editar</a><a class="btnBorrar btn btn-danger">Borrar</a>
                                <input type="hidden" id="idEmpleado" name="idEmpleado" value=${empleado.id_personar}>
                                <input type="hidden" id="rol" name="rol" value=${empleado.rol}>
                                <input type="hidden" id="clave" name="clave" value=${empleado.clave}></td>
                                
                        </tr>
                        `
            })
            contenedor.innerHTML = resultados;
    })
});

$(document).on('click', '.btnBorrar', function(e) {
    const fila = e.target.parentNode.parentNode;
    const id = fila.children[5].children[2].value
    alertify.confirm("Eliminar empleado",
    function(){
        $.ajax({
            type: "DELETE",
            url: 'http://127.0.0.1:5000/eliminarEmpleado/' + id,
            dataType: "json",
        }).done(function(){
            alertify
                .alert("Empleado eliminado correctamente", function(){
                alertify.message('OK');
            });
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
    const id = fila.children[5].children[2].value;
    const nombresForm = fila.children[0].innerHTML;
    const apellidosForm = fila.children[1].innerHTML;
    const documentoForm = fila.children[2].innerHTML;
    const telefonoForm = fila.children[3].innerHTML;
    const emailForm = fila.children[4].innerHTML;
    const rolForm = fila.children[5].children[3].value;
    const claveForm = fila.children[5].children[4].value;
    nombres.value = nombresForm;
    apellidos.value = apellidosForm;
    documento.value = documentoForm;
    telefono.value = telefonoForm;
    email.value = emailForm;
    rol.value = rolForm;
    clave.value = claveForm;
    idEmpleado.value = id;
    opcion = 'editar';
    fieldRol.style.display = 'block';
    fieldClave.style.display = 'block';
    modalEmpleado.show();
})

function submitForm(){
    if (opcion == 'crear'){
        const data = {
            'txtnombres': nombres.value,
            'txtapellidos': apellidos.value,
            'txtdocumento': documento.value,
            'txttelefono': telefono.value,
            'txtcorreo': email.value
        }
        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:5000/crearEmpleado',
            data: data,
            dataType: "json",
            success: function(){
                alertify
                    .alert("Empleado creado correctamente", function(){
                    alertify.message('OK');
                });
                location.reload();
            }
        })
    }
    if (opcion == 'editar'){
        const id = idEmpleado.value;
        const data = {
            'txtnombres': nombres.value,
            'txtapellidos': apellidos.value,
            'txtdocumento': documento.value,
            'txttelefono': telefono.value,
            'txtcorreo': email.value,
            'txtrol': rol.value,
            'txtclave': clave.value
        }
        $.ajax({
            type: "PUT",
            url: 'http://127.0.0.1:5000/modificarEmpleado/' + id,
            data: data,
            dataType: "json",
            success: function(){
                alertify
                    .alert("Empleado actualizado correctamente", function(){
                    alertify.message('OK');
                });
                location.reload();
            }
        })
    }
}
