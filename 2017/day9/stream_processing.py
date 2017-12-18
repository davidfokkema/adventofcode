class StreamProcessor(object):
    def parse_file(self, filename):
        with open(filename) as f:
            c = f.read(1)
            assert c == '{'
            return self.process_group(f)

    def eat_garbage(self, stream):
        while True:
            c = stream.read(1)
            if c == '!':
                # cancel next character
                stream.read(1)
            elif c == '>':
                break
            elif c == '':
                raise RuntimeError("Stream dried up")

    def process_group(self, stream, parent_score=0):
        num_groups = 1
        my_score = parent_score + 1
        total_score = my_score

        while True:
            c = stream.read(1)
            if c == '}':
                return num_groups, total_score
            if c == '{':
                N, child_score = self.process_group(stream, my_score)
                num_groups += N
                total_score += child_score
            if c == '<':
                self.eat_garbage(stream)
            elif c == '':
                raise RuntimeError("Stream dried up")


if __name__ == '__main__':
    processor = StreamProcessor()
    num_groups, score = processor.parse_file('input.txt')
    print("Day 9, part 1:", score)
