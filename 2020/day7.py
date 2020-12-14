import re

bag_pattern = re.compile("([a-z ]+) bags contain (.*)")
contents_pattern = re.compile("([0-9]+) ([a-z ]+) bag")


def parse_rules(rules):
    content_rules = {}
    for rule in rules:
        bag, contents = re.match(bag_pattern, rule).groups()
        content_bags = [b for c, b in re.findall(contents_pattern, contents)]
        content_rules[bag] = content_bags
    return content_rules


def count_possible_bags(color, rules):
    bags = set()

    def can_this_bag_contain(color, this_color, rules):
        nonlocal bags

        content_colors = rules[this_color]
        if color in content_colors:
            return True
        else:
            for c in content_colors:
                if can_this_bag_contain(color, c, rules):
                    return True
            return False

    for bag in rules.keys():
        if can_this_bag_contain(color, bag, rules):
            bags.add(bag)
    return len(bags)


if __name__ == "__main__":
    rules = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".splitlines()

    content_rules = parse_rules(rules)
    print(content_rules)

    print(count_possible_bags("shiny gold", content_rules))

    with open("2020/inputs/day7.txt") as f:
        rules = [l.strip() for l in f]
    content_rules = parse_rules(rules)

    print(f"Number of bags: {count_possible_bags('shiny gold', content_rules)}")
