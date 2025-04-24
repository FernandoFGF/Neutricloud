# meetings_actions.py

import paramiko
from PySide6.QtCore import QDate
from utils.utils import update_label_data

def get_next_friday():
    today = QDate.currentDate()
    day_of_week = today.dayOfWeek()  # Obtiene el día de la semana (1=Monday, 2=Tuesday, ..., 7=Sunday)
    
    if day_of_week != 5:  # Si no es viernes
        # Calcula la diferencia de días hasta el próximo viernes
        days_to_friday = (5 - day_of_week + 7) % 7
        if days_to_friday == 0:  # Si el día es hoy viernes, mantenemos la fecha de hoy
            days_to_friday = 7
        next_friday = today.addDays(days_to_friday)
    else:
        next_friday = today  # Si hoy es viernes, mantenemos la fecha de hoy
    
    return next_friday

def insert_meeting(self, lines, year, month, new_entry):
    """Inserta la reunión en la sección correcta del archivo."""
    year_header = f"===== {year} =====\n"
    month_header = f"=== {month} ===\n"

    meeting_entry = new_entry

    # Verificar si la reunión ya está en el archivo
    if meeting_entry in lines:
        update_label_data(self, "⚠️ La reunión ya existe en el archivo.")  # El primer argumento puede ser None si no es necesario acceder a una instancia
        #print("⚠️ La reunión ya existe en el archivo.")
        return lines

    updated_lines = []
    year_found = False
    month_found = False
    inserted = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Verificar si el año existe, si no, agregarlo
        if line.strip() == year_header.strip() and not year_found:
            year_found = True
            updated_lines.append(line)
            i += 1
            continue

        # Si el año no existe, agregarlo antes de la primera sección
        if not year_found and "=====" in line:
            updated_lines.append("\n")  # Agregar dos líneas vacías antes
            updated_lines.append(year_header)
            updated_lines.append("\n")
            year_found = True
            continue

        # Verificar si el mes existe dentro del año
        if year_found and line.strip() == month_header.strip() and not month_found:
            month_found = True
            updated_lines.append(line)
            i += 1
            continue

        # Si el mes no existe, agregarlo después del año
        if year_found and not month_found and "===" in line:
            updated_lines.append("\n")  # Agregar un retorno de carro para separar
            updated_lines.append(month_header)
            updated_lines.append("\n")
            month_found = True
            continue

        # Si el mes existe, verificar si la reunión ya está registrada
        if month_found and meeting_entry not in updated_lines:
            updated_lines.append(meeting_entry)  # Solo agregar la entrada de la reunión una vez
            inserted = True

        # Agregar la línea de contenido normal
        updated_lines.append(line)
        i += 1

    # Si no se encontró el mes ni el año, agregarlos al final
    if not month_found:
        updated_lines.append(month_header)
        updated_lines.append(meeting_entry)
        updated_lines.append("\n")

    if not year_found:
        updated_lines.append(year_header)
        updated_lines.append(month_header)
        updated_lines.append(meeting_entry)
        updated_lines.append("\n")

    return updated_lines


def createMeeting(self):
    """Añade una nueva reunión en el archivo remoto y crea el archivo de la próxima reunión con su fecha."""
    remote_path = "/var/www/wiki/data/pages/start/group_meetings.txt"
    local_path = "group_meetings_temp.txt"

    # Obtener la fecha del próximo viernes
    next_friday = get_next_friday()
    year = next_friday.toString("yyyy")
    month = next_friday.toString("MMMM")  # Nombre del mes completo en inglés
    date_str = next_friday.toString("yyyy_MM_dd")  # Formato 2025_04_05
    display_date = next_friday.toString("yyyy-MM-dd")  # Formato 2025-04-05

    new_entry = f"  * [[:start:group_meetings:{date_str} | {display_date}]]\n"

    # Definir la ruta del archivo basado en la fecha
    next_friday_filename = f"{date_str}.txt"
    next_friday_path = f"/var/www/wiki/data/pages/start/group_meetings/{next_friday_filename}"
    local_next_friday_path = next_friday_filename

    # Contenido del archivo de la reunión específica
    next_friday_content = f"""\
====== Group Meeting {display_date} ======

----

=== LAB ===

=== SIMULATIONS ===

=== ANALYSIS / RECONSTRUCTION ===

=== SBND COMMISSIONING ===

=== OTHERS ===
"""

    # Conectarse por SSH
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, username=self.user, password=self.password)
        ssh.exec_command("umask 002")  # Establece el umask para crear archivos con permisos 664

        sftp = ssh.open_sftp()

        # Descargar el archivo de reuniones
        sftp.get(remote_path, local_path)

        # Leer y modificar el archivo
        with open(local_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        modified_lines = insert_meeting(self, lines, year, month, new_entry)

        # Si las líneas han cambiado, actualizar el archivo en el servidor
        if modified_lines != lines:
            with open(local_path, "w", encoding="utf-8") as f:
                f.writelines(modified_lines)

            sftp.put(local_path, remote_path)
            update_label_data(self, "✅ Reunión añadida correctamente.")

            # Crear el archivo de la próxima reunión con la fecha específica
            with open(local_next_friday_path, "w", encoding="utf-8") as f:
                f.write(next_friday_content)

            # Subir el archivo con el nombre basado en la fecha
            sftp.put(local_next_friday_path, next_friday_path)
            update_label_data(self, f"✅ Archivo {next_friday_filename} creado correctamente.")
            
            # Comando para cambiar la propiedad del archivo al grupo www-data
            change_group_command = f"chown :www-data {next_friday_path}"
            
            # Comando para darle permisos de escritura al grupo www-data
            change_permissions_command = f"chmod 664 {next_friday_path}"

            # Ejecutar los comandos en el servidor remoto
            stdin, stdout, stderr = ssh.exec_command(change_group_command)
            stdout.channel.recv_exit_status()  # Esperar a que el comando termine
            
            # Dar permisos de escritura al grupo
            stdin, stdout, stderr = ssh.exec_command(change_permissions_command)
            stdout.channel.recv_exit_status()  # Esperar a que el comando termine

        # Cerrar conexiones
        sftp.close()
        ssh.close()

    except Exception as e:
        update_label_data(self, f"❌ Error al actualizar el archivo: {e}")
