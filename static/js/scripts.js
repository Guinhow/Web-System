//submenus
document.addEventListener('DOMContentLoaded', function() {
    var administrativo = document.getElementById('administrativo');
    var submenuAdministrativo = document.getElementById('submenu-administrativo');
    var relatorios = document.getElementById('relatorios');
    var submenuRelatorios = document.getElementById('submenu-relatorios');

    administrativo.addEventListener('click', function(event) {
        event.preventDefault();
        if (submenuAdministrativo.style.display === 'block') {
            submenuAdministrativo.style.display = 'none';
        } else {
            submenuAdministrativo.style.display = 'block';
        }
    });


    relatorios.addEventListener('click', function(event) {
        event.preventDefault();
        if (submenuRelatorios.style.display === 'block') {
            submenuRelatorios.style.display = 'none';
        } else {
            submenuRelatorios.style.display = 'block';
        }
    });

    // Redirecionamento dos submenus
    var itensSubmenuA = submenuAdministrativo.querySelectorAll('li');
    itensSubmenuA.forEach(function(item) {
        item.addEventListener('click', function(event) {
            var url = item.querySelector('a').getAttribute('href');
            window.location.href = url;
        });
    });

    var itensSubmenu = submenuRelatorios.querySelectorAll('li');
    itensSubmenu.forEach(function(item) {
        item.addEventListener('click', function(event) {
            var url = item.querySelector('a').getAttribute('href');
            window.location.href = url;
        });
    });
});
//logout
function confirmLogout() {
    if (confirm('Tem certeza de que deseja fazer logout?')) {
        document.getElementById('logout-form').submit();
    }
};


