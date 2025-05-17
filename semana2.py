#✈️ Sistema de Gestión y Costeo de Equipaje Aéreo

import datetime

def generar_id_compra(num_compras):
    """Genera un ID de compra único."""
    return f"COMP{num_compras:04d}"

def calcular_precio_base(tipo_viaje):
    """Devuelve el precio base según el tipo de viaje."""
    precios = {
        "nacional": 230000,
        "internacional": 4200000
    }
    return precios.get(tipo_viaje.lower(), 0)

def calcular_costo_equipaje(peso):
    """Calcula el costo adicional por el peso del equipaje principal."""
    if peso <= 20:
        return 50000
    elif peso <= 30:
        return 70000
    elif peso <= 50:
        return 110000
    else:
        return None  # No admitido

def registrar_reserva(reservas, num_compras):
    """Registra una nueva reserva."""
    nombre = input("Nombre del pasajero: ")
    tipo_viaje = input("Tipo de viaje (nacional/internacional): ").strip().lower()
    peso_equipaje_principal = float(input("Peso del equipaje principal (kg): "))
    
    if peso_equipaje_principal > 50:
        print("Equipaje no admitido. Debe cancelar o viajar sin equipaje.")
        return

    equipaje_mano = input("¿Lleva equipaje de mano? (sí/no): ").strip().lower()
    peso_equipaje_mano = 0
    if equipaje_mano == "sí":
        peso_equipaje_mano = float(input("Peso del equipaje de mano (kg): "))
        if peso_equipaje_mano > 13:
            print("Equipaje de mano rechazado, pero puede seguir viajando.")
            peso_equipaje_mano = 0  # Rechazado

    fecha_viaje = input("Fecha del viaje (YYYY-MM-DD): ")
    fecha_viaje = datetime.datetime.strptime(fecha_viaje, "%Y-%m-%d").date()

    precio_base = calcular_precio_base(tipo_viaje)
    costo_equipaje = calcular_costo_equipaje(peso_equipaje_principal)

    if costo_equipaje is None:
        return  # No se puede registrar la reserva

    total_a_pagar = precio_base + costo_equipaje
    id_compra = generar_id_compra(num_compras)

    reservas[id_compra] = {
        'nombre': nombre,
        'tipo_viaje': tipo_viaje,
        'peso_equipaje_principal': peso_equipaje_principal,
        'peso_equipaje_mano': peso_equipaje_mano,
        'fecha_viaje': fecha_viaje,
        'costo_total': total_a_pagar
    }

    print(f"\nReserva registrada con éxito. ID de compra: {id_compra}")
    print(f"Costo total del viaje: ${total_a_pagar}")

def mostrar_reserva(reservas, id_compra):
    """Muestra los detalles de una reserva por ID."""
    reserva = reservas.get(id_compra)
    if reserva:
        print(f"\nID de compra: {id_compra}")
        print(f"Nombre del pasajero: {reserva['nombre']}")
        print(f"Tipo de viaje: {reserva['tipo_viaje']}")
        print(f"Fecha del viaje: {reserva['fecha_viaje']}")
        print(f"Peso del equipaje principal: {reserva['peso_equipaje_principal']} kg")
        print(f"Peso del equipaje de mano: {reserva['peso_equipaje_mano']} kg")
        print(f"Costo total del viaje: ${reserva['costo_total']}")
    else:
        print("ID de compra no encontrado.")

def reporte_final(reservas):
    """Genera un reporte final de las reservas."""
    total_recaudado = sum(reserva['costo_total'] for reserva in reservas.values())
    total_pasajeros = len(reservas)
    nacionales = sum(1 for reserva in reservas.values() if reserva['tipo_viaje'] == 'nacional')
    internacionales = total_pasajeros - nacionales

    print(f"\nTotal recaudado: ${total_recaudado}")
    print(f"Número total de pasajeros procesados: {total_pasajeros}")
    print(f"Número de pasajeros nacionales: {nacionales}")
    print(f"Número de pasajeros internacionales: {internacionales}")

