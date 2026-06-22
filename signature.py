import hmac
import hashlib

def get_nested_value(d: dict, path: str):
    """
    Obtiene un valor anidado en un diccionario usando una ruta separada por puntos (ej. 'transaction.id').
    """
    keys = path.split('.')
    val = d
    for key in keys:
        if isinstance(val, dict) and key in val:
            val = val[key]
        else:
            return None
    return val

def verify_event_checksum(
    transaction_data: dict,
    signature_properties: list[str],
    checksum: str,
    timestamp: int,
    secret: str
) -> bool:
    """
    Verifica la firma (checksum) de un webhook de Wompi.
    Retorna True si la firma coincide (origen legítimo), False en caso contrario.
    """
    # Usamos un generador en lugar de una lista para ahorrar memoria.
    # El operador walrus (:=) nos ayuda a evitar que un valor nulo se convierta en el texto literal "None".
    signature_string = "".join(
        str(val) if (val := get_nested_value(transaction_data, prop)) is not None else ""
        for prop in signature_properties
    ) + f"{timestamp}{secret}"

    calculated = hashlib.sha256(signature_string.encode("utf-8")).hexdigest()

    # compare_digest es ideal para prevenir ataques de tiempo (timing attacks)
    return hmac.compare_digest(calculated, checksum)