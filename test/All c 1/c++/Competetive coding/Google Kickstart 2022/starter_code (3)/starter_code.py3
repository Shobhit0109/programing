# TODO: Complete the get_minimum_overall_delivery_time function
def get_minimum_overall_delivery_time(rows, columns, grid):
  # TODO: Add logic to calculate the minimum overall delivery time
  return 0

def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
    # Get the grid dimensions
    rows, columns = map(int, input().split())
    # Get the grid
    grid = [list(map(int, input())) for _ in range(rows)]
    print(f'Case #{t+1}:',
          get_minimum_overall_delivery_time(rows, columns, grid))

if __name__ == '__main__':
  main()
