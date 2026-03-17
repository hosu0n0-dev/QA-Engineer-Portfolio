from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List
import pandas as pd

@dataclass
class StepResult:
    tc_id: str
    cycle: int
    step_no: int
    step_name: str
    description: str
    start_time: datetime
    end_time: datetime
    duration_sec: float
    result: str
    expected: str
    actual: str
    remark: str

class ReportBuilder:
    def __init__(self) -> None:
        self.step_results: List[StepResult] = []

    def add_step(self, tc_id: str, cycle: int, step_no: int, step_name: str, description: str, start_time: datetime, end_time: datetime, result: str, expected: str, actual: str, remark: str = "") -> None:
        duration = round((end_time - start_time).total_seconds(), 3)
        self.step_results.append(StepResult(tc_id, cycle, step_no, step_name, description, start_time, end_time, duration, result, expected, actual, remark))

    def _results_dataframe(self) -> pd.DataFrame:
        if not self.step_results:
            return pd.DataFrame(columns=["tc_id","cycle","step_no","step_name","description","start_time","end_time","duration_sec","result","expected","actual","remark"])
        return pd.DataFrame([vars(step) for step in self.step_results])

    def _cycle_summary_dataframe(self, results: pd.DataFrame) -> pd.DataFrame:
        if results.empty:
            return pd.DataFrame(columns=["tc_id","cycle","cycle_result","total_steps","pass_steps","fail_steps","fail_step_no","fail_step_name"])
        rows = []
        for cycle, df_cycle in results.groupby("cycle", sort=True):
            fail_rows = df_cycle[df_cycle["result"] == "FAIL"]
            rows.append({
                "tc_id": str(df_cycle.iloc[0]["tc_id"]),
                "cycle": int(cycle),
                "cycle_result": "FAIL" if not fail_rows.empty else "PASS",
                "total_steps": int(df_cycle.shape[0]),
                "pass_steps": int((df_cycle["result"] == "PASS").sum()),
                "fail_steps": int((df_cycle["result"] == "FAIL").sum()),
                "fail_step_no": "" if fail_rows.empty else int(fail_rows.iloc[0]["step_no"]),
                "fail_step_name": "" if fail_rows.empty else str(fail_rows.iloc[0]["step_name"]),
            })
        return pd.DataFrame(rows)

    def _summary_dataframe(self, results: pd.DataFrame, cycle_summary: pd.DataFrame, default_tc_id: str) -> pd.DataFrame:
        total_cycle = int(cycle_summary.shape[0])
        pass_cycle = int((cycle_summary["cycle_result"] == "PASS").sum()) if total_cycle else 0
        fail_cycle = int((cycle_summary["cycle_result"] == "FAIL").sum()) if total_cycle else 0
        total_steps = int(results.shape[0])
        pass_steps = int((results["result"] == "PASS").sum()) if total_steps else 0
        fail_steps = int((results["result"] == "FAIL").sum()) if total_steps else 0
        cycle_pass_rate = round((pass_cycle / total_cycle * 100.0), 2) if total_cycle else 0.0
        step_pass_rate = round((pass_steps / total_steps * 100.0), 2) if total_steps else 0.0
        return pd.DataFrame([{
            "tc_id": default_tc_id,
            "total_cycle": total_cycle,
            "pass_cycle": pass_cycle,
            "fail_cycle": fail_cycle,
            "pass_rate_percent": cycle_pass_rate,
            "total_steps": total_steps,
            "pass_steps": pass_steps,
            "fail_steps": fail_steps,
            "step_pass_rate_percent": step_pass_rate,
        }])

    def save(self, output_path: Path, default_tc_id: str) -> Path:
        results = self._results_dataframe()
        cycle_summary = self._cycle_summary_dataframe(results)
        summary = self._summary_dataframe(results, cycle_summary, default_tc_id)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            summary.to_excel(writer, sheet_name="Summary", index=False)
            cycle_summary.to_excel(writer, sheet_name="CycleSummary", index=False)
            results.to_excel(writer, sheet_name="Results", index=False)
        return output_path
