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
