def read_log_file(file_path):
    parsed_logs = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(" ", 3)

            log = {
                "date": parts[0],
                "time": parts[1],
                "level": parts[2],
                "message": parts[3]
            }

            parsed_logs.append(log)

    return parsed_logs




