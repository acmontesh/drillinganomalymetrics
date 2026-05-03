import unittest
from ..src.drillinganomalymetrics.metrics import calculate_accuracy_metrics

class Testing_Metrics(unittest.TestCase):

    def setUp(self):
        self.results = calculate_accuracy_metrics(
            ["test_risk_1.csv", "test_risk_2.csv", "test_risk_3.csv"],
            labelsPositive=[
                ("2024-04-24 21:36","2024-04-28 21:36"),
                ("2023-05-01 02:59","2023-05-01 04:20"),
                ("2018-05-17 18:05","2018-05-17 20:05"),
            ],
            formatDatesInputs=[
                "%Y-%m-%d %H:%M:%S-05:00",
                "%Y-%m-%d %H:%M:%S",
                "%Y-%m-%d %H:%M:%S-05:00"
            ],
            formatDateLabels="%Y-%m-%d %H:%M",
            thersholdPredPos=0.62, delta=360, alpha=0.80
        )

    def test_recall(self):
        r, _, _, _, _ = self.results
        self.assertAlmostEqual( r, 0.8045, places=4 )

    def test_precision(self):
        _, p, _, _, _ = self.results
        self.assertAlmostEqual( p, 1.0000, places=4 )

    def test_f1(self):
        _, _, f1, _, _ = self.results
        self.assertAlmostEqual( f1, 0.8917, places=4 )

if __name__ == '__main__':
    unittest.main(  )