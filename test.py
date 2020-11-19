import unittest
import pjeuler
import time

class TestTools(unittest.TestCase):
  def test_lcm(self):
    self.assertEqual(pjeuler.tools.lcm(27,36),108)
    self.assertEqual(pjeuler.tools.lcm(27,36,8),216)
  def test_gcd(self):
    self.assertEqual(pjeuler.tools.gcd(27,36),9)
    self.assertEqual(pjeuler.tools.gcd(27,36,8),1)
  def test_smart_mod(self):
    base = 3
    exp = 17
    mod = 124
    x = (base**exp)%mod
    y = pjeuler.tools.smart_mod(base,exp,mod)
    self.assertEqual(x,y)
    
def mypr(i,t,sol,res):
  print("Problem",str(i).rjust(3), " took ",str(round(t,2)).rjust(5)," seconds. Expected ",str(sol).rjust(15)," Got ",str(res).rjust(15))
    
class TestProblems(unittest.TestCase):
  def test(self):
    
    # Solution definition    
    s = [233168,4613732,6857,906609,232792560,
         25164150,104743,23514624000,31875000,142913828922,
         70600674,76576500,5537376230,837799,137846528820,
         1366,21124,1074,171,648,
         31626,871198282,4179871,2783915460,4782,
         983,-59231]#,669171001,9183,443839,
         #73682,45228,100,40730,55,
         #872187,748317,932718654,840,210,
         #7652413,162,16695334890,5482660,1533776805,
         #5777,134043,9110846700,296962999629,997651]
    sols = dict(zip(range(1,len(s)+1),s))
    sols[67] = 7273
    sols[77] = 71
    sols[85] = 2772
    sols[97] = 8739992577
    
    print()
    for idx, sol in sols.items():
      t0 = time.time()
      res = pjeuler.pjeuler(idx)
      t = time.time() - t0
      self.assertEqual(sol,res)
      mypr(idx,t,sol,res)
    print()
