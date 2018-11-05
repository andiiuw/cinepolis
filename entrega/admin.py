from django.contrib import admin

from .models import (Camion)
from .models import (Ciudad,CiudadAdmin)
from .models import Piloto
from .models import Paquete

admin.site.register(Camion)
admin.site.register(Ciudad,CiudadAdmin)
admin.site.register(Piloto)
admin.site.register(Paquete)
# Register your models here.
