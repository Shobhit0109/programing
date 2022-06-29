# TODO: Complete the check_spell function
def check_spell(expression):
  # TODO: Add logic to determine if the expression contains spells
  return False

def main():
  # Get the number of test cases
  num_tests = int(input())
  for t in range(num_tests):
    # Get the Witch's expression
    expression = input()
    answer = 'Nothing.'
    if(check_spell(expression)):
      answer = 'Spell!'
    print(f'Case #{t+1}: {answer}')

if __name__ == '__main__':
  main()
