#!/usr/bin/env python3
"""Offline evidence analyzer for Modern Workplace and Cloud Operations portfolio scenarios.

The tool consumes public-safe JSON exports or synthetic fixtures. It performs deterministic,
read-only checks and emits structured findings. It does not call Intune, Azure or AWS APIs.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
        raise ValueError("Input must be a JSON object or list of JSON objects.")
    return data


def finding(code: str, severity: str, subject: str, evidence: str, next_check: str) -> dict[str, str]:
    return {
        "code": code,
        "severity": severity,
        "subject": subject,
        "evidence": evidence,
        "safe_next_check": next_check,
    }


def analyze_intune(items: list[dict[str, Any]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    now = datetime.now(timezone.utc)
    for d in items:
        name = str(d.get("deviceName") or d.get("id") or "unknown-device")
        if str(d.get("complianceState", "")).lower() not in {"compliant", "unknown"}:
            out.append(finding(
                "INTUNE-NONCOMPLIANT", "high", name,
                f"complianceState={d.get('complianceState')}",
                "Review the device compliance details and assigned policy before remediation.",
            ))
        if str(d.get("encryptionState", "")).lower() in {"off", "notencrypted", "not encrypted", "false"}:
            out.append(finding(
                "INTUNE-ENCRYPTION-OFF", "high", name,
                f"encryptionState={d.get('encryptionState')}",
                "Confirm BitLocker policy assignment and local protector state.",
            ))
        if str(d.get("secureBoot", "")).lower() in {"off", "disabled", "false"}:
            out.append(finding(
                "INTUNE-SECUREBOOT-OFF", "medium", name,
                f"secureBoot={d.get('secureBoot')}",
                "Validate device model/firmware state and the organization's compliance requirement.",
            ))
        raw = d.get("lastSync")
        if raw:
            try:
                dt = datetime.fromisoformat(str(raw).replace("Z", "+00:00"))
                age_h = (now - dt.astimezone(timezone.utc)).total_seconds() / 3600
                if age_h > 72:
                    out.append(finding(
                        "INTUNE-STALE-SYNC", "medium", name,
                        f"lastSync={raw} ({age_h:.0f}h ago)",
                        "Confirm device connectivity, enrollment state and management extension health.",
                    ))
            except ValueError:
                out.append(finding(
                    "INTUNE-SYNC-PARSE", "low", name,
                    f"Unparseable lastSync={raw}",
                    "Validate the export timestamp format before interpreting device freshness.",
                ))
    return out


def analyze_azure(items: list[dict[str, Any]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for d in items:
        name = str(d.get("vmName") or d.get("resourceId") or "unknown-azure-resource")
        if str(d.get("resourceHealth", "")).lower() not in {"available", "unknown"}:
            out.append(finding(
                "AZURE-RESOURCE-HEALTH", "high", name,
                f"resourceHealth={d.get('resourceHealth')}",
                "Review Resource Health details and platform events before changing the workload.",
            ))
        if str(d.get("networkReachability", "")).lower() in {"failed", "unreachable", "false"}:
            out.append(finding(
                "AZURE-NETWORK", "high", name,
                f"networkReachability={d.get('networkReachability')}",
                "Check effective NSG rules, NIC/IP configuration, route tables and DNS resolution.",
            ))
        cpu = d.get("cpuPercent")
        if isinstance(cpu, (int, float)) and cpu >= 85:
            out.append(finding(
                "AZURE-HIGH-CPU", "medium", name,
                f"cpuPercent={cpu}",
                "Correlate CPU with process/workload telemetry and the incident timeline.",
            ))
        disk = d.get("diskFreePercent")
        if isinstance(disk, (int, float)) and disk <= 10:
            out.append(finding(
                "AZURE-LOW-DISK", "high", name,
                f"diskFreePercent={disk}",
                "Validate filesystem usage and growth before resizing or deleting data.",
            ))
    return out


def analyze_aws(items: list[dict[str, Any]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for d in items:
        name = str(d.get("instanceId") or d.get("name") or "unknown-aws-instance")
        if str(d.get("state", "")).lower() not in {"running", "unknown"}:
            out.append(finding(
                "AWS-INSTANCE-STATE", "high", name,
                f"state={d.get('state')}",
                "Review instance state transition reason and recent operational changes.",
            ))
        if str(d.get("statusCheck", "")).lower() not in {"ok", "passed", "unknown"}:
            out.append(finding(
                "AWS-STATUS-CHECK", "high", name,
                f"statusCheck={d.get('statusCheck')}",
                "Separate system-status and instance-status evidence before recovery action.",
            ))
        if str(d.get("networkReachability", "")).lower() in {"failed", "unreachable", "false"}:
            out.append(finding(
                "AWS-NETWORK", "high", name,
                f"networkReachability={d.get('networkReachability')}",
                "Review security groups, NACLs, routes, DNS and target service state.",
            ))
        cpu = d.get("cpuPercent")
        if isinstance(cpu, (int, float)) and cpu >= 85:
            out.append(finding(
                "AWS-HIGH-CPU", "medium", name,
                f"cpuPercent={cpu}",
                "Correlate CloudWatch CPU with workload and process-level evidence.",
            ))
        disk = d.get("diskFreePercent")
        if isinstance(disk, (int, float)) and disk <= 10:
            out.append(finding(
                "AWS-LOW-DISK", "high", name,
                f"diskFreePercent={disk}",
                "Confirm filesystem usage and growth before modifying EBS or deleting data.",
            ))
    return out


ANALYZERS = {"intune": analyze_intune, "azure": analyze_azure, "aws": analyze_aws}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=sorted(ANALYZERS), required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    items = load_json(args.input)
    findings = ANALYZERS[args.kind](items)
    result = {
        "kind": args.kind,
        "source": str(args.input),
        "records": len(items),
        "findings": findings,
        "summary": {
            "high": sum(1 for x in findings if x["severity"] == "high"),
            "medium": sum(1 for x in findings if x["severity"] == "medium"),
            "low": sum(1 for x in findings if x["severity"] == "low"),
        },
        "boundary": "Deterministic offline analysis only; no live tenant/cloud connection and no remediation.",
    }
    rendered = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
