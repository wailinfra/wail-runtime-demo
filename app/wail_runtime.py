import time
import uuid
import logging

from events import Event, ExecutionTrace
from anomalies import LatencySpikeDetector
from behaviour_signals import derive_behaviour_signals

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class WailRuntime:
    def __init__(self):
        self.execution_id = None
        self.start_time = None
        self.trace = None

        # Demo-safe anomaly detector
        self.latency_detector = LatencySpikeDetector(
            threshold_seconds=0.9
        )

    def start_execution(self):
        self.execution_id = str(uuid.uuid4())
        self.start_time = time.perf_counter()

        self.trace = ExecutionTrace(
            execution_id=self.execution_id,
            start_time=self.start_time,
            events=[]
        )

        logging.info(
            f"WAIL | execution started | id={self.execution_id}"
        )

        self.trace.add_event(Event(
            type="execution_started",
            timestamp=self.start_time,
            data={}
        ))

    def observe_token(self, token: str):
        now = time.perf_counter()
        elapsed = now - self.start_time

        logging.info(
            f"WAIL | token observed | token='{token}' | t={elapsed:.4f}s"
        )

        # Token event
        self.trace.add_event(Event(
            type="token_observed",
            timestamp=now,
            data={
                "token": token,
                "elapsed": elapsed
            }
        ))

        # --- Anomaly detection (V1) ---
        if self.latency_detector.check(elapsed):
            logging.warning(
                f"WAIL | anomaly detected | type=latency_spike | t={elapsed:.4f}s"
            )

            self.trace.add_event(Event(
                type="anomaly_detected",
                timestamp=now,
                data={
                    "anomaly_type": "latency_spike",
                    "elapsed": elapsed
                }
            ))

    def end_execution(self):
        total = time.perf_counter() - self.start_time

        logging.info(
            f"WAIL | execution completed | id={self.execution_id} | total={total:.4f}s"
        )

        self.trace.add_event(Event(
            type="execution_completed",
            timestamp=time.perf_counter(),
            data={
                "total_duration": round(total, 4),
                "token_count": len(
                    [e for e in self.trace.events
                     if e.type == "token_observed"]
                )
            }
        ))

        # --- DEMO BEHAVIOUR SIGNAL DERIVATION ---
        behaviour_signals = derive_behaviour_signals(
            self.trace.events
        )

        self.trace.behaviour_signals = behaviour_signals

        # Terminal output (demo visibility)
        logging.info("WAIL | derived runtime behaviour signals")
        for key, value in behaviour_signals.items():
            logging.info(f"WAIL | signal | {key}={value}")

        return self.trace
