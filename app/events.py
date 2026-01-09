from dataclasses import dataclass, field


@dataclass
class Event:
    type: str
    timestamp: float
    data: dict


@dataclass
class ExecutionTrace:
    execution_id: str
    start_time: float
    events: list
    behaviour_signals: dict = field(default_factory=dict)

    def add_event(self, event: Event):
        self.events.append(event)

    def to_dict(self):
        return {
            "execution_id": self.execution_id,
            "start_time": self.start_time,
            "events": [
                {
                    "type": e.type,
                    "timestamp": e.timestamp,
                    "data": e.data
                }
                for e in self.events
            ],
            "behaviour_signals": self.behaviour_signals
        }
