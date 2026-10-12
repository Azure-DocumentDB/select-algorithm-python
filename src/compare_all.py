"""Run all nine isolated algorithm/metric cases; any failure is nonzero."""
from runner import cli

if __name__ == "__main__":
    raise SystemExit(cli(comparison=True))
