import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rat.Runner('Усейн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in TournamentTest.all_results.keys():
            print(TournamentTest.all_results[key])

    # def tearDown(self):
    #     print(TournamentTest.all_results)

    def test_run(self):
        tournament = rat.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.update({'test1': {key: value.name for (key, value) in results.items()}})
        max_key = max(results.keys())
        self.assertTrue(results[max_key] == 'Ник')

    def test_run2(self):
        tournament = rat.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.update({'test2': {key: value.name for (key, value) in results.items()}})
        max_key = max(results.keys())
        self.assertTrue(results[max_key] == 'Ник')

    def test_run3(self):
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results.update({'test3': {key: value.name for (key, value) in results.items()}})
        max_key = max(results.keys())
        self.assertTrue(results[max_key] == 'Ник')



if __name__ == '__main__':
    unittest.main()
