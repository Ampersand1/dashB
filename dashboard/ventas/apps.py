from django.apps import AppConfig

class VentasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ventas'
    verbose_name = 'Gestión de Ventas'
def ready(self):
        # Puedes realizar operaciones adicionales cuando la aplicación está lista
        pass