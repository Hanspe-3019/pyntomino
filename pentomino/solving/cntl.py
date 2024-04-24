'''Data Class with properties controlling the solver 
'''
from dataclasses import dataclass

INTERRUPT_LEVELS = [
    # (timeout in secs)
    .0,      # 0
    .2,      # 1
    1.0,    # 2
    10.0,   # 3
    30.0,   # 4
    60.0,   # 5
    120.0,  # 6
    3600,   # 7 Nolimit
]

@dataclass
class PuzzlerCntl():
    ' einige properties für timout usw. '
    # pylint: disable=too-many-instance-attributes
    to_be_placed: int
    prompt_when:int = 0
    int_level: int = 1
    timeout: float = .2
    timeout_before_stop: float = .2
    start: float = .0
    cum_placing: int = 0
    cnt_placing: int = 0

    def adjust_interrupt(self, down):
        ' Anpassung der Intervall-Länge der Interrupts '
        i = self.int_level
        i = max(i - 1, 0) if down else min(i + 1, len(INTERRUPT_LEVELS) - 1)
        self.timeout = INTERRUPT_LEVELS[i]
        old = INTERRUPT_LEVELS[self.int_level]
        self.int_level = i
        if i == 0:
            self.prompt_when = 1
        elif i == len(INTERRUPT_LEVELS) - 1:
            self.prompt_when = 0

        return (
            f'Timeout {old:.1f} -> {self.timeout:.1f}'
            f'{"." if self.prompt_when == 0 else "!"} '
        )
