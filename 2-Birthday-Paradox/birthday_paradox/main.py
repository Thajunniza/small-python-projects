from birthday_paradox import simulator
from birthday_paradox import constants
from birthday_paradox import utils
from birthday_paradox import config

def main():
    print(constants.MSG_WELCOME1)
    print(constants.MSG_WELCOME2)

    # Step 1: Get group size from user
    while True:
        usr_input = input(f"{constants.MSG_INPUT.format(config.MAX_GROUP_SIZE)}")
        if utils.validate_group_size(usr_input):
            break
        print(constants.MSG_INPUT_ERROR.format(config.MAX_GROUP_SIZE))
    
     # Step 2: Generate birthdays
    people = int(usr_input)
    birthdays = simulator.generate_birthdays(int(people))
    
    # Step 3 : Print All Generated Birthday
    n = len(birthdays)
    print(constants.MSG_GENERATED_BIRTHDAYS.format(people))
    for i,day in enumerate(birthdays):
        print(utils.format_bday(day),end=", " if i != n-1 else " ")
    print() 

    # Step 4: Lets run the Simulation for 1 time
    print(constants.MSG_SIMULATION.format(people,1))
    # Find Collision
    collision = simulator.get_collision(birthdays)
    if collision:
        simulator.display_collision(collision)
    else:
        print(constants.MSG_NO_COLLISION)
    
    # Step 5 : Lets find the probability by running 100,000 simulations
    print(f"\nRunning {config.DEFAULT_SIMULATION_COUNT} simulations for group size {people}...")
    input(constants.MSG_SIMULATION_ENTER)
    collision_cnt = simulator.run_simulations(people, config.DEFAULT_SIMULATION_COUNT)
    # Calculate probability
    probability = round(collision_cnt / config.DEFAULT_SIMULATION_COUNT * 100, 2)

    # Display results using constants
    print("\n" + constants.MSG_SIMULATION_RESULT_HEADER)
    print(constants.MSG_SIMULATION_MATCH.format(simulations=config.DEFAULT_SIMULATION_COUNT, group_size=people))
    print(constants.MSG_SIMULATION_COUNT.format(count=collision_cnt))
    print(constants.MSG_SIMULATION_PROBABILITY.format(group_size=people, probability=probability))
    print(constants.MSG_SIMULATION_FUN)




if __name__ == "__main__":
    main()