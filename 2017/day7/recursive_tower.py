import collections
import re


class UnbalancedException(RuntimeError):
    def __init__(self, correct_weight):
        self.correct_weight = correct_weight


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


def get_balanced_tower_weight(programs, name):
    program = programs[name]
    weight = program['weight']
    sub_weights = []
    children = program['children']
    if children:
        for child in children:
            sub_weights.append(get_balanced_tower_weight(programs, child))
        raise_if_unbalanced(programs, children, sub_weights)
    return weight + sum(sub_weights)


def raise_if_unbalanced(programs, children, weights):
    counts = collections.Counter(weights)
    if len(counts) > 1:
        (correct, _), (anomalous, _) = counts.most_common()
        dvalue = correct - anomalous
        idx = weights.index(anomalous)
        anomalous_program = programs[children[idx]]
        correct_weight = anomalous_program['weight'] + dvalue
        raise UnbalancedException(correct_weight=correct_weight)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_data = f.readlines()
    print("Day 7, part 1:", find_bottom_program(input_data))
