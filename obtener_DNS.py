import dns.resolver

def main():
    url = input("Ingrese el URL o dominio --> : ")
    tipos_registros = ["A", "AAAA", "NS", "MX", "TXT"]  
    for tipo in tipos_registros:
        try:
            respuestas = dns.resolver.resolve(url, tipo)
            print(f"\nRegistros {tipo} para {url}:")
            for rdata in respuestas:
                print(rdata.to_text())
        except dns.resolver.NoAnswer:
            print(f"No hay respuesta para tipo {tipo}")
        except dns.resolver.NXDOMAIN:
            print("Dominio no encontrado")
            break
        except Exception as e:
            print(f"No pude obtener la información para {tipo}: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nEjecutado interrupción por usuario. Saliendo...")
        exit()
