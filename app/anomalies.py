class LatencySpikeDetector:
    def __init__(self, threshold_seconds: float):
        self.threshold = threshold_seconds

    def check(self, elapsed: float) -> bool:
        return elapsed > self.threshold
