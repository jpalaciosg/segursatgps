from triggers.models import FleetTrigger,FleetTriggerExtension1007
from geofences.models import Geofence
from users.models import Account
from django.db.models import Q

# PARADAS POR 30 MINUTOS

account = Account.objects.get(name='civa')
#account = Account.objects.get(name='pruebas')
geofences = Geofence.objects.filter(account=account)
geofences = geofences.filter(
    Q(name = 'plaza norte') |
    Q(name = 'TERMINAL PLAZA NORTE')
)

for geofence in geofences:
    print(geofence.name)
    #print(geofence.description)
    print('==================')

print(len(geofences))

trigger = FleetTrigger.objects.create(
    name = "ALERTA DE PARADA 30MIN",
    description = "30 MINUTOS DETENIDO",
    alert_type = 1007,
    is_active = True,
    send_notification = True,
    send_mail_notification = True,
    account = account
)

extension1007 = FleetTriggerExtension1007.objects.create(
    seconds = 1800,
    account = account
)
extension1007.geofences.set(geofences)
extension1007.save()

trigger.extension1007 = extension1007
trigger.save()

# PARADAS POR 20 MINUTOS

account = Account.objects.get(name='civa')
#account = Account.objects.get(name='pruebas')
geofences = Geofence.objects.filter(account=account)
geofences = geofences.filter(
    Q(name = 'AGENCIA CHIMBOTE') |
    Q(name = 'AGENCIA JULIACA') |
    Q(name = 'Agencia Lambayeque') |
    Q(name = 'AGENCIA MATANZA') |
    Q(name = 'AGENCIA MOQUEGUA') |
    Q(name = 'AGENCIA MOYOBAMBA') |
    Q(name = 'AGENCIA NAZCA') |
    Q(name = 'AGENCIA NUEVA CAJAMARCA') |
    Q(name = 'AGENCIA PUNO') |
    Q(name = 'AGENCIA SULLANA')
)

for geofence in geofences:
    print(geofence.name)
    #print(geofence.description)
    print('==================')

print(len(geofences))

trigger = FleetTrigger.objects.create(
    name = "ALERTA DE PARADA 20MIN",
    description = "20 MINUTOS DETENIDO",
    alert_type = 1007,
    is_active = True,
    send_notification = True,
    send_mail_notification = True,
    account = account
)

extension1007 = FleetTriggerExtension1007.objects.create(
    seconds = 1200,
    account = account
)
extension1007.geofences.set(geofences)
extension1007.save()

trigger.extension1007 = extension1007
trigger.save()

# PARADAS POR 15 MINUTOS

account = Account.objects.get(name='civa')
#account = Account.objects.get(name='pruebas')
geofences = Geofence.objects.filter(account=account)
geofences = geofences.filter(
    Q(name = 'Peaje Ancon') |
    Q(name = 'RESTAURANT - ABANTO') |
    Q(name = 'RESTAURANT CHINCHORRO - IDA') |
    Q(name = 'RESTAURANT CHINCHORRO - RETORNO') |
    Q(name = 'RESTAURANT EL CHORRY CHALHUANCA') |
    Q(name = 'RESTAURANT EL OLIVAR') |
    Q(name = 'RESTAURANT EL VIAJERO') |
    Q(name = 'RESTAURANT ESTRELLITA') |
    Q(name = 'RESTAURANT MIKAEVE-HUARMEY') |
    Q(name = 'RESTAURANT SANTA LUCIA') |
    Q(name = 'RESTAURANT WARI NAZCA') |
    Q(name = 'SENASA MONTALVO') |
    Q(name = 'Sunat Pucusana') |
    Q(name = 'Agencia Canchaque') |
    Q(name = 'AGENCIA HUAURA') |
    Q(name = 'AGENCIA ICA') |
    Q(name = 'Agencia Mancora') |
    Q(name = 'AGENCIA MOTUPE') |
    Q(name = 'AGENCIA ORGANOS') |
    Q(name = 'AGENCIA PACASMAYO') |
    Q(name = 'AGENCIA PEDRO RUIZ') |
    Q(name = 'AGENCIA PUCARÁ') |
    Q(name = 'Agencia Rioja') |
    Q(name = 'Agencia Urcos') |
    Q(name = 'AGENCIA ZORRITOS') |
    Q(name = 'Control Aduana Cabanillas') |
    Q(name = 'Control Aduana Ojerani') |
    Q(name = 'Control Aduana Tomasiri') |
    Q(name = 'Control Aduana Vila Vila') |
    Q(name = 'CONTROL CARPITAS') |
    Q(name = 'Control Sunat Mazuco') |
    Q(name = 'CRUCE OLMOS') |
    Q(name = 'GRIFO AREQUIPA') |
    Q(name = 'GRIFO LAMBAYEQUE') |
    Q(name = 'GRIFO PRIMAX AREQUIPA') |
    Q(name = 'Grifo Primax-Chiclayo') |
    Q(name = 'GRIFO TARAPOTO') |
    Q(name = 'TERMINAL ABANCAY') |
    Q(name = 'TERMINAL MAZUCO') |
    Q(name = 'TERMINAL MOLLENDO')
)

