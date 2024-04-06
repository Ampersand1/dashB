from django.contrib import admin
from ventas.models import Dato

class VentasAdmin(admin.ModelAdmin):
    list_display = ["mes", "ventas", "barrio"]
    list_filter = ["mes", "barrio"]
    search_fields = ["mes", "barrio"]
    list_per_page = 10

    # Personalización de los estilos del panel de administración
    class Media:
        css = {
            "all": ("https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css",),
        }

admin.site.register(Dato, VentasAdmin)