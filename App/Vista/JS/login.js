
let resultado = '';
const consultaUsuario = document.getElementById('consultarUsuario');
const linkItem = document.getElementById('linkItem');
const linkProveedor = document.getElementById('linkProveedor');
const linkUsuario = document.getElementById('linkUsuario');

$(document).ready(function() {
    let resultado = '';
    if(localStorage.getItem('usuario')){
        const datosUsuario = JSON.parse( localStorage.getItem('usuario') );
        const usuario = datosUsuario.nombres + " " + datosUsuario.apellidos;
        resultado += `
            <div class="col-6">
                <a class="navbar-brand" href="index.html">
                    <img src=img/loogo.png alt="" width="200">
                </a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-expanded="false" aria-label="Toogle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
            <div class="col-5">
                <h4 id="usuario" class="derecha top-1">
                    ${usuario}
                    <br>
                    ${datosUsuario.rol}
                </h4> 
            </div>
            <div class="col-1">
                <div class="dropdown derecha top-2">
                    <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <svg id="userIcon" xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                        </svg>
                    </button>
                    <ul class="dropdown-menu">
                    <li><a onclick="cerrarSesion()" class="dropdown-item">Cerrar sesión</a></li>
                </ul>
            </div>
        </div>
        `
        consultaUsuario.innerHTML = resultado;
        if(datosUsuario.rol == "Empleado"){
            linkItem.style.display = 'block';
            linkProveedor.style.display = 'none';
            linkUsuario.style.display = 'none';    
        }
        if(datosUsuario.rol == "Admin"){
            linkItem.style.display = 'block';
            linkProveedor.style.display = 'block';
            linkUsuario.style.display = 'block';
        }
        
    }
    else{
        resultado += `
            <div class="col-6">
                <a class="navbar-brand" href= "#">
                    <img src=img/loogo.png alt="" width="200">
                </a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-expanded="false" aria-label="Toogle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
            <div class="col-6">
            <form class="form p-2 m-auto" id="botonLog" >
                <div class="row">
                    <div class="col-3"></div>
                    <div class="col-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input id="user" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="ejmp@email.com">
                    </div>
                    <div class="col-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input id="password" type="password" class="form-control" id="exampleInputPassword1" placeholder="*****">
                    </div>
                    <div class="col-3">
                        <br>
                        <button type="button" onclick="loginUsuario()" class="btn btn-info">Submit</button>
                    </div>
                </div>
            </form>
        </div>
        `
        consultaUsuario.innerHTML = resultado;
        const user = document.getElementById('user');
        const password = document.getElementById('password');
        user.value = '';
        password.value = '';
        linkItem.style.display = 'none';
        linkProveedor.style.display = 'none';
        linkUsuario.style.display = 'none';
    }
});

function loginUsuario(){
    const user = document.getElementById('user');
    const password = document.getElementById('password');
    const data = {
        'email': user.value,
        'clave': password.value
    }
    
    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:5000/iniciarsesion',
        data: data,
        dataType: "json",
    }).done(function(result){
        console.log(result)
        localStorage.setItem('usuario', JSON.stringify(result));
        location.reload();
    })
    .fail(function(){
        alertify
            .alert("Usuario o contraseña inválido", function(){
            alertify.message('OK');
        });
        user.value = '';
        password.value = '';
    })
};

function cerrarSesion() {
    localStorage.removeItem('usuario');
    location.href = 'index.html';
};