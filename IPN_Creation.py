import xml.etree.ElementTree as ET  # Importa la librería para trabajar con XML
import csv  # Importa la librería para leer archivos CSV

def xml_Creation(archivo_entrada):
    try:
        # Abre el archivo CSV con codificación UTF-8
        with open(archivo_entrada, encoding='utf8') as cvfile:
            spamreader = csv.reader(cvfile, delimiter=';')  # Lee el CSV usando ';' como delimitador

            # Intenta saltar la primera fila (el encabezado del CSV)
            try:
                next(spamreader, None)  # Saltar la fila de encabezado
            except StopIteration:
                print("El archivo CSV está vacío.")  # Si no hay filas, muestra un mensaje
                return  # Termina la función si el archivo CSV está vacío

            # Crea el elemento raíz del archivo XML
            root = ET.Element('IPD-UPLOAD')

            # Agrega elementos dentro del XML, como 'HEADER' y subelementos
            doc = ET.SubElement(root, "HEADER")
            doc1 = ET.SubElement(doc, "USER-NAME")
            doc1.text = 'NOMBRE DE USUARIO'  # Texto para el nombre de usuario
            doc2 = ET.SubElement(doc, "PASSWD")
            doc2.text = 'PASSWORD'  # Texto para la contraseña
            doc3 = ET.SubElement(doc, "UPLOADING-SOCIETY")
            doc3.text = 'NOMBRE_SOCIEDAD'  # Texto para la sociedad de carga
            doc4 = ET.SubElement(doc, "FILE-ID")
            doc4.text = '#'  # ID del archivo
            doc5 = ET.SubElement(doc, "ISO-CHAR-SET")
            doc5.text = 'ISO8859-1'  # Formato de codificación del archivo

            # Crea un contenedor para los titulares de derechos (RIGHTHOLDER)
            doc0 = ET.SubElement(root, "RIGHTHOLDERS")

            # Recorre cada fila del archivo CSV
            for row in spamreader:
                # Crea un nuevo elemento RIGHTHOLDER para cada fila en el CSV
                doc01 = ET.SubElement(doc0, "RIGHTHOLDER")
                
                # Agrega subelementos para RIGHTHOLDER con valores del CSV
                doc11 = ET.SubElement(doc01, "ACTION")
                doc11.text = 'INSERT'  # Indica la acción a realizar (en este caso, insertar)
                
                # Agrega información del titular de derechos tomada de la fila actual del CSV
                doc182 = ET.SubElement(doc01, "IPN")
                doc182.text = row[6]  # Número de identificación del titular de derechos
                
                doc12 = ET.SubElement(doc01, "RIGHTHOLDER-LOCAL-ID")
                doc12.text = row[7]  # ID local del titular
                
                doc13 = ET.SubElement(doc01, "RIGHTHOLDER-FIRST-NAME")
                doc13.text = row[8]  # Nombre del titular
                
                doc14 = ET.SubElement(doc01, "RIGHTHOLDER-LAST-NAME")
                doc14.text = row[9]  # Apellido del titular
                
                doc15 = ET.SubElement(doc01, "SEX")
                doc15.text = row[10]  # Sexo del titular
                
                doc16 = ET.SubElement(doc01, "DATE-OF-BIRTH")
                doc16.text = row[11]  # Fecha de nacimiento del titular
                
                doc17 = ET.SubElement(doc01, "COUNTRY-OF-BIRTH")
                doc17.text = row[12]  # País de nacimiento del titular
                
                doc18 = ET.SubElement(doc01, "COUNTRY-OF-RESIDENCE")
                doc18.text = row[13]  # País de residencia del titular
                
                # Si la columna IDENTIFYING-ROLE-CODE no está vacía
                if row[14] != '':
                    doc19 = ET.SubElement(doc01, "IDENTIFYING-ROLES")  # Crea un contenedor para roles
    
                # Separa por comas (o espacios adicionales después de la coma)
                substrings = [role.strip() for role in row[14].split(',')]
    
                for substring in substrings:
                    if substring:  # Verifica que no sea una cadena vacía
                        role_code = ET.SubElement(doc19, "IDENTIFYING-ROLE-CODE")
                        role_code.text = substring  # Agrega cada rol como un subelemento

                instruments = ET.SubElement(doc01, "INSTRUMENTS")
                # Verifica si hay información de tipo de instrumento o información del instrumento
                # Crea el elemento INSTRUMENT dentro de INSTRUMENTS
                instrument = ET.SubElement(instruments, "INSTRUMENT")
    
                # Agrega el tipo de instrumento si está presente
                if row[15] != '':
                    doc20 = ET.SubElement(instrument, "INSTRUMENT-TYPE")
                    doc20.text = row[15].strip()  # Tipo de instrumento

                # Agrega información del instrumento si está presente
                if row[16] != '':
                    doc21 = ET.SubElement(instrument, "INSTRUMENT-INFO")
                    doc21.text = row[16].strip()  # Información sobre el instrumento

                main_artists = ET.SubElement(doc01, "MAIN-ARTISTS")

                main_artist = ET.SubElement(main_artists, "MAIN-ARTIST")
    

                doc20 = ET.SubElement(main_artist, "MAIN-ARTIST-NAME")
                doc20.text = row[17].strip()

                doc21 = ET.SubElement(main_artist, "IMAN")
                doc21.text = row[18].strip()

                doc21 = ET.SubElement(main_artist, "MAIN-ARTIST-JOIN-DATE")
                doc21.text = row[19].strip()

                doc21 = ET.SubElement(main_artist, "MAIN-ARTIST-LEAVE-DATE")
                doc21.text = row[20].strip()
                    

                # Si la columna PSEUDONAMES no está vacía
                if row[21] != '':
                    doc26 = ET.SubElement(doc01, "PSEUDONAMES")  # Crea un contenedor para seudónimos
                    if ',' in row[21]:
                        substrings = row[21].split(',')
                        for substring in substrings:
                            pseudoname = ET.SubElement(doc26, "PSEUDONAME")
                            pseudoname.text = substring.strip()  # Agrega cada seudónimo
                    else:
                        pseudoname = ET.SubElement(doc26, "PSEUDONAME")
                        pseudoname.text = row[21].strip()  # Agrega un único seudónimo

    except FileNotFoundError:
        print(f"El archivo {archivo_entrada} no se encontró.")  # Mensaje si no se encuentra el archivo CSV
    except Exception as e:
        print(f"Ocurrió un error: {e}")  # Maneja otros errores durante la lectura o procesamiento del archivo
    else:
        try:
            # Guarda el archivo XML generado en la ubicación especificada
            tree = ET.ElementTree(root)
            tree.write('RUTA_XML', encoding='UTF-8', xml_declaration=True)
            print("Archivo XML exportado exitosamente.")  # Mensaje de éxito
        except Exception as e:
            print(f"Ocurrió un error al guardar el archivo XML: {e}")  # Maneja errores al guardar el archivo XML

# Llamada a la función
xml_Creation('RUTA_CSV')  # Ejecuta la función con el archivo CSV especificado
