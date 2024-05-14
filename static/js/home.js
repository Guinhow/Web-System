document.addEventListener("DOMContentLoaded", function() {
    var menuItems = document.querySelectorAll('.nav-list > li > a');
    menuItems.forEach(function(item) {
        item.addEventListener('click', function(event) {
            var submenu = this.parentNode.querySelector('.submenu');
            if (submenu) {
                event.preventDefault(); 
                var isOpen = submenu.classList.contains('active');
                closeAllSubmenus(); 
                if (!isOpen) {
                    submenu.classList.add('active'); 
                }
            }
        });
    });

    
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.nav-list')) {
            closeAllSubmenus();
        }
    });

   
    function closeAllSubmenus() {
        var submenus = document.querySelectorAll('.submenu');
        submenus.forEach(function(submenu) {
            submenu.classList.remove('active'); 
        });
    }
});
function confirmLogout() {
    if (confirm('Tem certeza de que deseja fazer logout?')) {
        document.getElementById('logout-form').submit();
    }
};

function confirmarRemocao() {
    return confirm("Tem certeza de que deseja remover este dado?");
}