from stellar_matchmaker import stellar_matchmaker 
import pytest 

class unit_test():
    def test_get_inputs(self):
        try:
            stellar_matchmaker.get_inputs(askinfo=False,ra='12:00:00')
            print("You passed the test :)")
        except ValueError as exc:
            pytest.fail(exc)
            
test= unit_test()
test.test_get_inputs() 
        
    
