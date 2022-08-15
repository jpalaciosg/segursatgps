from triggers.models import FleetTrigger,FleetTriggerExtension1008
from geofences.models import Geofence
from users.models import Account
from django.db.models import Q

# PARADAS POR 15 MINUTOS
account = Account.objects.get(name='civa')
geofences = Geofence.objects.raw("""
    SELECT * FROM geofences_geofence WHERE account_id=5 AND
    name IN (
        'PLAZA NORTE AREQUIPA',
        'PTE. NUEVO',
        'TALLER PUERTO MALDONADO',
        'TALLER AREQUIPA',
        'TALLER CHICLAYO',
        'TALLER CUSCO',
        'TALLER PIURA',
        'TALLER TACNA',
        'Taller Unión',
        'TER HUARAZ',
        'TERMINAL 28 JULIO',
        'AGENCIA ATOCONGO',
        'AGENCIA AYAVIRI',
        'AGENCIA BAGUA GRANDE',
        'AGENCIA CAMANA',
        'AGENCIA CHULUCANAS',
        'AGENCIA CUSCO',
        'AGENCIA GRAU-PIURA',
        'AGENCIA SICUANI',
        'CHACHAPOYAS NUEVA A.',
        'COCHERA TARAPOTO',
        'javier prado',
        'TERMINAL AREQUIPA',
        'TERMINAL AYACUCHO',
        'TERMINAL BAGUA CHICA',
        'TERMINAL CAJAMARCA',
        'TERMINAL CHACHAPOYAS',
        'TERMINAL CHICLAYO',
        'TERMINAL CHULUCANAS',
        'TERMINAL CUSCO',
        'TERMINAL DESAGUADERO',
        'TERMINAL GECHISA',
        'TERMINAL GUAYAQUIL',
        'TERMINAL HUANCABAMBA',
        'TERMINAL ILO',
        'TERMINAL JAEN',
        'TERMINAL JAVIER PRADO',
        'TERMINAL MARAÑON CIX',
        'TERMINAL MARCONA',
        'TERMINAL MORROPON',
        'TERMINAL OLMOS',
        'TERMINAL PAITA',
        'TERMINAL PIURA BOSQUE',
        'TERMINAL PIURA LORETO',
        'TERMINAL PUERTO MALDONADO',
        'TERMINAL SAN IGNACIO',    
        'TERMINAL TACNA',
        'TERMINAL TALARA',
        'TERMINAL TARAPOTO',
        'TERMINAL TRUJILLO',
        'TERMINAL TUMBES',
        'TERRAPUERTO AREQUIPA',
        'Terrapuerto trujillo',
        'VOLVO Santa Anita',
        'MINA ANTAMINA',
        'Ransa San Agustin',
        'PARQUEO EXTERNO ANTAMINA',
        'PAQREUO EXTERNO II CMA',
        'CASA BLANCA',
        'PERNOCTE SUPE',
        'PERNOCTE AUCALLAMA',
        'PERNOCTE PASAMAYO'
    );
""")

print(geofences)

for geofence in geofences:
    print(geofence.name)
    print(geofence.description)
    print('==================')

print(len(geofences))

trigger = FleetTrigger.objects.create(
    name = "ALERTA DE PARADA FUERA DE GEOCERCA - 15MIN",
    description = "15 MINUTOS DETENIDO",
    alert_type = 1008,
    is_active = True,
    send_notification = True,
    send_mail_notification = True,
    account = account
)

extension1008 = FleetTriggerExtension1008.objects.create(
    seconds = 900,
    account = account
)
extension1008.geofences.set(geofences)
extension1008.save()

trigger.extension1008 = extension1008
trigger.save()