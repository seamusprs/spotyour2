import spotyour2.stats.testreaddata
import spotyour2.stats.testshowstats
import unittest

# run this outside of the spotyour2 directory!

tests = unittest.TestLoader().discover(start_dir="spotyour2/stats", pattern="test*.py")

# print("Tests: ", tests)

if __name__ == "__main__":
   unittest.TextTestRunner(verbosity=2).run(tests)







