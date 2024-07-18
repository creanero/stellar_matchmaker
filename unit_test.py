from stellar_matchmaker import stellar_matchmaker 
import pytest 

class unit_test():
    def test_get_inputs_normal_ra(self):
        try:
            stellar_matchmaker.get_inputs(askinfo=False,ra='12:00:00')
            print("You passed the test :)")
        except ValueError as exc:
            pytest.fail(exc)

    def test_get_inputs_high_ra(self):
        try:
            stellar_matchmaker.get_inputs(askinfo=False,ra='25:00:00')
        except ValueError:
            print('over 24 hours in RA does not work as expected, so you passed the test :)')
            
test= unit_test()
test.test_get_inputs_normal_ra() 
test.test_get_inputs_high_ra() 

        
    
