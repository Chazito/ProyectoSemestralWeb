const expr = /^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$/;
const passwordRegex = /^(.{8,20})$/;
;


function handleRegisterForm(event) {
    event.preventDefault();

    var username = $("#username").val();
    var email = $("#email").val();
    var password = $("#password").val();
    var rPassword = $("#repeatPassword").val();
    hideAllErrorMessages();

    if (username == "" || username.length < 6 || username.length > 20) {
        $("#mensaje1").fadeIn();
        return false;
    }
    if (!expr.test(email)) {
        $("#mensaje2").fadeIn();
        return false;
    }
    if (!passwordRegex.test(password)) {
        $("#mensaje3").fadeIn();
        return false;
    }
    if (password != rPassword) {
        $("#mensaje4").fadeIn();
        return false;
    }


    $("#btn-submit").val("Enviando...");

    const serviceId = "service_5ottxpb";
    const templateId = "template_1j4af5o";

    emailjs.sendForm(serviceId, templateId, this).then(() => {
        $("#btn-submit").val("Registrado!");
        alert("Datos enviados correctamente");
        return true;
    }).catch((err) => {
        $("#btn-submit").val("Registrarse!");
        alert("Error al enviar los datos. Intentelo nuevamente.");
        return false;
    });
}

function hideAllErrorMessages() {
    $("#mensaje1").fadeOut();
    $("#mensaje2").fadeOut();
    $("#mensaje3").fadeOut();
    $("#mensaje4").fadeOut();
}