for geofence in geofences:
    print(geofence.name)
    #print(geofence.description)
    print('==================')

print(len(geofences))

trigger = FleetTrigger.objects.create(
    name = "ALERTA DE PARADA 15MIN",
    description = "15 MINUTOS DETENIDO",
    alert_type = 1007,
    is_active = True,
    send_notification = True,
    send_mail_notification = True,
    account = account
)

extension1007 = FleetTriggerExtension1007.objects.create(
    seconds = 900,
    account = account
)
extension1007.geofences.set(geofences)
extension1007.save()

trigger.extension1007 = extension1007
trigger.save()

# PARADAS POR 10 MINUTOS

account = Account.objects.get(name='civa')
#account = Account.objects.get(name='pruebas')
geofences = Geofence.objects.filter(account=account)
geofences = geofences.filter(
    Q(name = 'Peaje Aguas Claras') |
    Q(name = 'Peaje Bayovar-Piura') |
    Q(name = 'Peaje Cancas') |
    Q(name = 'Peaje Casacancha-Cusco') |
    Q(name = 'Peaje Chicama') |
    Q(name = 'Peaje Chilca') |
    Q(name = 'Peaje Chincha') |
    Q(name = 'Peaje Chulucanas') |
    Q(name = 'Peaje Ciudad De  Dios') |
    Q(name = 'PEAJE DE ATICO') |
    Q(name = 'PEAJE DE CAMANA') |
    Q(name = 'Peaje de Ica') |
    Q(name = 'Peaje De Ilo') |
    Q(name = 'Peaje De Uchumayo') |
    Q(name = 'Peaje de Villa') |
    Q(name = 'Peaje De Yauca') |
    Q(name = 'Peaje El Fiscal') |
    Q(name = 'Peaje Fortaleza Paramonga') |
    Q(name = 'Peaje Huacho') |
    Q(name = 'Peaje Huarmey KM 314') |
    Q(name = 'Peaje Loma Larga-Canchaque') |
    Q(name = 'Peaje Marcona') |
    Q(name = 'Peaje Mocce-Lambayeque') |
    Q(name = 'Peaje Montalvo') |
    Q(name = 'Peaje Morrope') |
    Q(name = 'Peaje Moyobamba') |
    Q(name = 'Peaje Nazca') |
    Q(name = 'PEAJE OLMOS') |
    Q(name = 'Peaje P. Maldonado') |
    Q(name = 'Peaje Pacanguilla') |
    Q(name = 'Peaje Pampa Galeras') |
    Q(name = 'Peaje Pampamarca') |
    Q(name = 'Peaje Patahuasi') |
    Q(name = 'Peaje Pero Ruiz') |
    Q(name = 'Peaje Pomahuaca') |
    Q(name = 'Peaje Puente Piedra') |
    Q(name = 'PEAJE PUNTA NEGRA') |
    Q(name = 'Peaje Rumichaca') |
    Q(name = 'PEAJE SOCOS AYACUCHO') |
    Q(name = 'Peaje Sullana') |
    Q(name = 'Peaje Talara') |
    Q(name = 'Peaje Tomasiri') |
    Q(name = 'PEAJE TUNAN') |
    Q(name = 'Peaje Utcubamba') |
    Q(name = 'Peaje Vesique-Chimbote') |
    Q(name = 'Peaje Viru') |
    Q(name = 'Control Senasa-Trujillo') |
    Q(name = 'CRUCE CHAMAYA') |
    Q(name = 'PUNTO DE CONTROL TUNAN')
)

