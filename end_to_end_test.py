from stellar_matchmaker import stellar_matchmaker 
import pytest 
import numpy as np

class end_to_end_test():
    """
    This class is for testing the end to end test
    """
    def test_star_on_the_edge():
        """
        test for when the star is on the edge of RA range (~360 deg)
        selecting ra=0 deg would give the result with stars RA~0 deg and RA~360 deg so the difference between the maximum and minimum RA should be around 360 deg
        """
        diff_ra_expected  = 360
        obs, param = stellar_matchmaker.get_inputs(askinfo=False, ra='00:0:0', dec='0:00:00',)
        result = stellar_matchmaker.run_query(obs, param)

        result = stellar_matchmaker.organize(obs, param, result)
        diff_ra = np.max(result['ra'])-np.min(result['ra'])
        assert diff_ra == pytest.approx(diff_ra_expected, abs=0.2*diff_ra_expected)
        print('you passed the end to end test :)')
test = end_to_end_test
test.test_star_on_the_edge()
