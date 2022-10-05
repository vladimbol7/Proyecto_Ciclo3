const url = 'http://127.0.0.1:5000/listarItems';
const contenedor = document.querySelector('tbody');
const selectPersonal = document.getElementById('idPersonal');
const selectProveedor = document.getElementById('idProveedor');
let resultados = '';
let resultadosE = '';
let resultadosP = '';

const modalItem = new bootstrap.Modal(document.getElementById('modalItem'));
const formItem = document.querySelector('form');

const descripcion = document.getElementById('descripcion');
const cantidad = document.getElementById('cantidad');
const valorUnitario = document.getElementById('valorUnitario');
const idProveedor = document.getElementById('idProveedor');
const idPersonal = document.getElementById('idPersonal');
const idItem = document.getElementById('idFormItem');

let opcion = '';

btncrearItem.addEventListener('click', () => {
    descripcion.value = '';
    cantidad.value = '';
    valorUnitario.value = '';
    idProveedor.value = '';
    idPersonal.value = '';
    opcion = 'crear';
    modalItem.show();
})

$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
    }).done(function(data){
        console.log(data)
        data.forEach(item => {
            resultados += `<tr>
                                <td>${item.descripcion}</td>
                                <td>${item.cantidad}</td>
                                <td>${item.valor_unitario}</td>
                                <td>${item.proveedor}</td>
                                <td>${item.usuario}</td>
                                <td class="text-center"><a class="btnEditar btn btn-primary">Editar</a><a class="btnBorrar btn btn-danger">Borrar</a>
                                <input type="hidden" id="idItem" name="idItem" value=${item.id_item}>
                                <input type="hidden" id="idProveedor" name="idProveedor" value=${item.id_proveedor}>
                                <input type="hidden" id="idPersonal" name="idPersonal" value=${item.id_personar}>
                                </td>
                        </tr>
                        `
            })
            contenedor.innerHTML = resultados;
    });
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:5000/listarEmpleados',
        dataType: "json",
    }).done(function(dataE){
        console.log(dataE)
        dataE.forEach(empleado => {
            resultadosE += `<option value="${empleado.id_personar}">${empleado.documento}</option>`
            })
            selectPersonal.innerHTML = resultadosE;
    });
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:5000/listarProveedores',
        dataType: "json",
    }).done(function(dataP){
        console.log(dataP)
        dataP.forEach(proveedor => {
            resultadosP += `<option value="${proveedor.id_proveedores}">${proveedor.nombre}</option>`
            })
            selectProveedor.innerHTML = resultadosP;
    })
});

$(document).on('click', '.btnBorrar', function(e) {
    const fila = e.target.parentNode.parentNode;
    const id = fila.children[5].children[2].value
    alertify.confirm("Eliminar item",
    function(){
        $.ajax({
            type: "DELETE",
            url: 'http://127.0.0.1:5000/eliminarItem/' + id,
            dataType: "json",
        }).done(function(){
            alertify
                .alert("Item eliminado correctamente", function(){
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
    console.log(id);
    const descripcionForm = fila.children[0].innerHTML;
    const cantidadForm = fila.children[1].innerHTML;
    const valorUnitarioForm = fila.children[2].innerHTML;
    const ProveedorForm = fila.children[5].children[3].value;
    const PersonalForm = fila.children[5].children[4].value;
    descripcion.value = descripcionForm;
    cantidad.value = cantidadForm;
    valorUnitario.value = valorUnitarioForm;
    idProveedor.value = ProveedorForm;
    idPersonal.value = PersonalForm;
    idItem.value = id;
    opcion = 'editar';
    modalItem.show();
})

function submitForm(){
    if (opcion == 'crear'){
        const data = {
            'txtdescripcion': descripcion.value,
            'txtcantidad': cantidad.value,
            'txtvalorUnitario': valorUnitario.value,
            'txtidProveedor': idProveedor.value,
            'txtidPersonal': idPersonal.value
        }
        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:5000/crearItem',
            data: data,
            dataType: "json",
            success: function(){
                alertify
                    .alert("Item creado correctamente", function(){
                    alertify.message('OK');
                });
                location.reload();
            }
        })
    }
    if (opcion == 'editar'){
        const id = idItem.value;
        const data = {
            'txtdescripcion': descripcion.value,
            'txtcantidad': cantidad.value,
            'txtvalorUnitario': valorUnitario.value,
            'txtidProveedor': idProveedor.value,
            'txtidPersonal': idPersonal.value
        }
        $.ajax({
            type: "PUT",
            url: 'http://127.0.0.1:5000/modificarItem/' + id,
            data: data,
            dataType: "json"
        }).done(function(){
            alertify
                .alert("Item actualizado correctamente", function(){
                alertify.message('OK');
            });
            location.reload();
        });
    }
}