for geofence in geofences:
    print(geofence.name)
    #print(geofence.description)
    print('==================')

print(len(geofences))

trigger = FleetTrigger.objects.create(
    name = "ALERTA DE PARADA 10MIN",
    description = "10 MINUTOS DETENIDO",
    alert_type = 1007,
    is_active = True,
    send_notification = True,
    send_mail_notification = True,
    account = account
)

extension1007 = FleetTriggerExtension1007.objects.create(
    seconds = 600,
    account = account
)
extension1007.geofences.set(geofences)
extension1007.save()

trigger.extension1007 = extension1007
trigger.save()

# PARADAS POR 5 MINUTOS

account = Account.objects.get(name='civa')
#account = Account.objects.get(name='pruebas')
geofences = Geofence.objects.filter(account=account)
geofences = geofences.filter(
    Q(name = 'Balanza Cerro Azul')
)

for geofence in geofences:
    print(geofence.name)
    #print(geofence.description)
    print('==================')

print(len(geofences))

trigger = FleetTrigger.objects.create(
    name = "ALERTA DE PARADA 5MIN",
    description = "5 MINUTOS DETENIDO",
    alert_type = 1007,
    is_active = True,
    send_notification = True,
    send_mail_notification = True,
    account = account
)

extension1007 = FleetTriggerExtension1007.objects.create(
    seconds = 300,
    account = account
)
extension1007.geofences.set(geofences)
extension1007.save()

trigger.extension1007 = extension1007
trigger.save()

# PARADAS POR 3 MINUTOS

