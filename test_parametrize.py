# -*- coding: UTF-8 -*-
import pytest
# 参数化
class Test_abc(object):



    @pytest.mark.parametrize("a",[3,8])
    def test_d1(self,a):
        print(f'\ntest_d1在执行{a}')

    @pytest.mark.parametrize("a", [(3, 8),(5,6)])
    def test_d21(self, a):
        print(f'test_d2在执行{a}')

if __name__ == '__main__':
    pytest.main(['test_parametrize.py'])
