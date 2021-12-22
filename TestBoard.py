import pytest

from Board import Board

@pytest.fixture
def board3by3():
   return Board(2, 3, None)

class TestBoard:

    def testIsBoard(board3by3):
        assert (board3by3.isBoard() == True)
    
    # @pytest.mark.parametrize("x,y", [(0,0,0,1,1,1,2,2,2),
    #                                      (0,1,2,0,1,2,0,1,2)])

    def testInnerIsBoard(board3by3):
        for i in range(2):
            for j in range(2):
                assert board3by3.peek(i,j).isBoard() == True

    def testItems(board3by3):
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        assert board3by3.peek(i,j).peek(k,l).isBoard() == False

    @pytest.mark.parametrize("vals,bool",[("O,X,O,"+
                                           "X,X,O,"+
                                           "O,O,X",

                                           "X,O,X,"+
                                           "X,X,O,"+
                                           "X,O,O,"), (True, False)])  
    
    def testTie(board3by3, vals, bool):
        v = vals.split(",")
        for k in range(board3by3.Size*board3by3.Size):
            board3by3.choose(k%3,k//3,v[k])
        assert (board3by3.tie() == bool)