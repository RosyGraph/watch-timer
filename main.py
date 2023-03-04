import datetime
from pathlib import Path as P


def main():
    input("Press Enter when your watch's second hand is on 12.")
    now = datetime.datetime.now()
    minute = int(input("What minute is it? "))
    minute_offset = minute - now.minute
    second_offset = -now.second
    print(f"Your watch is off by {minute_offset} minutes and {second_offset} seconds.")
    if abs(minute_offset) != 0:
        adjustment_target = datetime.datetime.now()
        input(f"Adjust your watch to {adjustment_target.time()}, and press Enter.")
    input("Press Enter to save a checkpoint. (Ctrl+C to exit.)")
    if not P("checkpoints.csv").exists():
        P("checkpoints.csv").write_text("time,minute_offset,second_offset\n")
    with P("checkpoints.csv").open("a") as f:
        f.write(f"{now},{minute_offset},{second_offset}\n")
    print("Checkpoint saved.")


if __name__ == "__main__":
    main()
