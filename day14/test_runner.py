from day14.bitmask import BitMask
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