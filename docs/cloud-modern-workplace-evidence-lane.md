# Cloud + Modern Workplace evidence lane

This lane adds reproducible portfolio evidence for two areas that were previously represented mainly by training and documentation.

## What is implemented

A deterministic offline analyzer accepts public-safe JSON exports or committed synthetic fixtures for:

- **Intune / Modern Workplace:** compliance, encryption, Secure Boot and management-sync evidence;
- **Azure Operations:** Resource Health, connectivity, CPU and disk-pressure evidence;
- **AWS Operations:** instance state, status checks, connectivity, CPU and disk-pressure evidence.

The analyzer produces structured findings with severity, exact evidence and a safe next check.

## Why offline first

The public portfolio must not depend on production credentials or imply tenant/cloud ownership that has not been demonstrated. Live exports may be used only after redaction. The committed fixtures are synthetic and exist so the workflow is reproducible in CI.

## What this demonstrates

- interpreting endpoint-management and cloud-operational evidence;
- separating platform state from workload/network symptoms;
- deterministic triage rules;
- evidence-based escalation;
- safe boundaries before remediation;
- Python automation and automated verification.

## What this does not demonstrate

- production ownership of Intune, Azure or AWS;
- tenant-wide administration;
- automatic remediation;
- IaC provisioning;
- enterprise cloud architecture.

Those capabilities should only be claimed when supported by separate evidence.
