import unittest
import time
import pjeuler

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
  def test_first100(self):
    # Solution definition
    s = [233168,4613732,6857,906609,232792560,
         25164150,104743,23514624000,31875000,142913828922,
         70600674,76576500,5537376230,837799,137846528820,
         1366,21124,1074,171,648,
         31626,871198282,4179871,2783915460,4782,
         983,-59231,669171001,9183,443839,
         73682,45228,100,40730,55,
         872187,748317,932718654,840,210,
         7652413,162,16695334890,5482660,1533776805,
         5777,134043,9110846700,296962999629,997651,
         121313,142857,4075,376,249,
         972,153,26241,129448,26033,
         28684,127035954683,49,1322,272,
         661,7273,6531031914842725,510510,8319823,
         428570,303963552391,7295372,402,
         161667,190569291,71,55374,73162890,40886,
         427337,260324,425185,101524,2772,
         1818,1097343,7587457,743,1217,
         14234,8581146,1258,518408346,14316,
         24702,8739992577,18769,709,756872327473]
    sols = dict(zip(range(1,len(s)+1),s))

    print()
    for idx, sol in sols.items():
      t0 = time.time()
      res = pjeuler.pjeuler(idx)
      t = time.time() - t0
      self.assertEqual(sol,res)
      mypr(idx,t,sol,res)
    print()

  def test_rest(self):
    sols = {}
    sols[101] = 'd382b0cc25e82446da83d3a792e1cd27'
    sols[102] = '74db120f0a8e5646ef5a30154e9f6deb'
    sols[104] = 'c8771ddd4df191098d70a8e94dd1cde7'
    sols[107] = 'b0db1202ec966e7855ca23626eb285b8'
    sols[108] = '765ba18edd2844db2db95fba25d2f3e7'
    sols[109] = 'e6aebd5be1ba81557dbcc5f6f57bbe5c'
    sols[110] = '591a7a92f10322866e6a02f3b2386a1c'
    sols[112] = 'e08c982713a1c2bd3637dd489199722e'
    sols[113] = 'a9e504ee704c87f9bddad6d3ffe39532'
    sols[114] = 'de48ca72bf252a8be7e0aad762eadcf8'
    sols[115] = '006f52e9102a8d3be2fe5614f42ba989'
    sols[116] = 'c21ca0ec54e6d1646a953a480f68feb4'
    sols[117] = '542612809b3dd08cf518b85450fce8d6'
    sols[119] = '72fddfa6c52a120892ade628f3819da4'
    sols[120] = '0dd05ec40fe11279c2203b72e92a450a'
    sols[121] = '51de85ddd068f0bc787691d356176df9'
    sols[122] = 'b710915795b9e9c02cf10d6d2bdb688c'
    sols[123] = '71497f728b86b55d965edbf1849cca8d'
    sols[124] = 'f228d2e6f9099153388e9470180c8302'
    sols[125] = '1b5635e8ab723e01570ca783129493dd'
    sols[126] = '387d6ae83cbc6fa0b9192b56bf095c49'
    sols[145] = '705e8444ad9c92e9a7589fb97515a9b6'
    #sols[155] = 'da0a3fc900cc8ae42d514e280524ee39'
    sols[169] = 'd149d4836703a8908becea56ddd3ed42'
    sols[172] = 'f5f260ee21ead7478403c2ccd18a1829'
    sols[173] = '177f825c89a68aefae37b8dec9bb8a9b'
    #sols[177] = 'd7a85236af930db0f7e84f2de8ee7ac2'
    sols[179] = 'bafa0132bc7fc422a8d53bebb9d003c9'
    sols[187] = 'b3e6977523511d2cbbef8fccb1e394db'
    sols[191] = 'e04dfa598b22a87570f63063f3ff595d'
    sols[199] = '0f8fd87159c28ae5fea6ac91a95d48dd'

    sols[203] = 'd7ec16d216c923d3c927f46cfc914e92'
    sols[205] = 'ba6c6c3888227a0799eca38191b587be'
    sols[206] = '09f9d87cb4b1ebb34e1f607e55a351d8'
    #sols[216] = 'e512153424a482deb9de401ac0465a72'
    sols[235] = '41b13508789be1001308e065d4f83ea2'

    sols[301] = 'f47b7d975a5ebd3b66af0968ef5e1cdb'
    sols[317] = 'b0e2bec93bfe598ade5d3d1141f76bdd'
    sols[345] = 'cf3b784c8593890043b17e24088125d4'
    sols[349] = '412b0faec10b3adb415363d2df26530d'
    sols[353] = '211b5626459be71baefc78478d18bdc3'
    sols[357] = 'ed25b13b18a21c1077fed00ef42f503b'
    sols[363] = 'd577f7de8bcdac23329cd166d1bc7a8e'

    sols[493] = 'e7a3d17e900134dd57ae44da7e31603c'

    sols[808] = 'b3026f0182a9ff9bbe9193fa55c87d03'

    print()
    for idx, sol in sols.items():
      t0 = time.time()
      res = pjeuler.my_hash(pjeuler.pjeuler(idx))
      t = time.time() - t0
      self.assertEqual(sol,res)
      mypr(idx,t,sol,res)
    print()
