import json

#Excepción Personalizada
class StockInvalidoError(Exception):
    """
    Excepción lanzada cuando se intenta asignar un stock negativo.

    """
    def __init__(self, mensaje="El stock no puede ser un valor negativo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

#Clase Base
class DispositivoEcologico:
    """
    Clase base para los productos ecológicos del catálogo.

    """
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self._stock = 0        
        self.stock = stock     # Pasa por el setter para validarse al instanciar

    # Encapsulamiento explícito usando properties
    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor)->None:

        """
        Asigna un nuevo stock al producto.

        Raises:
            StockInvalidoError: Si el valor es negativo se lanza una excepción.
        """
        if valor < 0:
            raise StockInvalidoError(f"Error de Negocio: Intento de asignar stock negativo ({valor}) al producto '{self.nombre}'.")
        self._stock = valor

    def ficha_tecnica(self) -> str:
        """
        Devuelve la ficha técnica comercial del producto ecológico.

        """
        return f"[{self.codigo}] {self.nombre} - Precio: ${self.precio} - Stock: {self.stock} uds."

    def to_dict(self) -> dict:
        """
        Este devuelve el diccionario con los datos del producto para el json.

        """
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

#Clase Especializada

class PanelSolar(DispositivoEcologico):
    """
    Clase especializada para los paneles solares.

    """
    def __init__(self, codigo, nombre, precio, stock, potencia_w, eficiencia):
        super().__init__(codigo, nombre, precio, stock)
        self.potencia_w = potencia_w
        self.eficiencia = eficiencia

    # Polimorfismo: se sobreescibe el método para personalizar la ficha
    def ficha_tecnica(self)->str: 
        """
        Devuelve la ficha técnica comercial del panel solar.

        """
      
        base = super().ficha_tecnica()
        return f"{base} | Potencia: {self.potencia_w}W | Eficiencia: {self.eficiencia}%"

    def to_dict(self)->dict:
        """
        Este devuelve el diccionario con los datos del producto para el json.

        """
        # Extendemos el diccionario base
        data = super().to_dict()
        data.update({
            "potencia_w": self.potencia_w,
            "eficiencia": self.eficiencia
        })
        return data

#Persistencia y Gestión-B

class GestorInventario:
    """
    Gestiona la persistencia del catálogo de dispositivos ecológicos.
    """
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos:list[DispositivoEcologico], ruta_archivo:str):
        """
        guarda el catalago en formato json.

        Args:
            lista_dispositivos: Dispositivos que se van a guardar.
            ruta_archivo: Ruta del archivo, por defecto "catalogo_ecotech.json".
        """

        # Serializamos la lista de objetos usando comprensión de listas y el método to_dict
        datos_serializados = [dispositivo.to_dict() for dispositivo in lista_dispositivos]
        
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos_serializados, archivo, indent=4, ensure_ascii=False)
        print(f"-> Catálogo exportado exitosamente en el archivo: '{ruta_archivo}'.")

# Bloque de Prueba (Simulación del programa)

if __name__ == "__main__":
    # Estilos de color ANSI para la terminal
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    CYAN    = "\033[96m"
    RED     = "\033[91m"
    GRAY    = "\033[90m"
    
    catalogo_valido = []
    print(f"\n{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║                     - ECOTECH SOLUTIONS - GESTIÓN DE CATÁLOGO -                  ║{RESET}")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════════════════════════════╝{RESET}\n")
    #el cartelito me lo paso un amigo para mejorar las vistas. jejee

    print(f"{BOLD}{BLUE}▶ 1. CARGA DE PRODUCTOS VÁLIDOS{RESET}")
    print(f"{GRAY}────────────────────────────────────────────────────────────────────────────────────{RESET}")
    try:
        panel_1 = PanelSolar("PS-001", "Panel Pro", 250000.0, 10, 450, 21.5)
        catalogo_valido.append(panel_1)
        print(panel_1.ficha_tecnica())
        
        panel_2 = PanelSolar("PS-002", "Panel Flexible Eco", 120000.0, 5, 150, 18.0)
        catalogo_valido.append(panel_2)
        print(panel_2.ficha_tecnica())
    except StockInvalidoError as e:
        print(e)

    print(f"\n{BOLD}{YELLOW}▶ 2. AUDITORÍA DE INVENTARIO (VALIDACIÓN DE STOCK NEGATIVO){RESET}")
    print(f"{GRAY}────────────────────────────────────────────────────────────────────────────────────{RESET}")
    try:
        # Intentamos instanciar un producto con stock -3
        panel_invalido = PanelSolar("PS-003", "Panel Defectuoso", 90000.0, -3, 100, 15.0)
        catalogo_valido.append(panel_invalido)
    except StockInvalidoError as e:
        print("¡Excepción capturada correctamente!")
        print(f"Detalle: {e}")

    print(f"\n{BOLD}{CYAN}▶ 3. PERSISTENCIA DE DATOS{RESET}")
    print(f"{GRAY}────────────────────────────────────────────────────────────────────────────────────{RESET}")
    # Guardamos solo los paneles que pasaron la validación
    GestorInventario.guardar_catalogo_json(catalogo_valido, "catalogo_ecotech.json")