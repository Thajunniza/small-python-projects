from birthday_paradox import simulator
from birthday_paradox import utils  # optional helper

def main():
    group_size = 25  # example, can be replaced with input later

    # Generate birthdays (numbers only)
    birthdays = simulator.generate_birthdays(group_size)

    # Format birthdays for display (month + day)
    formatted_birthdays = [utils.format_bday(day) for day in birthdays]

    # Find Collision
    collision = simulator.get_collision(birthdays)

    # Print results
    print(f"Group size: {group_size}")
    print("Birthdays:", ", ".join(formatted_birthdays))
    simulator.display_collision(collision)

if __name__ == "__main__":
    main()
