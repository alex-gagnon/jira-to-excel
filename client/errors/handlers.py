from . import bp


@bp.errorhandler(500)
def handle_500(e):
    return f"{e} Error"


@bp.errorhandler(400)
def handle_400(e):
    return f"{e} Error"
