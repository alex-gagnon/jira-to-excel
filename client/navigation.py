from flask_login import login_required, current_user
from flask_nav.elements import Navbar, View


@login_required
def login_navbar():
    nav = list()
    if current_user.is_authenticated:
        nav.append([
            View('Logout', 'auth.logout')
        ])
    else:
        nav.append([
            View('Login', 'auth.login')
        ])

    return Navbar(*nav)
