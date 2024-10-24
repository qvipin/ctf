import struct
import socket
import datetime

def parse_sky_log(file_path):
    with open(file_path, 'rb') as f:
        # Read magic bytes (8 bytes)
        magic_bytes = f.read(8)
        if magic_bytes != b'\x91SKY\r\n\x1a\n':
            raise ValueError("Invalid SKY log file format.")

        # Read version (1 byte)
        version = struct.unpack('>B', f.read(1))[0]
        if version != 1:
            raise ValueError("Unsupported version.")

        # Read creation timestamp (4 bytes)
        creation_timestamp = struct.unpack('>I', f.read(4))[0]
        creation_time_utc = datetime.datetime.utcfromtimestamp(creation_timestamp)

        # Read hostname length (4 bytes)
        hostname_length = struct.unpack('>I', f.read(4))[0]

        # Read hostname (dynamic length)
        hostname = f.read(hostname_length).decode('utf-8') if hostname_length > 0 else None

        # Read flag length (4 bytes)
        flag_length = struct.unpack('>I', f.read(4))[0]

        # Read flag (dynamic length)
        flag = f.read(flag_length).decode('utf-8') if flag_length > 0 else None

        # Read the number of entries (4 bytes)
        num_entries = struct.unpack('>I', f.read(4))[0]

        entries = []
        ip_data_count = {}

        total_bytes_transferred = 0

        for _ in range(num_entries):
            # Read source IP (4 bytes)
            src_ip_int = struct.unpack('>I', f.read(4))[0]
            src_ip = socket.inet_ntoa(struct.pack('>I', src_ip_int))

            # Read destination IP (4 bytes)
            dest_ip_int = struct.unpack('>I', f.read(4))[0]
            dest_ip = socket.inet_ntoa(struct.pack('>I', dest_ip_int))

            # Read timestamp (4 bytes)
            timestamp = struct.unpack('>I', f.read(4))[0]
            timestamp_utc = datetime.datetime.utcfromtimestamp(timestamp)

            # Read bytes transferred (4 bytes)
            bytes_transferred = struct.unpack('>I', f.read(4))[0]
            total_bytes_transferred += bytes_transferred

            # Track data per IP for later analysis
            for ip in (src_ip, dest_ip):
                if ip not in ip_data_count:
                    ip_data_count[ip] = 0
                ip_data_count[ip] += bytes_transferred

            # Store entry data
            entries.append({
                'src_ip': src_ip,
                'dest_ip': dest_ip,
                'timestamp': timestamp_utc,
                'bytes_transferred': bytes_transferred
            })

        return {
            'hostname': hostname,
            'flag': flag,
            'creation_time_utc': creation_time_utc,
            'num_entries': num_entries,
            'total_bytes_transferred': total_bytes_transferred,
            'ip_data_count': ip_data_count,
            'entries': entries
        }

def analyze_log(file_path):
    log_data = parse_sky_log(file_path)

    # Q1: Hostname of the server
    print(f"Hostname of the server: {log_data['hostname']}")

    # Q2: Plaintext flag in the log file
    print(f"Plaintext flag in the log file: {log_data['flag']}")

    # Q3: Date file was created (UTC)
    print(f"Date file was created (UTC): {log_data['creation_time_utc']}")

    # Q4: Number of entries
    print(f"Number of entries: {log_data['num_entries']}")

    # Q5: Total transferred bytes
    print(f"Total transferred bytes: {log_data['total_bytes_transferred']}")

    # Q6: Number of unique IP addresses (both senders and receivers)
    unique_ips = set()
    for entry in log_data['entries']:
        unique_ips.add(entry['src_ip'])
        unique_ips.add(entry['dest_ip'])
    print(f"Number of unique IP addresses: {len(unique_ips)}")

    # Q7: IP address that sent the most data
    max_ip = max(log_data['ip_data_count'], key=log_data['ip_data_count'].get)
    print(f"IP address that sent the most data: {max_ip}")

    # Q8: Total bytes sent by the IP address that sent the most data
    total_bytes_sent_by_max_ip = sum(entry['bytes_transferred'] for entry in log_data['entries'] if entry['src_ip'] == max_ip)
    print(f"Total bytes sent by {max_ip}: {total_bytes_sent_by_max_ip}")

    # Q9: Busiest day (most bytes transferred)
    day_data = {}
    for entry in log_data['entries']:
        day = entry['timestamp'].date()
        if day not in day_data:
            day_data[day] = 0
        day_data[day] += entry['bytes_transferred']

    busiest_day = max(day_data, key=day_data.get)
    print(f"Busiest day (most bytes transferred): {busiest_day}")

# Example usage
log_file = "cff.sky"  # Replace with your actual log file path
analyze_log(log_file)
