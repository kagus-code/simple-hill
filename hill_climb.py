from numpy import random


objective_function = lambda x: 2 - x**2
INITIAL_STEP_SIZE = 0.2
LOWER_BOUNDARY = -5
UPPER_BOUNDARY = 5
MAX_STEPS_WITHOUT_IMPROVEMENT = 100


def main():
    # generate a random start point
    start_point = random.uniform(LOWER_BOUNDARY, UPPER_BOUNDARY)
    # evaluation of the initial point
    state_value = objective_function(start_point)
    step_size = INITIAL_STEP_SIZE
    # run the hill climb
    for i in range(MAX_STEPS_WITHOUT_IMPROVEMENT):
#  Propose the right and left neighbor,

        left_neighbor = start_point - step_size
        right_neighbor = start_point + step_size
# calculate the value of the ojective function there: state's,
        left_value = objective_function(left_neighbor)
        right_value = objective_function(right_neighbor)

        if left_value > state_value and left_value > right_value:
          #  assign the next state to the left state if it is higher the current and the right state
            start_point = left_neighbor
            state_value = left_value
        elif right_value > state_value and right_value > left_value:
          #  assign the next state to the right state if it is higher the current and the left state
            start_point = right_neighbor
            state_value = right_value
        # track progress 
        print(f"X: {start_point}. State: {state_value}")
    print()
    # return max value of the objective function and its state
    print(f"Result:\nXmax: {start_point}. Smax: {state_value}")
    

if __name__ == '__main__':
    main()