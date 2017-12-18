class StreamProcessor(object):
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

    def process_group(self, stream):
        num_groups = 1
        while True:
            c = stream.read(1)
            if c == '}':
                return num_groups, 0
            if c == '{':
                N, _ = self.process_group(stream)
                num_groups += N
            if c == '<':
                self.eat_garbage(stream)
            elif c == '':
                raise RuntimeError("Stream dried up")
