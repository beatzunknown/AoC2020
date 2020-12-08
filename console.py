class Console:
    def __init__(self, code):
        self.instructions = [(op, int(arg)) for op, arg in code]
        self.code_size = len(self.instructions)
        self.accumulator = 0
        self.ip = 0 # instruction pointer
        self.instruction_set = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop
        }
        self.memory = set()
        self.halted = False

    def execute(self):
        while self.ip < self.code_size and not self.is_looped() and not self.halted:
            self.memory.add(self.ip)
            op, arg = self.instructions[self.ip]
            self.instruction_set[op](arg)
        return (self.accumulator, self.ip < self.code_size)

    def jmp(self, arg):
        self.ip += arg

    def acc(self, arg):
        self.accumulator += arg
        self.ip += 1

    def nop(self, arg):
        self.ip += 1

    def halt(self):
        self.halted = True

    def is_halted(self):
        return self.halted

    def is_looped(self):
        return (self.ip in self.memory)