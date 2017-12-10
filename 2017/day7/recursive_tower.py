import re


def find_bottom_program(input_data):
    upper_programs = find_upper_programs(input_data)
    for line in input_data:
        program = re.match('[a-z]+', line).group(0)
        if program not in upper_programs:
            return program


def find_upper_programs(input_data):
    upper_programs = []
    for line in input_data:
        try:
            bottom, top = line.split('->')
        except ValueError:
            pass
        else:
            programs = re.findall('[a-z]+', top)
            upper_programs.extend(programs)
    return upper_programs
  
      
def build_tree_structure(input_data):
    programs = {}
    for line in input_data:
        name, weight = re.match('([a-z]+) \(([0-9]+)\)', line).groups()
        try:
            left, right = line.split(' -> ')
            children = right.strip().split(', ')
        except ValueError:
            children = []
        programs[name] = {'weight': int(weight), 'children': children}
    return programs
          

if __name__ == '__main__':
    with open('input.txt') as f:
        input_data = f.readlines()
    print("Day 7, part 1:", find_bottom_program(input_data))
