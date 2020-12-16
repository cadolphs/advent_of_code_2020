from day14.memory import FloatingMemory
from day14.bitmask import BitMask, IndexBitMask
from day14.runner import Runner


class DummyMemory:
    pass


def test_runner_calls_mask():
    memory = DummyMemory()
    runner = Runner(memory)

    runner.execute("mask = XX10X")
    assert BitMask("XX10X") == memory.mask


def test_runner_sets_memory():
    memory = [0] * 36
    runner = Runner(memory)

    runner.execute("mem[10] = 42")

    assert 42 == memory[10]


def test_example_part2():
    memory = FloatingMemory()
    runner = Runner(memory, mask_factory=IndexBitMask)

    commands = "mask = 000000000000000000000000000000X1001X\nmem[42] = 100\nmask = 00000000000000000000000000000000X0XX\nmem[26] = 1"

    for command in commands.split("\n"):
        runner.execute(command)

    assert sum(memory.values()) == 208
