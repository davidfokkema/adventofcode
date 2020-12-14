def parse_boarding_pass(boarding_pass):
    table = str.maketrans({"F": "0", "B": "1", "L": "0", "R": "1"})
    boarding_pass_binary = boarding_pass.translate(table)

    row_code, column_code = boarding_pass_binary[:7], boarding_pass_binary[7:]
    row = int(row_code, 2)
    column = int(column_code, 2)
    seat_id = int(boarding_pass_binary, 2)

    return row, column, seat_id


def find_empty_seat(seat_ids):
    for seat_id in range(min(seat_ids), max(seat_ids)):
        if seat_id not in seat_ids:
            if seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
                break
    else:
        print("Uhoh, I can't find my seat!")
    return seat_id


if __name__ == "__main__":
    print(parse_boarding_pass("BFFFBBFRRR"))
    print(parse_boarding_pass("FFFBBBFRRR"))
    print(parse_boarding_pass("BBFFBBFRLL"))

    with open("2020/inputs/day5.txt") as f:
        boarding_passes = [l.strip() for l in f]

    seat_ids = [parse_boarding_pass(p)[2] for p in boarding_passes]
    print(f"Highest seat ID is {max(seat_ids)}")

    print(f"My seat is {find_empty_seat(seat_ids)}")

    # Much simpler:
    all_seat_ids = set(range(min(seat_ids), max(seat_ids) + 1))
    print(f"My seat is {all_seat_ids - set(seat_ids)}")
