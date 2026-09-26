import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "python" / "analyze_ops_evidence.py"


class EvidenceAnalyzerTests(unittest.TestCase):
    def run_case(self, kind, payload):
        with tempfile.TemporaryDirectory() as td:
            src = Path(td) / "input.json"
            src.write_text(json.dumps(payload), encoding="utf-8")
            cp = subprocess.run(
                [sys.executable, str(SCRIPT), "--kind", kind, "--input", str(src)],
                check=True, capture_output=True, text=True,
            )
            return json.loads(cp.stdout)

    def test_intune_flags_compliance_and_encryption(self):
        result = self.run_case("intune", [{
            "deviceName": "LAB-W11-01",
            "complianceState": "noncompliant",
            "encryptionState": "off",
            "secureBoot": "enabled",
        }])
        codes = {x["code"] for x in result["findings"]}
        self.assertIn("INTUNE-NONCOMPLIANT", codes)
        self.assertIn("INTUNE-ENCRYPTION-OFF", codes)

    def test_azure_flags_network_and_low_disk(self):
        result = self.run_case("azure", [{
            "vmName": "az-vm-01", "resourceHealth": "available",
            "networkReachability": "failed", "cpuPercent": 20, "diskFreePercent": 8,
        }])
        codes = {x["code"] for x in result["findings"]}
        self.assertEqual(codes, {"AZURE-NETWORK", "AZURE-LOW-DISK"})

    def test_aws_healthy_instance_has_no_findings(self):
        result = self.run_case("aws", [{
            "instanceId": "i-demo", "state": "running", "statusCheck": "ok",
            "networkReachability": "ok", "cpuPercent": 15, "diskFreePercent": 60,
        }])
        self.assertEqual(result["findings"], [])


if __name__ == "__main__":
    unittest.main()