account = Account.objects.get(name='civa')
#account = Account.objects.get(name='pruebas')
geofences = Geofence.objects.filter(account=account)
geofences = geofences.filter(
    Q(name = 'km 119') |
    Q(name = 'km 125') |
    Q(name = 'km 130') |
    Q(name = 'km 132') |
    Q(name = 'km 140') |
    Q(name = 'km 42') |
    Q(name = 'km 47') |
    Q(name = 'KM 50') |
    Q(name = 'KM 52') |
    Q(name = 'KM 55') |
    Q(name = 'KM 57') |
    Q(name = 'KM 58') |
    Q(name = 'KM 58.6') |
    Q(name = 'KM 63') |
    Q(name = 'KM 65') |
    Q(name = 'KM 66') |
    Q(name = 'KM 68') |
    Q(name = 'KM 69') |
    Q(name = 'KM 72') |
    Q(name = 'KM 74') |
    Q(name = 'KM 76') |
    Q(name = 'KM 77') |
    Q(name = 'KM 79') |
    Q(name = 'KM 80') |
    Q(name = 'KM 81') |
    Q(name = 'KM 83') |
    Q(name = 'KM 84') |
    Q(name = 'KM 87') |
    Q(name = 'KM 89') |
    Q(name = 'KM 90') |
    Q(name = 'KM 99') |
    Q(name = 'Km. 102') |
    Q(name = 'Km. 106') |
    Q(name = 'Km. 107') |
    Q(name = 'Km. 111') |
    Q(name = 'Km. 113') |
    Q(name = 'Km. 116') |
    Q(name = 'Km. 119') |
    Q(name = 'Km. 130') |
    Q(name = 'Km. 76') |
    Q(name = 'Km. 98') |
    Q(name = 'Km. 99') |
    Q(name = 'La Oroya') |
    Q(name = 'Marcavalle Carr. Central') |
    Q(name = 'Mercado las Delicias 1') |
    Q(name = 'MINA  MINSUR') |
    Q(name = 'MODULO Q') |
    Q(name = 'PARADA PROHIBIDA ACAPULCO') |
    Q(name = 'PE-1N ANCASH N-S 1 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 10 - 60 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 11 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 12 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 2 - 60 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 3 - 60 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 4 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 5 - 60 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 6 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 7 - 90 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 8 - 60 KM/H') |
    Q(name = 'PE-1N ANCASH N-S 9 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH S-N 1 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH S-N 2 - 60 KM/H') |
    Q(name = 'PE-1N ANCASH S-N 3 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH S-N 4 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH S-N 5 - 80 KM/H') |
    Q(name = 'PE-1N ANCASH S-N 6 - 80 KM/H') |
    Q(name = 'PE-1N LA LIBERTAD N-S 1 - 60 KM/H') |
    Q(name = 'PE-1N LA LIBERTAD N-S 2 - 80 KM/H') |
    Q(name = 'PE-1N LA LIBERTAD S-N 1 - 80 KM/H') |
    Q(name = 'PE-1N LA LIBERTAD S-N 2 - 80 KM/H') |
    Q(name = 'PE-1N LA LIBERTAD S-N 3 - 80 KM/H') |
    Q(name = 'PE-1N LA LIBERTAD S-N 4 - 80 KM/H') |
    Q(name = 'PE-1N LA LIBERTAD S-N 5 - 60 KM/H') |
    Q(name = 'PE-1N LA LIBERTAD S-N 6 - 80 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 1 - 80 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 10 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 11 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 12 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 13 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 14 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 15 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 16 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 17 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 18 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 19 - 40 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 2 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 20 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 21 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 22 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 23 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 24 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 25 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 26 - 45 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 27 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 28 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 29 - 45 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 3 - 80 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 30 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 31 - 45 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 32 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 33 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 34 - 80 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 35 - 80 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 36 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 37 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 4 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 5 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 6 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 7 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 8 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) N-S 9 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 1 - 80 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 10 - 45 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 11 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 12 - 40 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 15 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 17 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 18 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 19 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 2 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 20 - 80 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 21 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 22 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 23 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 24 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 25 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 26 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 27 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 28 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 29 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 30 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 31 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 32 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 33 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 34 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 4 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 5 - 45 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 6 - 60 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 7 - 55 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 8 - 45 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 9 - 60 KM/H') |
    Q(name = 'PE-1S AREQUIPA N-S 1 - 35 KM/H') |
    Q(name = 'PE-1S AREQUIPA S-N 1 - 35 KM/H') |
    Q(name = 'PE-1S AREQUIPA S-N 2 - 35 KM/H') |
    Q(name = 'PE-1SE ICA N-S 1 - 90 KM/H') |
    Q(name = 'PE-1SE ICA N-S 2 - 70 KM/H') |
    Q(name = 'PE-1SE ICA N-S 3 - 80 KM/H') |
    Q(name = 'PE-1SE ICA N-S 4 - 70 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 1 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 10 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 11 - 40 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 12 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 13 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 14 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 15 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 16 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 17 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 18 - 40 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 19 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 2 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 3 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 4 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 5 - 40 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 7 - 40 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 8 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN E-O 9 - 40 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 1 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 10 - 40 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 11 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 12 - 40 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 13 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 14 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 15 - 40 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 17 - 60 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 18 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 2 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 3 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 4 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 5 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 6 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 7 - 50 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 8 - 35 KM/H') |
    Q(name = 'PE-22 LIMA (ESTE) y JUNIN O-E 9 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 1 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 10 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 11 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 12 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 2 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 3 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 4 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 5 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 6 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 7 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 8 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN N-S 9 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 1 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 10 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 11 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 12 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 13 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 2 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 3 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 4 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 5 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 6 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 7 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 8 - 35 KM/H') |
    Q(name = 'PE-3N PASCO y JUNIN S-N 9 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 1 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 10 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 11 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 12 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 13 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 14 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 15 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 16 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 17 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 2 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 3 - 50 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 4 - 30 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 5 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 6 - 50 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 7 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 8 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN N-S 9 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 1 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 10 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 11 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 12 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 13 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 14 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 15 - 50 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 16 - 50 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 17 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 18 - 50 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 2 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 3 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 4 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 5 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 6 - 50 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 7 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 8 - 35 KM/H') |
    Q(name = 'PE-3S JUNIN S-N 9 - 35 KM/H') |
    Q(name = 'PE-3S PUNO N-S 1 - 35 KM/H') |
    Q(name = 'PE-3S PUNO N-S 2 - 35 KM/H') |
    Q(name = 'PE-3S PUNO N-S 3 - 35 KM/H') |
    Q(name = 'PE-3S PUNO S-N 1 - 35 KM/H') |
    Q(name = 'PE-3S PUNO S-N 2 - 35 KM/H') |
    Q(name = 'PE-3SB JUNIN N-S 1 - 35 KM/H') |
    Q(name = 'PE-3SB JUNIN N-S 2 - 35 KM/H') |
    Q(name = 'PE-3SB JUNIN N-S 3 - 35 KM/H') |
    Q(name = 'PE-3SB JUNIN N-S 4 - 80 KM/H') |
    Q(name = 'PE-3SB JUNIN N-S 5 - 35 KM/H') |
    Q(name = 'PE-3SB JUNIN S-N 1 - 35 KM/H') |
    Q(name = 'PE-3SB JUNIN S-N 2 - 35 KM/H') |
    Q(name = 'PE-3SB JUNIN S-N 3 - 35 KM/H') |
    Q(name = 'PE-3SB JUNIN S-N 4 - 50 KM/H') |
    Q(name = 'PE-3SB JUNIN S-N 5A - 35 KM/H') |
    Q(name = 'PE-3SB JUNIN S-N 5B - 35 KM/H') |
    Q(name = 'PUENTE NUEVO') |
    Q(name = 'PUENTE STUART-MARGEN DERECHO') |
    Q(name = 'Restaurant El Real') |
    Q(name = 'ruta 1') |
    Q(name = 'Av. Central 1') |
    Q(name = 'chaclacayo') |
    Q(name = 'CHACLAYO') |
    Q(name = 'CHOSICA') |
    Q(name = 'Control Fundicion Ilo') |
    Q(name = 'Control Mocupe') |
    Q(name = 'Cruce Bayovar') |
    Q(name = 'Cruce Ventanilla') |
    Q(name = 'EXCESO COLEGIO HUARAL') |
    Q(name = 'EXCESO CRUCE HUARAL') |
    Q(name = 'EXCESO PEAJE ANCON') |
    Q(name = 'EXCESO SUBIDA TORO') |
    Q(name = 'HOSPITAL REGIONAL') |
    Q(name = 'KM 100') |
    Q(name = 'KM 102') |
    Q(name = 'KM 107') |
    Q(name = 'km 113') |
    Q(name = 'km 116') |
    Q(name = 'PE-1N ANCASH N-S 13 - 80 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 13 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 14 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 16 - 90 KM/H') |
    Q(name = 'PE-1N LIMA (NORTE) S-N 3 - 80 KM/H') |
    Q(name = 'Tramo 32: Humay') |
    Q(name = 'HUALAPAMPA - LA VICTORIA') |
    Q(name = 'CHASQUITAMBO PUNTO DE CONTROL') |
    Q(name = 'HUACHO')
)

for geofence in geofences:
    print(geofence.name)
    #print(geofence.description)
    print('==================')

print(len(geofences))

trigger = FleetTrigger.objects.create(
    name = "ALERTA DE PARADA 3MIN",
    description = "3 MINUTOS DETENIDO",
    alert_type = 1007,
    is_active = True,
    send_notification = True,
    send_mail_notification = True,
    account = account
)

extension1007 = FleetTriggerExtension1007.objects.create(
    seconds = 180,
    account = account
)
extension1007.geofences.set(geofences)
extension1007.save()

trigger.extension1007 = extension1007
trigger.save()