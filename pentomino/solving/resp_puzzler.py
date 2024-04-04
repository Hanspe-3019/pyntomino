''' Puzzler ist als Generator implementiert
    yield Response
'''
from dataclasses import dataclass

(INTERRUPT, UNDO, FINISH, SOLUTION) = range(4)
@dataclass()
class Response():
    ' Response Dataclass'
    resptype: int
    message: str

    def __repr__(self):
        type_astext = (
            'Interrupt Undo Finished Solution'.split()[self.resptype]
        )
        return f'Resp {type_astext:9s} : {self.message}'

    def is_undo(self):
        ' ist es undo?'
        return self.resptype==UNDO
    def is_finish(self):
        ' ist es finish?'
        return self.resptype==FINISH
def interrupt(msg):
    ' Interrrupt Response an die GUI'
    return Response(INTERRUPT, msg)
def undo(msg):
    ' undo Response nur intern, geht nicht an die GUI'
    return Response(UNDO, msg)
def solution(msg):
    ' solution Response, wird an die GUI weitergereicht'
    return Response(SOLUTION, msg)
def finish(msg):
    ' finish Response, wird an die GUI weitergereicht'
    return Response(FINISH, msg)
