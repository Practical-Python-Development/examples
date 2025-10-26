"""Weekly step tracker."""


class WeeklyStepTracker:
    """Weekly step tracker."""

    def __init__(self):
        """Initialize the tracker."""
        self.week = {}

    def add_day(self, day_name: str, steps: list[int] = []) -> None:  # noqa
        """Register a day in the tracker with optional step data."""
        self.week[day_name] = steps

    def record_steps(self, day_name: str, step_count: int) -> None:
        """Add a step count record for a given day."""
        if day_name not in self.week:
            self.add_day(day_name)

        self.week[day_name].append(step_count)

    def daily_average(self, day_name: str) -> float:
        """Return the average steps for a given day."""
        records = self.week.get(day_name, [])

        if not records:
            raise ValueError(f"No step data recorded for {day_name}.")

        return sum(records) / len(records)

    def weekly_average(self) -> float:
        """Return the overall average step count across all days."""
        all_steps = [s for steps in self.week.values() for s in steps]

        if not all_steps:
            return 0.

        return sum(all_steps) / len(all_steps)


def main():
    """Entry point."""
    tracker = WeeklyStepTracker()

    tracker.record_steps("Monday", 7000)
    tracker.record_steps("Monday", 8000)
    tracker.record_steps("Tuesday", 5000)
    tracker.record_steps("Wednesday", 9000)
    tracker.record_steps("Wednesday", 6000)

    print(f"Overall weekly average: {tracker.weekly_average():.0f} steps")

    print("Average steps per day:")
    for day in ["Monday", "Tuesday", "Wednesday"]:
        avg = tracker.daily_average(day)
        print(f"  {day}: {avg:.0f} steps")


if __name__ == "__main__":
    main()
